# Ajan Talimatları (Codex, Claude Code ve diğer yapay zekâ ajanları)

Bu depo, HASANCA müzik projesinin video arşivi ve **viral video analiz
sistemini** içerir.

## Depo yapısı

- `HASANCA-*.mp4` — kullanıcının (Hasan Çataltepe / HASANCA) kendi müzik
  videoları. Analizlerde "benim videolarım" bunlardır.
- `viral-analiz/` — viral video analiz sistemi. **Video analizi istendiğinde
  buradan çalış.**
- `index.html`, `privacy-policy.html`, `terms.html`, `callback.html` —
  web sayfaları. `tiktok*.txt` — TikTok site doğrulama dosyaları.

## Video analizi görevi geldiğinde

Kullanıcı sohbette video URL'leri (YouTube / TikTok / Instagram) veya
kendi video dosyalarını verdiğinde:

1. **Önce oku:** `viral-analiz/README.md` (sistemin tamamı) ve
   `viral-analiz/ANALIZ_REHBERI.md` (zorunlu rapor protokolü).
2. Her video için: `cd viral-analiz && python -m viral_analiz hazirla "<URL|dosya>" -o "calismalar/<tarih>-<konu>/<viral-N|benim-N>"`
3. `metadata.json`'u oku, `kareler/` içindeki damgalı kareleri görsel
   olarak sırayla incele.
4. `RAPOR.md`'yi ANALIZ_REHBERI.md protokolüne göre yaz.
   **Eksiksizlik kontrol listesi tamamlanmadan rapor teslim edilemez —
   öneriler her zaman eksiksiz olmalı, bu kullanıcının açık talebidir.**
5. Rapor + metadata'yı commit'le ve push'la. Videolar ve kareler
   `.gitignore` gereği push edilmez.

## Genel kurallar

- Kullanıcıyla iletişim dili Türkçedir.
- Bağımlılıklar: `pip install -r viral-analiz/requirements.txt` ve
  sistemde `ffmpeg` (yoksa `apt-get install -y ffmpeg`).
- Harici LLM API'si KULLANILMAZ — analizi ajan kendisi yapar.
