#!/usr/bin/env python3
"""Hasanca Buffer slot doldurucu — GitHub Actions cron icin.

State (cursor + skip) state.json'da tutulur, her run sonra commit edilir.
Buffer token GH secret olarak BUFFER_TOKEN env'inde olmali.
"""
import json
import os
import sys
import urllib.request
import urllib.error
from pathlib import Path

ROOT = Path(__file__).parent
SCHED = json.loads((ROOT / "schedule.json").read_text(encoding="utf-8"))
STATE_PATH = ROOT / "state.json"
STATE = json.loads(STATE_PATH.read_text(encoding="utf-8"))

TOKEN = os.environ.get("BUFFER_TOKEN", "").strip()
if not TOKEN:
    print("ERROR: BUFFER_TOKEN env yok")
    sys.exit(1)

ENDPOINT = "https://api.buffer.com/graphql"

MUTATION = """mutation CreatePost($input: CreatePostInput!) {
  createPost(input: $input) {
    __typename
    ... on PostActionSuccess { post { id } }
    ... on LimitReachedError { message }
    ... on InvalidInputError { message }
    ... on UnexpectedError { message }
    ... on RestProxyError { message link code }
  }
}"""


def call(query, variables=None):
    body = {"query": query}
    if variables is not None:
        body["variables"] = variables
    data = json.dumps(body).encode("utf-8")
    req = urllib.request.Request(
        ENDPOINT,
        data=data,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {TOKEN}",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return json.loads(r.read())
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        print(f"  HTTP {e.code}: {body[:200]}")
        return None
    except Exception as e:
        print(f"  NET err: {e}")
        return None


def try_post(platform, channel_id, song):
    hook = song["hook"]
    hashtags = SCHED["hashtags"]
    url = f"{SCHED['base_url']}/{song['file']}.mp4"
    caption = f"{hook} {hashtags}"
    yt_title = hook
    yt_desc = f"{hook}\n\n{hashtags} #shorts"

    inp = {
        "channelId": channel_id,
        "schedulingType": "automatic",
        "mode": "customScheduled",
        "dueAt": song["due"],
        "text": caption,
        "assets": [{"video": {"url": url}}],
    }
    if platform == "Instagram":
        inp["metadata"] = {"instagram": {"type": "reel", "shouldShareToFeed": True}}
    elif platform == "YouTube":
        inp["text"] = yt_desc
        inp["metadata"] = {
            "youtube": {"title": yt_title, "privacy": "public", "categoryId": "10"}
        }
    return call(MUTATION, {"input": inp})


def main():
    songs = SCHED["songs"]
    n = len(songs)
    totals = {"ok": 0, "limit": 0, "skip": 0, "err": 0, "rate": 0}

    for plat, ch_id in SCHED["channels"].items():
        idx = STATE["nextIndex"].get(plat, 0)
        skip = set(STATE.get("skip", {}).get(plat, []))
        print(f"\n=== {plat} cursor={idx} skip={sorted(skip)} ===")
        while idx < n:
            if idx in skip:
                print(f"  [{idx+1}/{n}] SKIP (zaten pending)")
                totals["skip"] += 1
                idx += 1
                continue
            song = songs[idx]
            resp = try_post(plat, ch_id, song)
            if resp is None:
                print(f"  [{idx+1}/{n}] {song['hook']} -> NETWORK/RATE LIMIT, dur")
                totals["rate"] += 1
                break
            data = resp.get("data", {}).get("createPost") or {}
            t = data.get("__typename", "")
            if t == "PostActionSuccess":
                print(f"  [{idx+1}/{n}] {song['hook']} -> {song['due']} OK")
                totals["ok"] += 1
                idx += 1
            elif t == "LimitReachedError":
                print(f"  [{idx+1}/{n}] {song['hook']} -> LIMIT (10/10), dur")
                totals["limit"] += 1
                break
            else:
                msg = data.get("message", resp.get("errors", "?"))
                print(f"  [{idx+1}/{n}] {song['hook']} -> HATA ({t}): {msg}")
                totals["err"] += 1
                idx += 1
        STATE["nextIndex"][plat] = idx

    STATE_PATH.write_text(
        json.dumps(STATE, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    print(f"\n=== OZET ===")
    print(f"OK: {totals['ok']} | LIMIT: {totals['limit']} | SKIP: {totals['skip']} | RATE: {totals['rate']} | HATA: {totals['err']}")
    print(f"Yeni cursor: {STATE['nextIndex']}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"FATAL: {e}", file=sys.stderr)
        # Rate limit / network errors should not fail the workflow run
        sys.exit(0)
    sys.exit(0)
