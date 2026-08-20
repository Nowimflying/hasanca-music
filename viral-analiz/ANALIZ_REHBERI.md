# ANALİZ REHBERİ — Zorunlu Protokol

Bu belge, viral video analizini yapan yapay zekâ ajanının (Claude Code,
Codex vb.) **uymak zorunda olduğu** protokoldür. Rapor bu rehberdeki
bölümlerin TAMAMINI içermeden teslim edilemez.

## Temel kural: EKSİKSİZLİK

> Kullanıcının videolarına öneri verildiğinde öneriler **her zaman
> eksiksiz olmalıdır.** Hiçbir bölüm "kısaca", "özetle", "birkaç örnek"
> diye geçiştirilemez. Aşağıdaki kontrol listesindeki her madde raporda
> dolu olmalıdır. Bir madde gerçekten uygulanamıyorsa (ör. yerel dosyada
> izlenme verisi yoktur) raporda o maddenin altına *neden* uygulanamadığı
> açıkça yazılır — madde sessizce atlanamaz.

## İş akışı

1. Kullanıcı sohbette viral video URL'leri (YouTube / TikTok / Instagram)
   ve kendi videolarını (URL veya depodaki yerel dosya) verir.
2. Her video için hazırlık komutu çalıştırılır:
   ```bash
   python -m viral_analiz hazirla "<URL veya dosya>" -o "calismalar/<tarih>-<konu>/<viral-N | benim-N>"
   ```
3. Ajan her videonun `metadata.json` dosyasını okur ve `kareler/`
   klasöründeki damgalı kareleri **görsel olarak, sırayla, atlamadan**
   inceler. Kare damgaları (`#012 | 00:06.0`) sıra numarası ve videodaki
   zamandır — analizde zamana atıf bu damgayla yapılır.
4. Rapor `calismalar/<tarih>-<konu>/RAPOR.md` olarak yazılır, commit
   edilip push edilir. Videolar ve kareler git'e girmez (.gitignore).

## Rapor bölümleri (hepsi zorunlu)

### 1. Viral video analizi (her viral video için ayrı ayrı)

**1a. Metadata analizi**
- Başlık: neden tıklatıyor (merak boşluğu, duygu, anahtar kelime, uzunluk)
- Açıklama: yapısı, anahtar kelime kullanımı, link/CTA var mı
- Etiketler: tam liste, hangi arama niyetlerini yakalıyor
- Yükleme tarihi + saati; yayından bu yana geçen gün;
  **günlük ortalama izlenme** (viral hızın asıl ölçüsü)
- İzlenme / beğeni / yorum oranları

**1b. Kare kare görsel analiz**
- **Hook (ilk 3 saniye = ilk ~6 kare):** ilk karede ne var, izleyiciyi
  ne durduruyor, hangi karede konu belli oluyor
- **Tempo:** sahne/plan değişim sıklığı (kaç karede bir kesme var)
- **Efektler:** geçişler, zoom, yazı animasyonu, renk filtresi,
  hangi zaman damgalarında
- **Ekran yazıları (overlay):** ne yazıyor, hangi saniyelerde, konumu
- **CTA'lar:** abone ol / takip et / yorum yaz çağrıları hangi saniyede,
  nasıl (sözlü, yazılı, görsel)
- **Görsel kimlik:** renk paleti, ışık, çekim kalitesi, dikey/yatay format
- **Kapak / ilk kare:** küçük resim işlevi görüyor mu

**1c. Sentez: bu video neden ve nasıl çok izlendi**
- En az 5 somut neden, her biri kare damgası veya metadata kanıtıyla

### 2. Kullanıcının videosunun analizi (her video için ayrı ayrı)

- 1a ve 1b'deki TÜM boyutlar aynı derinlikte uygulanır
- **Hata/eksik listesi:** numaralandırılmış, EKSİKSİZ liste. Her hata
  için: (a) sorun nedir, (b) hangi karede/metadata alanında görülüyor,
  (c) viral referanslar bunu nasıl doğru yapıyor

### 3. Karşılaştırma tablosu

Viral videolar ile kullanıcı videosu yan yana: hook, süre, tempo,
overlay kullanımı, CTA sayısı ve zamanlaması, başlık stili, etiket
sayısı, yükleme zamanı.

### 4. Yeni video önerisi — EKSİKSİZ paket

- **4a.** En az **10 başlık alternatifi** (her birinin neden işe
  yarayacağı bir cümleyle)
- **4b.** Kopyala-yapıştır hazır **tam açıklama metni** (platform başına)
- **4c.** En az **30 etiket** (platform başına gruplu: geniş / orta / niş)
- **4d.** **Saniye saniye içerik akışı**: 0:00'dan videonun sonuna kadar
  her bölümün süresi, görüntüsü, sesi, ekran yazısı
- **4e.** **Toplam süre önerisi** ve gerekçesi (platform başına)
- **4f.** **Hook planı**: ilk 3 saniyenin tam tarifi
- **4g.** **CTA planı**: kaç CTA, hangi saniyelerde, hangi kelimelerle
- **4h.** **Efekt ve görsel öneriler**: geçişler, yazı stilleri, filtre
- **4i.** **Yayın zamanı önerisi**: gün + saat, viral referansların
  yükleme zamanlarına dayanarak
- **4j.** **Kapak / ilk kare önerisi**

### 5. Eski videolar için yeniden düzenleme planı

Kullanıcının analiz edilen her eski videosu için:
- Mevcut halinden ne kesilecek / ne eklenecek (kare damgalarıyla)
- Yeni başlık, yeni açıklama, yeni etiketler (tam liste)
- Yeniden yayınlama mı, metadata güncellemesi mi — gerekçeli karar

### 6. Eksiksizlik kontrol listesi

Rapor sonunda ajan şu listeyi işaretleyerek doğrular:

```
- [ ] Her viral video için 1a + 1b + 1c tamam
- [ ] Her kullanıcı videosu için tam analiz + numaralı hata listesi
- [ ] Karşılaştırma tablosu var
- [ ] 10+ başlık, tam açıklama, 30+ etiket
- [ ] Saniye saniye akış planı 0:00'dan sona kadar kesintisiz
- [ ] Süre, hook, CTA, efekt, yayın zamanı, kapak önerileri dolu
- [ ] Her eski video için yeniden düzenleme planı var
- [ ] Uygulanamayan maddelerin nedeni raporda açıkça yazılı
```

İşaretlenemeyen madde varsa rapor bitmemiştir; ajan eksiği tamamlar,
sonra teslim eder.
