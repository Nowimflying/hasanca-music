"""Komut satiri arayuzu.

Kullanim (analiz eden yapay zeka ajani bu komutu calistirir):

    python -m viral_analiz hazirla <URL veya yerel dosya> -o <hedef klasor>

Ornekler:

    # Viral referans video (URL'den indirilir)
    python -m viral_analiz hazirla "https://youtube.com/watch?v=XXX" \
        -o calismalar/2026-08-20-gaddar/viral-1

    # Kullanicinin kendi videosu (yerel dosya)
    python -m viral_analiz hazirla ../HASANCA-GADDAR.mp4 \
        -o calismalar/2026-08-20-gaddar/benim-1

Cikti klasoru yapisi:
    <hedef>/video.mp4          indirilen/kopyalanan video (git'e girmez)
    <hedef>/metadata.json      baslik, aciklama, etiket, yukleme tarihi/saati
    <hedef>/kareler/kare_NNNN.jpg  damgali kareler (git'e girmez)
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from .indir import videoyu_indir, yerel_videoyu_hazirla
from .kareler import kareleri_cikar


def _url_mu(kaynak: str) -> bool:
    return kaynak.startswith(("http://", "https://"))


def hazirla(kaynak: str, hedef: Path, aralik: float) -> None:
    print(f"Hazirlaniyor: {kaynak}")
    if _url_mu(kaynak):
        meta = videoyu_indir(kaynak, hedef)
    else:
        dosya = Path(kaynak)
        if not dosya.exists():
            sys.exit(f"HATA: dosya bulunamadi: {dosya}")
        meta = yerel_videoyu_hazirla(dosya, hedef)

    kareler = kareleri_cikar(Path(meta["video_dosyasi"]), hedef, aralik)

    meta["kare_sayisi"] = len(kareler)
    meta["kare_araligi_saniye"] = aralik
    (hedef / "metadata.json").write_text(
        json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    print("\nOZET")
    print(f"  Baslik   : {meta.get('baslik')}")
    print(f"  Yukleme  : {meta.get('yukleme_tarihi')} {meta.get('yukleme_saati') or ''}")
    print(f"  Izlenme  : {meta.get('izlenme')}")
    print(f"  Sure     : {meta.get('sure_saniye')} sn")
    print(f"  Kareler  : {len(kareler)} adet -> {hedef / 'kareler'}")
    print(f"  Metadata : {hedef / 'metadata.json'}")
    print("\nSiradaki adim: kareleri ve metadata'yi ANALIZ_REHBERI.md'ye gore analiz et.")


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(
        prog="viral_analiz", description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    alt = parser.add_subparsers(dest="komut", required=True)

    p = alt.add_parser("hazirla", help="Videoyu indir/kopyala, kareleri cikar ve damgala")
    p.add_argument("kaynak", help="Video URL'si (YouTube/TikTok/Instagram) veya yerel dosya yolu")
    p.add_argument("-o", "--cikti", required=True, help="Hedef klasor")
    p.add_argument(
        "--aralik", type=float, default=0.5,
        help="Kare cikarma araligi, saniye (varsayilan: 0.5)",
    )

    args = parser.parse_args(argv)
    if args.komut == "hazirla":
        hazirla(args.kaynak, Path(args.cikti), args.aralik)


if __name__ == "__main__":
    main()
