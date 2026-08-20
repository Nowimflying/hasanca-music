# Viral Video Analiz Sistemi

Çok izlenen (viral) videoları kare kare ve metadata düzeyinde analiz
edip **"neden ve nasıl çok izlendi"** sorusunu cevaplayan; ardından
kullanıcının kendi videolarını aynı süzgeçten geçirip hatalarını bulan
ve yeni video için **eksiksiz** öneri paketi üreten sistem.

Bu sistem **harici bir LLM API'si kullanmaz.** Analizi, depoya bağlanan
yapay zekâ ajanının kendisi yapar (Claude Code, Codex veya benzeri).
Ajan videoyu indirir, kareleri çıkarır, kareleri kendi görüş
yeteneğiyle inceler ve raporu yazar.

---

## Yapay zekâ ajanları için: sisteme bağlandığında ne yapacaksın

Bu depoya bağlanan ajan (Claude Code, Codex vb.) şu sözleşmeye uyar:

1. **Kullanıcı sohbette URL verir** — viral referans videolar
   (YouTube / TikTok / Instagram) ve/veya kendi videoları. Kullanıcının
   kendi videoları depo kökündeki `HASANCA-*.mp4` dosyaları da olabilir.
2. Ajan her video için hazırlık komutunu çalıştırır (aşağıda).
3. Ajan `metadata.json`'u okur ve `kareler/` içindeki **damgalı
   kareleri görsel olarak, sırayla, atlamadan** inceler.
4. Ajan `ANALIZ_REHBERI.md`'deki protokole göre `RAPOR.md` yazar.
   **Rehberdeki eksiksizlik kontrol listesi tamamlanmadan rapor teslim
   edilemez.** Bu, kullanıcının açık talebidir: öneriler her zaman
   eksiksiz olmalı.
5. Rapor ve metadata commit edilip push edilir. Videolar ve kareler
   `.gitignore` gereği push edilmez (boyut + telif).

> Önce oku: [`ANALIZ_REHBERI.md`](ANALIZ_REHBERI.md) — zorunlu rapor
> bölümleri ve eksiksizlik sözleşmesi oradadır.

---

## Kurulum

Gereksinimler: Python 3.10+, `ffmpeg` (sistemde kurulu olmalı).

```bash
cd viral-analiz
pip install -r requirements.txt   # yt-dlp + Pillow
ffmpeg -version                   # yoksa: apt-get install -y ffmpeg
```

## Kullanım

Tek komut vardır: `hazirla`. Videoyu indirir (veya yerel dosyayı
kopyalar), metadata'yı yazar, kareleri çıkarıp damgalar.

```bash
# Viral referans video (URL'den indirilir)
python -m viral_analiz hazirla "https://www.youtube.com/watch?v=XXXX" \
    -o "calismalar/2026-08-20-gaddar/viral-1"

# Kullanıcının kendi videosu (depodaki yerel dosya)
python -m viral_analiz hazirla "../HASANCA-GADDAR.mp4" \
    -o "calismalar/2026-08-20-gaddar/benim-1"

# Kare aralığını değiştirmek (varsayılan 0.5 sn)
python -m viral_analiz hazirla "<URL>" -o "<klasor>" --aralik 1.0
```

## Çıktı yapısı

```
viral-analiz/
├── README.md              ← bu dosya
├── ANALIZ_REHBERI.md      ← zorunlu analiz protokolü + eksiksizlik listesi
├── requirements.txt
├── viral_analiz/          ← Python paketi
│   ├── indir.py           ← yt-dlp ile indirme + metadata (yükleme tarihi/saati dahil)
│   ├── kareler.py         ← ffmpeg kare çıkarma + PIL damgalama
│   └── cli.py             ← komut satırı arayüzü
└── calismalar/            ← her analiz çalışması ayrı klasör
    └── 2026-08-20-gaddar/         ← <tarih>-<konu>
        ├── viral-1/
        │   ├── video.mp4          ← git'e girmez
        │   ├── metadata.json      ← commit edilir
        │   └── kareler/           ← git'e girmez
        │       ├── kare_0001.jpg  ← damga: "#001 | 00:00.0"
        │       └── ...
        ├── benim-1/               ← aynı yapı
        └── RAPOR.md               ← eksiksiz analiz raporu, commit edilir
```

