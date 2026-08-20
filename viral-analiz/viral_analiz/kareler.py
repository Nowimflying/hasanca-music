"""Kare cikarma ve damgalama.

ffmpeg ile videodan varsayilan 0.5 saniyede bir kare cikarilir. Her
karenin sol ust kosesine kucuk bir kutu icinde SIRA NUMARASI ve o
karenin videodaki ZAMANI (saniye) basilir. Boylece analiz sirasinda
"hangi kare, videonun kacinci saniyesi" karisikligi ve yanlis atlama
olmaz.
"""

from __future__ import annotations

import subprocess
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

KARE_KLASORU = "kareler"
MAKS_GENISLIK = 800  # damgalanmis kareler bu genislige kucultulur

_FONT_YOLLARI = [
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
]


def _font_yukle(boyut: int) -> ImageFont.ImageFont:
    for yol in _FONT_YOLLARI:
        if Path(yol).exists():
            return ImageFont.truetype(yol, boyut)
    return ImageFont.load_default(size=boyut)


def _zaman_metni(saniye: float) -> str:
    dakika = int(saniye // 60)
    return f"{dakika:02d}:{saniye % 60:04.1f}"


def _damgala(kare_yolu: Path, sira_no: int, saniye: float) -> None:
    """Karenin sol ust kosesine '#012 | 00:06.0' damgasi basar."""
    with Image.open(kare_yolu) as img:
        img = img.convert("RGB")
        if img.width > MAKS_GENISLIK:
            oran = MAKS_GENISLIK / img.width
            img = img.resize((MAKS_GENISLIK, int(img.height * oran)))

        cizim = ImageDraw.Draw(img)
        metin = f"#{sira_no:03d} | {_zaman_metni(saniye)}"
        font = _font_yukle(max(14, img.width // 45))
        kutu = cizim.textbbox((0, 0), metin, font=font)
        dolgu = 4
        cizim.rectangle(
            [0, 0, kutu[2] + dolgu * 2, kutu[3] + dolgu * 2], fill=(0, 0, 0)
        )
        cizim.text((dolgu, dolgu), metin, font=font, fill=(255, 255, 0))
        img.save(kare_yolu, quality=85)


def kareleri_cikar(
    video_dosyasi: Path, hedef_klasor: Path, aralik: float = 0.5
) -> list[Path]:
    """Videodan `aralik` saniyede bir kare cikarir, damgalar.

    Kareler `hedef_klasor/kareler/kare_0001.jpg ...` olarak yazilir.
    Donen liste sira numarasina gore siralidir.
    """
    kare_klasoru = hedef_klasor / KARE_KLASORU
    kare_klasoru.mkdir(parents=True, exist_ok=True)
    for eski in kare_klasoru.glob("kare_*.jpg"):
        eski.unlink()

    subprocess.run(
        [
            "ffmpeg",
            "-hide_banner",
            "-loglevel",
            "error",
            "-i",
            str(video_dosyasi),
            "-vf",
            f"fps=1/{aralik}",
            "-qscale:v",
            "3",
            str(kare_klasoru / "kare_%04d.jpg"),
        ],
        check=True,
    )

    kareler = sorted(kare_klasoru.glob("kare_*.jpg"))
    for i, kare in enumerate(kareler, start=1):
        _damgala(kare, i, (i - 1) * aralik)

    print(f"  {len(kareler)} kare cikarildi ve damgalandi ({aralik} sn aralikla)")
    return kareler
