"""Video indirme ve metadata cikarma (YouTube, TikTok, Instagram).

yt-dlp ile videoyu indirir; baslik, aciklama, etiketler, izlenme/begeni
sayilari ve ozellikle YUKLEME TARIHI + SAATI kaydedilir. Yukleme zamani
onemli: "cok izlenmis" degerlendirmesi yayin tarihine gore yapilir
(2 gunde 1M izlenme ile 2 yilda 1M izlenme ayni sey degildir).
"""

from __future__ import annotations

import json
import shutil
from datetime import datetime, timezone
from pathlib import Path

import yt_dlp

VIDEO_DOSYA_ADI = "video.mp4"
METADATA_DOSYA_ADI = "metadata.json"


def _yukleme_zamani(info: dict) -> dict:
    """upload_date (YYYYMMDD) ve timestamp (epoch) alanlarindan
    okunabilir tarih + saat uretir. Saat bilgisi yalnizca platform
    timestamp verdiyse kesindir; yoksa sadece tarih yazilir."""
    zaman = {"yukleme_tarihi": None, "yukleme_saati": None, "yukleme_iso": None}
    ts = info.get("timestamp") or info.get("release_timestamp")
    if ts:
        dt = datetime.fromtimestamp(ts, tz=timezone.utc)
        zaman["yukleme_tarihi"] = dt.strftime("%Y-%m-%d")
        zaman["yukleme_saati"] = dt.strftime("%H:%M:%S UTC")
        zaman["yukleme_iso"] = dt.isoformat()
    elif info.get("upload_date"):
        dt = datetime.strptime(info["upload_date"], "%Y%m%d")
        zaman["yukleme_tarihi"] = dt.strftime("%Y-%m-%d")
        zaman["yukleme_iso"] = dt.date().isoformat()
    return zaman


def _metadata_cikar(info: dict, url: str) -> dict:
    meta = {
        "url": url,
        "platform": info.get("extractor_key"),
        "baslik": info.get("title"),
        "aciklama": info.get("description"),
        "etiketler": info.get("tags") or [],
        "kanal": info.get("channel") or info.get("uploader"),
        "kanal_takipci": info.get("channel_follower_count"),
        "sure_saniye": info.get("duration"),
        "izlenme": info.get("view_count"),
        "begeni": info.get("like_count"),
        "yorum": info.get("comment_count"),
        "cozunurluk": f"{info.get('width')}x{info.get('height')}"
        if info.get("width")
        else None,
        "indirilme_zamani": datetime.now(timezone.utc).isoformat(),
    }
    meta.update(_yukleme_zamani(info))

    # Yayindan bu yana gecen gun ve gunluk ortalama izlenme:
    # viral hizini olcmek icin rapora girer.
    if meta["yukleme_iso"] and meta["izlenme"]:
        yuklenme = datetime.fromisoformat(meta["yukleme_iso"])
        if yuklenme.tzinfo is None:
            yuklenme = yuklenme.replace(tzinfo=timezone.utc)
        gecen_gun = max((datetime.now(timezone.utc) - yuklenme).days, 1)
        meta["yayindan_beri_gun"] = gecen_gun
        meta["gunluk_ortalama_izlenme"] = round(meta["izlenme"] / gecen_gun)
    return meta


def videoyu_indir(url: str, hedef_klasor: Path) -> dict:
    """URL'deki videoyu indirir, metadata.json yazar, metadata dondurur."""
    hedef_klasor.mkdir(parents=True, exist_ok=True)
    secenekler = {
        "outtmpl": str(hedef_klasor / "video.%(ext)s"),
        "format": "bv*[ext=mp4]+ba[ext=m4a]/b[ext=mp4]/bv*+ba/b",
        "merge_output_format": "mp4",
        "quiet": True,
        "no_warnings": True,
        "noplaylist": True,
    }
    with yt_dlp.YoutubeDL(secenekler) as ydl:
        info = ydl.extract_info(url, download=True)

    meta = _metadata_cikar(info, url)
    meta["video_dosyasi"] = str(hedef_klasor / VIDEO_DOSYA_ADI)
    (hedef_klasor / METADATA_DOSYA_ADI).write_text(
        json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(
        f"  Indirildi: {meta['baslik']!r} — yukleme: {meta['yukleme_tarihi']} "
        f"{meta['yukleme_saati'] or ''} — izlenme: {meta['izlenme']}"
    )
    return meta


def yerel_videoyu_hazirla(dosya: Path, hedef_klasor: Path) -> dict:
    """Kullanicinin diskteki kendi videosunu analiz klasorune kopyalar.

    Yerel dosyada platform metadata'si yoktur; dosya adi baslik olarak,
    dosyanin degistirilme zamani yukleme zamani tahmini olarak kullanilir.
    """
    hedef_klasor.mkdir(parents=True, exist_ok=True)
    hedef = hedef_klasor / VIDEO_DOSYA_ADI
    shutil.copyfile(dosya, hedef)
    degistirilme = datetime.fromtimestamp(dosya.stat().st_mtime, tz=timezone.utc)
    meta = {
        "url": None,
        "platform": "yerel-dosya",
        "baslik": dosya.stem.replace("_", " "),
        "aciklama": None,
        "etiketler": [],
        "sure_saniye": None,
        "izlenme": None,
        "yukleme_tarihi": degistirilme.strftime("%Y-%m-%d"),
        "yukleme_saati": degistirilme.strftime("%H:%M:%S UTC"),
        "yukleme_iso": degistirilme.isoformat(),
        "yukleme_zamani_tahmini": True,
        "indirilme_zamani": datetime.now(timezone.utc).isoformat(),
        "video_dosyasi": str(hedef),
    }
    (hedef_klasor / METADATA_DOSYA_ADI).write_text(
        json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(f"  Yerel video hazirlandi: {dosya.name}")
    return meta