## Sistem nasıl çalışır — teknik detay

### 1. İndirme ve metadata (`indir.py`)

- `yt-dlp` ile YouTube / TikTok / Instagram desteklenir.
- Kaydedilen metadata: başlık, açıklama, etiketler, kanal, süre,
  izlenme / beğeni / yorum sayıları, çözünürlük.
- **Yükleme tarihi VE saati** kaydedilir (`timestamp` alanından, UTC).
  Saat bilgisini platform vermediyse yalnızca tarih yazılır.
- `yayindan_beri_gun` ve `gunluk_ortalama_izlenme` hesaplanır —
  viral hızın asıl ölçüsü budur (2 günde 1M ≠ 2 yılda 1M).
- Yerel dosyalarda platform verisi olmadığından dosya adı başlık olur,
  değiştirilme zamanı tahmini yükleme zamanı olarak işaretlenir
  (`yukleme_zamani_tahmini: true`).

### 2. Kare çıkarma ve damgalama (`kareler.py`)

- `ffmpeg -vf fps=1/0.5` ile **0.5 saniyede bir** kare çıkarılır
  (`--aralik` ile ayarlanabilir).
- Her karenin **sol üst köşesine** siyah kutu içinde sarı yazıyla
  damga basılır: `#012 | 00:06.0` → 12. kare, videonun 6.0 saniyesi.
  Amaç: analiz sırasında kare sırası/zamanı karışmasın, yanlış atlama
  olmasın.
- Kareler en fazla 800 px genişliğe küçültülür (analiz için yeterli,
  disk ve bağlam maliyeti düşük).

### 3. Analiz (yapay zekâ ajanı — API yok)

- Ajan kareleri görsel olarak okur (Claude Code'da `Read` aracı, Codex'te
  eşdeğeri) ve metadata ile birleştirip `ANALIZ_REHBERI.md` protokolünü
  uygular.
- Rapor zorunlu bölümleri: viral video analizi (metadata + kare kare +
  sentez), kullanıcı videosu hata listesi, karşılaştırma tablosu,
  **eksiksiz yeni video paketi** (10+ başlık, tam açıklama, 30+ etiket,
  saniye saniye akış, süre, hook, CTA, efekt, yayın zamanı, kapak) ve
  eski videolar için yeniden düzenleme planı.

## Sık karşılaşılan durumlar

| Durum | Çözüm |
|---|---|
| Bulut oturumunda (Claude Code web / Codex cloud) indirme `403 / Tunnel connection failed` veriyor | Ortamın **ağ politikası** o alan adını engelliyor. Kullanıcı, claude.ai ortam ayarlarından ağ erişimini genişletmeli (youtube.com, googlevideo.com, tiktok.com, instagram.com, cdninstagram.com) ya da videoyu kendisi indirip dosya olarak vermeli — `hazirla` yerel dosyayla da çalışır |
| `yt-dlp` indirmesi coğrafi/oturum engeline takıldı | Kullanıcıdan videoyu indirip depoya/oturuma dosya olarak vermesini iste; `hazirla` yerel dosyayla da çalışır |
| Video çok uzun (>5 dk), kare sayısı çok yüksek | `--aralik 1.0` veya `2.0` kullan; hook analizi için ilk 10 saniyeyi ayrıca `--aralik 0.5` ile çıkar |
| Instagram/TikTok saat bilgisi vermedi | Metadata'da `yukleme_saati: null` kalır; raporda bunun belirtilmesi zorunludur |
| ffmpeg yok | `apt-get update && apt-get install -y ffmpeg` |

## Tasarım kararları

- **API yok:** analiz, oturumdaki ajanın kendi görüş yeteneğiyle yapılır.
  Maliyet ve anahtar yönetimi yoktur; sistemin tamamı bu depo + ajan.
- **Damgalı kareler:** ajanın "kaçıncı saniye" atıflarının doğrulanabilir
  olması için zaman bilgisi karenin üzerine basılıdır.
- **Videolar git dışı:** GitHub dosya limiti ve telif nedeniyle yalnızca
  metadata + rapor versiyonlanır. Aynı analiz gerekirse video URL'den
  yeniden indirilir.
