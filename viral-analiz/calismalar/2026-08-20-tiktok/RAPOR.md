# RAPOR — 2026-08-20 TikTok Viral Analizi

**Çalışma:** `viral-analiz/calismalar/2026-08-20-tiktok/`
**Kaynak:** `URLLER.txt` içindeki 5 TikTok gönderisi (kullanıcı verdi).
**Yöntem:** Her video `python -m viral_analiz hazirla` ile indirildi; kareler 0,5 sn
aralıkla damgalandı ve **tamamı sırayla görsel olarak incelendi**. viral-4 bir
TikTok **fotoğraf (photo-mode) gönderisi** olduğu için yt-dlp indiremedi; metadata
ve 3 fotoğraf TikTok embed API'sinden alındı (`viral-4/metadata.json` içindeki
`not` alanına yazıldı).

**Analiz tarihi:** 2026-08-20 (~08:00 UTC). İzlenme sayıları bu ana aittir.

---

## Genel tablo (özet)

| | viral-1 | viral-2 | viral-3 | viral-4 | viral-5 |
|---|---|---|---|---|---|
| Sanatçı/kanal | Can Güven (@can.gven85) | Can Güven (@can.gven85) | MELEX (@melexx.mp3) | MELEX (@melexx.mp3) | FEROV (@ferov.music) |
| Kanal takipçi / video sayısı | 6.608 / 176 | 6.608 / 176 | 3.189 / 100 | 3.189 / 100 | 3.750 / 203 |
| Üretildiği ülke | 🇳🇱 NL | 🇳🇱 NL | 🇩🇪 DE | 🇩🇪 DE | 🇩🇪 DE |
| Şarkı | Senin Aşkın Beni Dili Ediyor | Gözün Sadece Bende Olsun | Gözlerinle Sar Beni (teaser) | Ömrüm | Gizli Gizli |
| Ses | orijinal ses – Can Güven | orijinal ses – Can Güven | Originalton – MELEX | Originalton – MELEX | Originalton – FEROV |
| Format | Statik AI görsel + söz + dalga formu | Statik AI görsel + söz + dalga formu | FPV drone + kinetik söz yazısı | 3 fotoğraflık slayt + söz | Sahte Spotify arayüzü + hızlı kesme |
| Süre | 61 sn | 71 sn | 32 sn | slayt (3 foto) | 64 sn |
| Yükleme (UTC) | 19.08 Çarş. 16:39 | 18.08 Salı 13:51 | 19.08 Çarş. 10:52 | 08.07 Çarş. 17:32 | 02.08 Pazar 06:37 |
| İzlenme | 5.842 | **63.000** | 13.000 | 27.400 | 3.703 |
| İzlenme / takipçi oranı | 0,9× | **9,5×** | 4,1× | 8,6× | 1,0× |
| Günlük ort. izlenme | ~5.800 (1 gün) | **~31.500 (2 gün)** | ~13.000 (1 gün) | ~652 (43 gün) | ~206 (18 gün) |
| Beğeni (oran) | 258 (%4,4) | 2.082 (%3,3) | 657 (%5,1) | 1.142 (%4,2) | 177 (%4,8) |
| Yorum | 36 | 199 | 35 | 123 | 7 |
| Paylaşım (oran) | 94 (%1,6) | **971 (%1,5)** | 104 (%0,8) | 132 (%0,5) | 24 (%0,6) |
| Etiket sayısı | 0 | 0 | 5 | 5 | 5 |

(İzlenme/beğeni sayıları ilk indirme ile embed API kontrolü arasında ~1 saatte
hafif arttığı için tabloda embed API'nin daha güncel değerleri kullanıldı.)

**Tablonun en önemli bulgusu:** Beş video da 3–7 bin takipçili KÜÇÜK hesaplardan
geliyor; viral-2 takipçi sayısının **9,5 katı**, viral-4 **8,6 katı** izlenme
almış. Yani bu izlenmeler abone kitlesinden değil, TikTok'un keşfet dağıtımından
geliyor — doğru içerik kalıbıyla küçük hesap (HASANCA dahil) aynı sonucu
alabilir. İkinci bulgu: üç kanal da Avrupa'dan (NL/DE) yayın yapan
gurbetçi/diaspora üreticileri; TR+RU iki dillilik ve "Turkish x Afrohouse"
konumlandırması bu pazarın bilinçli stratejisi.

---

## 1. Viral video analizleri

### VIRAL-1 — Can Güven, "Senin Aşkın Beni Dili Ediyor"

**1a. Metadata analizi**

- **Başlık/açıklama:** `🎵 Senin Aşkın Beni Dili Ediyor ✍️ Söz & Müzik: Can Güven © Can Güven – Tüm hakları saklıdır`.
  Tıklatma mekanizması merak boşluğu değil; emoji ile ayrıştırılmış **marka/telif
  kalıbı**. Şarkı adı doğrudan duygu cümlesi olduğu için başlığın kendisi söz gibi
  okunuyor. Link/CTA yok.
- **Etiketler:** YOK (0 adet). Buna rağmen 1 günde 5,8k izlenme almış: dağıtım
  tamamen ses + izlenme sinyalinden geliyor; arama niyeti yakalanmıyor.
- **Kanal:** @can.gven85 — 6.608 takipçi, 176 video, toplam 71,8k beğeni;
  Hollanda'dan (NL) yayınlıyor. Video/beğeni oranına göre seri üretim yapan,
  ara sıra patlayan bir "şablon kanalı".
- **Ses:** "orijinal ses – Can Güven" (kendi şarkısı orijinal ses olarak bağlı;
  sesi kullanan her video kanala geri trafik üretir).
- **Yükleme:** 2026-08-19 Çarşamba 16:39 UTC (19:39 TR). Yayından bu yana ~1 gün;
  **günlük ortalama ~5.800 izlenme** — takipçi sayısının ~0,9 katı (henüz
  keşfete tam düşmemiş).
- **Oranlar:** Beğeni/izlenme %4,4 (iyi), yorum %0,62 (yüksek — açıklamada soru
  olmadığı hâlde), paylaşım 94 (%1,6 — dikkat: paylaşım oranı viral-2 ile aynı;
  içerik "gönderilebilir" nitelikte, sadece dağıtım ivmesi düşük kalmış).

**1b. Kare kare görsel analiz**

- **Hook (ilk 3 sn, #001–#006):** Daha ilk karede (#001 | 00:00.0) sahne tam kurulu:
  altın/amber ışıklı gece kulübü fonunda güneş gözlüklü, siyah elbiseli kadın (AI
  üretimi), altında dalga formu ve altın el yazısı tipografiyle şarkı adı. #002'de
  (00:00.5) ilk söz satırı beliriyor. İzleyiciyi durduran şey görsel lüks + "bu ne
  şarkısı?" merakı; konu 0,5. saniyede belli.
- **Tempo:** Plan değişimi YOK — 61 saniye boyunca tek statik görsel. Hareket
  hissi üç şeyden geliyor: dalga formu animasyonu, ~10 sn'de bir değişen söz
  satırı ve aralıklı renk/ışık nabzı (ör. #011, #031, #035, #075, #119'da görüntü
  yeşil-turkuaz tona kayıp geri dönüyor — döngülü filtre nabzı).
- **Efektler:** Renk nabzı (yukarıda), söz satırında ✨ parıltı, kalp emojisi ❤️,
  animasyonlu ses dalga formu. Geçiş/zoom yok.
- **Ekran yazıları:** Üstte söz satırı (karaoke değil, satır bloğu olarak):
  #002–#022 "Ne zaman adını söylesem içimde baharlar açıyor…", #023–#033 "İlk
  günkü gibi aşık oluyorum", #034–#048 "Senin aşkın beni sarhoş ediyor her bakışın
  deli ediyor", #049–#057 "Bu kalp senden vazgeçmiyor", #058–#064 "Adını durmadan
  söylüyor", #065–#087 "Sen benim en güzel düşümsün…", #085–#091 "tek gerçeğim
  Sensin", #092–#098 "seni seviyorum". Ortada kalıcı: "Senin Aşkın BENİ DİLİ
  EDİYOR / Söz•Müzik Can Güven".
- **CTA'lar:** TEK CTA, yazılı: #101–#118 (00:50–00:58) "Abone olmayı, yorum
  yapmayı ve beğen butonuna tıklamayı unutmayın". Videonun son 10 saniyesinde,
  söz akışı bittikten sonra.
- **Görsel kimlik:** Siyah + altın palet, sıcak tungsten ışık, dikey format
  (720x952 — tam 9:16 değil, hafif kırpık). Üretim: tek AI görsel + şablon.
- **Kapak/ilk kare:** #001 kapak işlevi görüyor: şarkı adı, sanatçı, estetik
  görsel tek karede.

**1c. Sentez — neden izlendi**

1. **İlk karede tam kurulum:** başlık kartı + estetik insan yüzü + dalga formu
   (#001); kaydırmayı durduran net "bu bir şarkı" sinyali.
2. **Söz-odaklı format:** sözler ekranda blok blok akıyor (#002–#098); izleyici
   şarkıyı "okuyarak" sonuna kadar kalıyor — izlenme süresi sinyali.
3. **Duygusal, alıntılanabilir sözler:** "Bu kalp senden vazgeçmiyor" (#049) gibi
   satırlar yorum/paylaşım tetikliyor (36 yorum, %0,63 oran).
4. **Tutarlı marka şablonu:** viral-2 ile birebir aynı kalıp; seri üretim kanal
   estetiği tanınırlık ve tekrar izlenme üretiyor.
5. **CTA'nın geç gelmesi (#101):** ilk 50 sn tamamen içerik; CTA ancak sadık
   izleyiciye gösteriliyor, erken terk tetiklenmiyor.
6. **Prime-time yükleme:** Çarşamba 19:39 TR — akşam kaydırma saati.

---

### VIRAL-2 — Can Güven, "Gözün Sadece Bende Olsun" (en güçlü performans)

**1a. Metadata analizi**

- **Başlık/açıklama:** `🎵 Gözün Sadece bende Olsun ✍️ Söz & Müzik: Can Güven © Can Güven – Tüm hakları saklıdır`.
  viral-1 ile aynı kalıp. Şarkı adı ikinci tekil şahısa emir kipi — doğrudan
  izleyiciye söylenmiş gibi okunuyor (kancayı başlık taşıyor).
- **Etiketler:** YOK. Link/CTA yok.
- **Kanal:** viral-1 ile aynı (@can.gven85, 6.608 takipçi). **63.000 izlenme =
  takipçi sayısının 9,5 katı** — dağıtım tamamen keşfetten; kanıt: küçük hesabın
  algoritmayla büyüyebildiği.
- **Ses:** "orijinal ses – Can Güven".
- **Yükleme:** 2026-08-18 Salı 13:51 UTC (16:51 TR). ~2 gün içinde 63.000 izlenme —
  **günlük ~31.500, bu çalışmanın açık farkla en hızlı videosu.**
- **Oranlar:** Beğeni %3,3, yorum 199 (%0,32 — mutlak yorum en yüksek).
  **Paylaşım 971 (%1,5) — beş videonun toplamından fazla.** "Gözün sadece bende
  olsun" cümlesi sevgiliye GÖNDERİLEN bir mesaj işlevi görüyor; videoyu büyüten
  ana sinyalin paylaşım olduğu neredeyse kesin.

**1b. Kare kare görsel analiz**

- **Hook (ilk 3 sn, #001–#006):** #001'de tam kurulum: orkestra (kemancılar,
  çellist) önünde sarılmış şık bir çift (AI üretimi), altın işlemeli el yazısıyla
  "Gözünün SADECE BENDE OLSUN", altın dalga formu. viral-1'den farkı: **iki kişi +
  orkestra** = hikâye ve prodüksiyon algısı daha yüksek. #003'te (00:01.0) ilk
  yazı ("Çeviri ve Altyazı C.Güven") giriyor.
- **Tempo:** Plan değişimi yok; tek statik görsel 71 sn. Renk/ton nabzı: #010,
  #051, #070, #086, #111, #130'da karanlıklaşma/aydınlanma dalgası.
- **Efektler:** Altın (sarı) dalga formu — viral-1'deki beyazdan daha markalı;
  ✨ parıltılar; ışık nabzı. Geçiş yok.
- **Ekran yazıları:** #003–#008 "Çeviri ve Altyazı C.Güven" (jenerik). Sözler:
  #009–#014 "Ellerini tuttuğu anda", #015–#028 "Duruyor zaman usulca / Bir ömür
  yetmez sevgine / Kalbim bağlı sonsuza", #029–#044 "Hayallerimin tek sahibi /
  Yüreğimin en güzel sesi / Benim en değerlimsin", #045–#056 "Aşkımın tek nefesi /
  Kim gelirse gelsin boşuna / Kalbimde yerin değişmez", #057–#075 "Sen benim
  kaderimsin / Bu sevda hiç bitmez", #075–#084 "Gözüm senden başkasını görmez /
  Kalbim senden başkası sevmez", #085–#096 "Sen benim en güzel şarkımsın / Bu aşk
  sonsuza dek sürer", #096–#105 "Gözüm senden başkasını görmez mez / Yüreğim
  yalnız seni özler / Senin adınla başlar", #106–#113 "hayatım ve seninle",
  #114–#121 "Güzelleşir her şey".
- **CTA'lar:** TEK CTA, yazılı: #125–#137 (01:02–01:08) "İzlediğiniz için
  teşekkür ederim. Kanalıma abone olmayı unutmayın". Son 9 saniyede.
- **Görsel kimlik:** Siyah + altın; 1080x1428 (en yüksek çözünürlüklü olanı);
  romantik "gala gecesi" sahnelemesi.
- **Kapak/ilk kare:** #001 mükemmel kapak: çift + başlık + orkestra.

**1c. Sentez — neden izlendi**

1. **Çift + orkestra sahnesi (#001):** tek yüz yerine ilişki hikâyesi; hedef
   kitlenin (romantik Türkçe pop dinleyicisi) kendini koyduğu sahne. Bu, viral-1
   ile arasındaki 10 katlık farkın en olası görsel açıklaması.
2. **Başlık kancası:** "Gözün Sadece Bende Olsun" — izleyiciye söylenen bir
   cümle; yorum bölümünü sevgiliyi etiketlemeye, videoyu sevgiliye göndermeye
   davet ediyor (199 yorum, **971 paylaşım** — asıl büyüme motoru bu).
3. **71 sn boyunca kesintisiz söz akışı:** 10 ayrı söz bloğu; her blok yeni bir
   "alıntılık cümle" (ör. "Sen benim kaderimsin", #057).
4. **İzlenme süresi tuzağı:** statik görselde değişen tek şey sözler olduğundan
   izleyici satırı okumak için bekliyor; TikTok tamamlanma oranını ödüllendiriyor.
5. **Salı 16:51 TR yüklemesi:** hafta içi akşam kuşağının başı; ilk saat ivmesini
   akşam trafiği büyütmüş.
6. **Teşekkür-CTA'sı (#125):** kibar kapanış; abonelik çağrısı videoyu bitirenlere
   geliyor.

---

### VIRAL-3 — MELEX, "Gözlerinle Sar Beni" çıkış teaser'ı

**1a. Metadata analizi**

- **Başlık/açıklama:** `28.08.2026 🖤 Gözlerinle Sar Beni çıkıyor! 🎶✨ #afrohouse #turkish #turkishafrohouse #türk #türkceşarkılar`.
  Kanca **tarihli duyuru**: çıkış gününü söyleyip merak + beklenti (pre-save
  davranışı) kuruyor. Emoji ritmi başlığı taramada öne çıkarıyor.
- **Etiketler (5):** afrohouse (geniş/global), turkish + türk (orta, kimlik),
  turkishafrohouse (niş, tam tür), türkceşarkılar (orta, TR arama niyeti).
  Hem global tür arayanı hem Türkçe içerik arayanı yakalıyor.
- **Kanal:** @melexx.mp3 — 3.189 takipçi, 100 video, toplam 72k beğeni;
  Almanya'dan (DE) yayınlıyor. Profil imzası konumlandırmayı açıkça yazıyor:
  "DJ | Producer 🇹🇷 / ÖMRÜM (OUT NOW) / Afro House • Deep House • Melodic
  Techno / IG: melexx.mp3" — bio, güncel single'ın reklam panosu olarak
  kullanılıyor ve Instagram'a köprü kuruyor.
- **Ses:** "Originalton – MELEX" (kendi sesi).
- **Yükleme:** 2026-08-19 Çarşamba 10:52 UTC (13:52 TR — öğle molası kuşağı).
  ~1 günde 13.000 izlenme = takipçinin 4,1 katı.
- **Oranlar:** Beğeni %5,1 — çalışmanın en yüksek beğeni oranı. Yorum 35,
  paylaşım 104 (%0,8).

**1b. Kare kare görsel analiz**

- **Hook (ilk 3 sn, #001–#006):** #001'de gün batımı sahil FPV drone planı +
  üstte kalıcı overlay "SUMMER X THIS SONG ☀️ X 🇹🇷" + ekran ortasında büyük KIRMIZI
  kinetik tipografiyle "GÖZLERİNLE" ve altında beyaz Rusça çeviri "Обними".
  Kanca üç katman: yaz estetiği + tür vaadi + iki dilli söz.
- **Tempo:** Çalışmanın en hızlısı: #001–#008 sahil, #009–#022 gün batımı deniz,
  #023–#031 dağ/orman FPV, #032–#037 güneş patlaması, #038–#047 patika koşu
  planı, #048–#060 dağ yamacı + sahil şehri, #061–#065 beyaz villa + marina.
  Ortalama 4–7 saniyede bir plan; her plan içinde FPV hareketi sürekli.
- **Efektler:** Kinetik söz animasyonu (kırmızı dev harfler ekrana yayılıp
  soluyor — #004, #013, #024, #040'ta net), hız bulanıklığı (#051), güneş lens
  parlaması (#029–#034). Kesmeler beat ile senkron.
- **Ekran yazıları:** Kalıcı üst overlay "SUMMER X THIS SONG ☀️ X 🇹🇷" (her karede).
  Sözler TR (kırmızı, büyük) + RU (beyaz, ince) çift katman: "GÖZLERİNLE / Обними"
  (#001), "SAR BENİ / меня взглядом" (#004), "YAVAŞÇA / Медленно" (#009),
  "KALBİM / Когда сердце" (#023), "AÇILINCA / моё раскрывается" (#026), "BÖYLE
  DOKUN DA / Прикоснись ко мне нежно" (#038), "BEN HÂLÂ / Я всё" (#055),
  "BURADA / ещё здесь" (#058).
- **CTA'lar:** Görsel/yazılı abone-beğen CTA'sı YOK. CTA açıklamada: çıkış tarihi
  duyurusu ("28.08.2026 … çıkıyor!") — davranış hedefi takip/bekleme.
- **Görsel kimlik:** Gerçek çekim (drone), sıcak gün batımı + Akdeniz palet;
  576x1026 (düşük çözünürlük — buna rağmen çalışmış). Dikey.
- **Kapak/ilk kare:** #001 güçlü: yaz + kırmızı söz + iki dil aynı anda.

**1c. Sentez — neden izlendi**

1. **Çıkış tarihi kancası:** başlıktaki "28.08.2026 … çıkıyor!" videoyu duyuruya
   çeviriyor; beklenti yaratma %5,0 beğeni oranının ana motoru.
2. **İki dilli söz katmanı (TR+RU):** her karede iki pazara birden konuşuyor —
   Rusça bilen kitle (turist/diaspora) için erişim ikiye katlanıyor.
3. **FPV drone temposu:** 32 sn'de 6+ plan, sürekli hareket; kaydırma refleksine
   fırsat yok.
4. **32 sn süre:** kısa süre = yüksek tamamlanma + döngü (loop) izlenmesi.
5. **Etiket mimarisi:** geniş (afrohouse) + orta (turkish/türkceşarkılar) + niş
   (turkishafrohouse) katmanlı arama niyeti kapsaması.
6. **"SUMMER X THIS SONG" kalıcı overlay'i:** videonun tezini her karede tekrar
   ediyor; ortasından girene de bağlam veriyor.

---

### VIRAL-4 — MELEX, "Ömrüm" fotoğraf/slayt gönderisi

**1a. Metadata analizi**

- **Başlık/açıklama:** Yalnızca etiketler: `#afrohouse #turkish #türk #turkishafrohouse #türkceşarkılar`.
  Sözlü kanca fotoğrafların İÇİNDE ("it's just a song...🇹🇷"). Açıklama boş
  bırakılarak merak tamamen görsele yüklenmiş.
- **Etiketler (5):** viral-3 ile birebir aynı set — kanal düzeyinde tutarlı
  etiket stratejisi.
- **Kanal:** viral-3 ile aynı (@melexx.mp3, 3.189 takipçi). 27.400 izlenme =
  **takipçinin 8,6 katı**; kanalın en çok izlenen içeriklerinden.
- **Yükleme:** 2026-07-08 Çarşamba 17:32 UTC (20:32 TR). 43 günde 27.400 izlenme
  (~652/gün) — yavaş ama **uzun kuyruklu**; fotoğraf gönderileri aramada/beslemede
  uzun yaşıyor.
- **Oranlar:** Beğeni %4,2; yorum 123 (%0,45); **paylaşım 132 (%0,48) — paylaşım
  sayısı yorumdan yüksek**, "sevgiliye gönderilen" içerik profili.
- **Müzik:** "Originalton – MELEX" (kendi şarkısı orijinal ses olarak): sesi
  kullanan her yeni video bu gönderiye trafik döndürüyor.

**1b. Kare kare görsel analiz** (3 fotoğraf; `kareler/foto_1..3.jpg`)

- **Hook (foto_1):** Gece İstanbul — hilal ay + ışıklı Galata Kulesi + önde flu
  pembe çiçekler; ortada beyaz serif yazı: **"it's just a song...🇹🇷"**. Kanca
  ironi/duygu terslemesi: "sadece bir şarkı" deyip tam tersini ima ediyor;
  kaydırınca sözlerin gelacağı vaadi.
- **foto_2:** Sultanahmet/Ayasofya silüeti gün batımı; üstte Türkçe nakarat bloğu:
  "Ömrüm, ömrüm / Sen benim ömrüm / Ömrüm, ömrüm / Kalbimde bir ömür // Ömrüm,
  ömrüm / Beni bende bırakma / Ömrüm, ömrüm / Gel, geceme dokunma ✨".
- **foto_3:** foto_2 ile AYNI görsel, sözlerin Rusça çevirisi: "Моя жизнь, моя
  жизнь / Ты — моя жизнь / … / Приди, не тревожь мою ночь ✨". İki dilli strateji
  burada da (TR slayt + RU slayt).
- **Tempo/efekt:** Slayt formatında kesme yok; kullanıcı kendi hızında kaydırıyor
  — bu, "izlenme süresi"ni kullanıcının merakına bağlıyor. Efekt yok; tek ✨.
- **CTA:** Yok (ne yazılı ne sözlü). Format kendisi CTA: kaydır → oku → sesi aç.
- **Görsel kimlik:** 1260x2240, yüksek kalite gerçek fotoğraflar; İstanbul
  ikonografisi (Galata, Ayasofya) + gün batımı paleti. Türkiye kimliği görselin
  kendisinde.
- **Kapak:** foto_1 kapak olarak kusursuz: az yazı, yüksek estetik, bayrak emojisi.

**1c. Sentez — neden izlendi**

1. **"it's just a song..." tersleme kancası:** İngilizce yazılmış (global kitle),
   duygusal merak açıyor; kaydırma davranışını tetikliyor (slaytta kaydırma =
   etkileşim sinyali).
2. **Söz kartpostalı formatı:** foto_2/3 ekran görüntüsü alınıp story'de
   paylaşılacak şekilde tasarlanmış — 132 paylaşım bunun kanıtı.
3. **İki dilli slayt (TR + RU):** çeviri ayrı slayta konarak hem iki pazar
   yakalanıyor hem slayt sayısı (gezinme süresi) artıyor.
4. **İstanbul ikonografisi:** Galata + Ayasofya, turist ve gurbetçi kitlede güçlü
   duygusal/estetik tetikleyici.
5. **Orijinal ses döngüsü:** şarkı gönderiye "Originalton – MELEX" olarak bağlı;
   sesi kullanan her video kaynağa geri besliyor — 43 günlük uzun kuyruk.
6. **Fotoğraf formatının maliyeti sıfır:** 2 fotoğraf + 1 yazı; üretim eforu
   dakikalar — yatırım getirisi bakımından çalışmanın en verimli içeriği.

---

### VIRAL-5 — FEROV, "Gizli Gizli" (kıyas için: en zayıf performans)

**1a. Metadata analizi**

- **Başlık/açıklama:** `Gizli Gizli - Ferov OUT NOW🚨🎧 #afrohouse #afrobeats #turkish #russian #newmusic`.
  Kanca "OUT NOW" aciliyeti; ama merak boşluğu yok — her şey söylenmiş.
- **Etiketler (5):** afrohouse, afrobeats (geniş), turkish, russian (orta),
  newmusic (geniş-jenerik). "russian" etiketiyle iki pazar hedefi burada da var.
- **Kanal:** @ferov.music — 3.750 takipçi, **203 video**, toplam 51,2k beğeni;
  Almanya'dan (DE). Video başına ortalama beğenisi (~252) üç kanalın en düşüğü:
  çok üretip az isabet alan profil. İmza: "FEROV 🌙 / Afro House Producer /
  Ferov – Gizli Gizli 🎧 OUT NOW".
- **Ses:** "Originalton – FEROV" (kendi sesi).
- **Yükleme:** 2026-08-02 **Pazar 06:37 UTC (09:37 TR sabahı)** — düşük trafik
  kuşağı. 18 günde 3.703 izlenme (~206/gün, takipçinin 1,0 katı): çalışmanın
  en yavaşı.
- **Oranlar:** Beğeni %4,8 (yüksek!) ama yorum yalnız 7, paylaşım 24 (%0,6).
  İçerik beğenilmiş fakat konuşturmamış/gönderilmemiş; dağıtım ivmesi hiç
  oluşmamış.

**1b. Kare kare görsel analiz**

- **Hook (ilk 3 sn, #001–#006):** Ekranda **sahte Spotify oynatıcı arayüzü**
  ("Lieblingssongs" çalma listesi, kapak, "Gizli Gizli – Ferov", yeşil onay
  rozeti, ilerleme çubuğu, oynat/duraklat) + arkada dikey üçlü kolaj (gün batımı,
  kulaklıklı kadın, Galata gecesi). #001–#002'de çubuk 0:42'de duruyor, #003'te
  0:00'a atlıyor (şarkı "başlıyor") — akıllı bir "şimdi çalıyor" illüzyonu.
  Üstte kalıcı: "Turkish x Russian x Afrohouse OUT NOW 🇹🇷🇷🇺❤️‍🔥🥁".
- **Tempo:** Arka plan klipleri çok hızlı dönüyor (1–2 sn'de bir: DJ kontrolcüsü
  eli #006, İstanbul gece #003, yat/marina #008, kulaklıklı kadın #011…) ama
  ekranın ~%40'ını kaplayan oynatıcı UI'si sabit — algılanan tempo düşüyor.
- **Efektler:** #033'ten itibaren yoğun glitch/kromatik sapma (#035–#043 çok
  belirgin), renk şeritli dikey kolaj, ilerleme çubuğu gerçek zamanlı ilerliyor
  (0:42→1:01+). Beat-senkron kesmeler.
- **Ekran yazıları:** Kalıcı iki satır: "Turkish x Russian x Afrohouse / OUT NOW
  🇹🇷🇷🇺❤️‍🔥🥁". **Şarkı sözü katmanı YOK** — bu, ilk dört videoyla en kritik fark.
- **CTA'lar:** Dolaylı: yeşil onay rozeti "kaydet/beğen" çağrışımı; açıklamada
  "OUT NOW". Açık takip/kaydet çağrısı yok.
- **Görsel kimlik:** Neon mor/pembe + gece İstanbul; 720x1376. Estetik tutarlı
  ama anonim — sanatçı yüzü/kimliği yok.
- **Kapak/ilk kare:** #001 "Spotify ekran görüntüsü" gibi; beslemede şarkı
  önerisi sanılıp durdurabiliyor — ilginç ama yanıltıcı olduğu için etkileşim
  kalitesi düşük.

**1c. Sentez — neden (nispeten az) izlendi ve yine de ne öğretiyor**

1. **Söz katmanı yokluğu:** izleyiciyi tutan okuma davranışı yok; beğeni oranı
   yüksek ama izlenme süresi sinyali zayıf → dağıtım büyümemiş.
2. **Pazar sabahı yüklemesi (Pazar 09:37 TR):** ilk saat ivmesi ölü kuşakta
   harcanmış.
3. **Sahte-UI hook'u çift taraflı:** durduruyor (+) ama içerik vaadi vermiyor (−);
   yorum yalnız 7.
4. **"OUT NOW" merak bırakmıyor:** viral-3'ün "28.08'de çıkıyor" beklenti kancası
   burada yok; aciliyet var, hikâye yok.
5. **Yine de %4,8 beğeni:** estetik/kalite yeterli; sorun içerik mimarisi ve
   zamanlama. Ders: aynı prodüksiyon kalitesi, söz + doğru saat + merak kancası
   olmadan taşımıyor.

---

## 1B. İKİNCİ PARTİ (2. tur, kullanıcı 4 URL daha verdi)

**Analiz zamanı:** 2026-08-20 ~09:30 UTC.

### Özet tablo — 2. parti

| | viral-6 | viral-7 | viral-8 | viral-9 |
|---|---|---|---|---|
| Sanatçı/kanal | @kozat26 | Ayşe Çetin (@aysecetinofficiall) | retrobesto (@retrobesto) | TAYFUN X (@tayfunyenidunya) |
| Kanal takipçi / video | erişilemedi | 4.447 / 29 | 1.451 / 16 | 5.016 / 97 |
| Ülke | — | 🇹🇷 TR | 🇹🇷 TR | 🇹🇷 TR |
| Şarkı / içerik | erişilemedi | Sana Emanet (tam AI klip) | Katalog derlemesi (11 şarkı) | Kaldım (AI düet klip) |
| Süre | — | 298 sn (5 dk!) | 124 sn | 222 sn |
| Yükleme (UTC) | — | 16.08 Pazar 21:49 (Pzt 00:49 TR) | 05.08 Çarş. 15:05 (18:05 TR) | 17.08 Pzt 13:13 (16:13 TR) |
| İzlenme | — | **396.400** | 43.600 | 7.451 |
| İzlenme/takipçi | — | **89×** | 30× | 1,5× |
| Günlük ort. izlenme | — | **~99.100 (4 gün)** | ~2.900 (15 gün) | ~2.480 (3 gün) |
| Beğeni (oran) | — | 2.206 (**%0,56!**) | 1.072 (%2,5) | 854 (**%11,5!**) |
| Yorum / Paylaşım | — | 132 / 429 | 7 / 25 | 73 / 117 |
| Etiket | — | 5 (açıklama içinde) | 5 | 5 |

### VIRAL-6 — @kozat26 (7675415130695339277)

**Uygulanamadı — nedeni:** Gönderi TikTok tarafından "bazı izleyiciler için
uygun olmayabilir" (hassas içerik) etiketiyle **giriş duvarının arkasına**
alınmış. yt-dlp, embed API, oEmbed ve mobil sayfa — dördü de anonim erişimde
boş/kilitli dönüyor; oturum çerezi olmadan videoya, metadata'sına ve karelerine
ulaşmak mümkün değil. Analiz istenirse: (a) videonun ekran kaydı/dosyası bana
verilebilir, ya da (b) gönderinin hangi video olduğu söylenirse açık bir
kopyası üzerinden analiz yapılır. Not: hassas içerik etiketi yiyen gönderiler
keşfet dağıtımından büyük ölçüde düşer — HASANCA stratejisi için ders: kapak ve
ilk karede bu etiketi tetikleyebilecek görsellerden (aşırı ten, şiddet imgesi,
sigara/alkol yakın planı) kaçınılmalı.

### VIRAL-7 — Ayşe Çetin, "Sana Emanet" (396k izlenme — 2. turun devi)

**1a. Metadata analizi**

- **Başlık/açıklama (tam metin):** "✨🖤 BUGÜN YAYINDA! 🖤✨ 🎶 Yeni şarkım 'Sana
  Emanet' 🎬 Klibiyle birlikte bugün sizlerle! Benden sonra size emanet… 🖤
  TikTok keşfette beni öne çıkarttı, şimdi sıra sizde! 🔥 Dinle, izle, paylaş…
  Duyguma ortak ol. 🎶 🎧 Spotify • YouTube Müzik • Fizy • Apple Music
  #SanaEmanet #AyşeÇetin #BugünYayında #YeniŞarkı #YeniKlip".
  Ders kitabı gibi bir açıklama: (1) aciliyet ("BUGÜN YAYINDA"), (2) duygusal
  kanca ("Benden sonra size emanet…" — şarkı adıyla kelime oyunu), (3) sosyal
  kanıt + görev verme ("TikTok keşfette beni öne çıkarttı, şimdi sıra sizde!"),
  (4) üçlü eylem CTA'sı ("Dinle, izle, paylaş"), (5) platform listesi,
  (6) 5 etiket: 2 marka (#SanaEmanet #AyşeÇetin) + 3 arama (#BugünYayında
  #YeniŞarkı #YeniKlip). Tamamı Türkçe — hedef yerli pazar.
- **Kanal:** 4.447 takipçi, yalnız 29 video, 64,3k toplam beğeni. **396.400
  izlenme = takipçinin 89 katı.** İmza: "AYSECETIN OFFICIAL / eternal sound
  music / Yeni şarkılar için takipte kalın" (plak şirketi + takip CTA'sı).
- **Yükleme:** 2026-08-16 Pazar 21:49 UTC = **Pazartesi 00:49 TR (gece
  yarısı!)** — "BUGÜN yayında" ifadesiyle tutarlı: gün dönümünde yayın, tüm
  Pazartesi'yi ilk-24-saat penceresi yapıyor. 4 günde 396.400 (~99.100/gün).
- **Oranlar — kritik bulgu:** Beğeni **%0,56** (bu çalışmadaki en düşük!),
  yorum %0,03, paylaşım %0,11. İzlenme devasa ama etkileşim oranı çok cılız.
  Bu imza tipik olarak **ücretli tanıtımın (TikTok Promote/reklam)** izidir:
  geniş ama pasif kitleye zorla gösterim. "TikTok keşfette beni öne çıkarttı"
  cümlesi de buna işaret ediyor olabilir. Yani 396k'nın anlamlı bir kısmı
  muhtemelen satın alınmış erişim — kalıbı kopyalarken bunu bilerek kopyalamalı.

**1b. Kare kare görsel analiz**

- **Format:** YATAY (16:9) sinematik, tamamı yapay zekâ ile üretilmiş 5
  dakikalık anlatılı klip. TikTok'ta dikey doldurmuyor — buna rağmen izlenmiş.
- **Hook (ilk 3 sn, #001–#006):** Fırtınalı gökyüzü, siyah kumlu sahilde
  beyaz elbiseli kadın + siyah giyimli adam; ekranda gümüş işlemeli, mücevher
  gibi "Sana Emanet" logosu (#001–#010 boyunca kalır). Sinema afişi açılışı.
- **Sahne akışı (tempo ~4–8 sn/plan):** sahil çifti (#001–#020) → tren vagonu
  kadın (#021–#040) → Boğaz köprüsü + cami silüeti önünde adam (#041–#060) →
  kırık cep saati makro (#061–#068) → masada viski + tek lamba (#069–#074,
  #086–#096) → ağlayan kadın makro (#075–#085) → yeşil kazak/yağmurlu pencere
  (#121–#131) → masada yüzleşme sahnesi (#132–#142) → neon sokak (#143–#171) →
  yağmurlu cam bokeh (#172–#188) → bozkırda gelinlik/bordo elbise (#189–#258) →
  sahil evi kapısı (#259–#264) → sonbahar yaprağı düşüşü (#313–#325) → ormanda
  ağlayan adam (#326–#336+) → mektup yazma/okuma (#409–#432) → mezarlık +
  **alyansını çıkarıp mezar taşına bırakma** (#505–#525) → fırtınalı gökte
  kadın portresi (#526–#528) → uçurumda vedalaşma (#577–#591) → siyaha kararma
  (#592–#597, 4:55–4:58).
- **Hikâye:** kayıp/yas anlatısı — "Benden sonra size emanet" başlığıyla klip
  birebir örtüşüyor; izleyiciye çözülecek bir hikâye veriyor (yorumlarda "kim
  öldü?" tartışması etkileşim üretir).
- **Efektler/kusurlar:** film grenli, pastel sinematik renk; AI kusurları
  görünür durumda (#518'de eriyen eller, #582'de bozulan yüz) — 396k izlenmeye
  engel olmamış.
- **Ekran yazıları:** YOK (başlık logosu hariç). Söz katmanı YOK. CTA YOK.
  Tüm metin yükü açıklamada.
- **Kapak/ilk kare:** #001 gerçek bir film afişi gibi; başlık logosu net.

**1c. Sentez — neden izlendi**

1. **Muhtemel ücretli itki + organik uyum:** %0,56 beğeni oranı erişimin
   satın alınmış olabileceğini söylüyor; ama içerik "reklam gibi" değil film
   gibi olduğundan izleyici kaçmamış.
2. **"BUGÜN YAYINDA" lansman kurgusu:** gece 00:49'da yükleme + aciliyet dili
   ilk 24 saati maksimize ediyor.
3. **Anlatılı 5 dk klip:** kayıp hikâyesi merak döngüsü kuruyor; uzun süre =
   toplam izlenme dakikası sinyali yüksek.
4. **Açıklamadaki görev verme dili:** "TikTok keşfette beni öne çıkarttı,
   şimdi sıra sizde! Dinle, izle, paylaş" — izleyiciye rol veriyor; 429
   paylaşımın motoru.
5. **Sinema kalitesinde AI prodüksiyon:** tek kişilik bütçeyle "plak şirketi
   klibi" algısı; kusurlar (eriyen el) umursanmıyor.
6. **Ders (ters yönde):** başlık kartı dışında overlay/söz/CTA yok; %0,56
   beğeni bunun da faturası. HASANCA kopyasında söz katmanı eklenmeli.

### VIRAL-8 — retrobesto, katalog derlemesi (43,6k izlenme)

**1a. Metadata analizi**

- **Başlık/açıklama (tam):** "Retrobesto - Şu ana kadar dijital platformlarda
  yayınladığımız şarkıların kısa bir derlemesini yaptık sizler için.. Retro
  ruhlu pop şarkıları arasından sizde kendinize uygun olanı bulacaksınız..
  Daha yeni başlıyoruz yayınlanacak çok şarkımız var sırada bekleyen..😊
  Takipte kalın #retromusic #şarkı #aimusic #vintage #retro". Samimi/mütevazı
  ton + "kendinize uygun olanı bulacaksınız" (kişiselleştirme vaadi) +
  "takipte kalın" CTA. Etiketler: retro kimliği (retromusic/vintage/retro) +
  genel (şarkı) + **#aimusic — yapay zekâ olduğunu gizlemiyor.**
- **Kanal:** 1.451 takipçi (çalışmanın en küçüğü), 16 video, imza: "Retro
  ruhlu yapay zeka müzik projesi. Dünün melodileri, bugünün sözleri." —
  **açık AI-müzik markası.** 43.600 izlenme = takipçinin 30 katı.
- **Yükleme:** 2026-08-05 Çarşamba 15:05 UTC (18:05 TR — akşam kuşağı).
  15 günde 43,6k (~2.900/gün) — istikrarlı uzun kuyruk.
- **Oranlar:** Beğeni %2,5; yorum yalnız 7, paylaşım 25. Dinletmiş ama
  konuşturmamış: derleme formatı tek şarkılık duygusal bağ kurmuyor.

**1b. Kare kare görsel analiz**

- **Format:** 124 sn; **11 şarkının "AI albüm kapağı afişi"** art arda, her
  kapak ~10–11 sn ekranda, aralarda VHS/glitch geçişi (ör. #021–#022,
  #065–#066, #131–#132). Kapak başına şarkının en vurucu ~10 saniyesi çalıyor.
- **Görülen kapaklar:** "Ahım Tutarsa" (sepya sokak, klasik araba, bavul,
  #001–#021) → "Kâfi" (karanlık şato + zırhlı figür, #022–#048) → "Temmuz"
  (retro yaz afişi: palmiye, kabriyole, gün batımı, #049–#065) → "Tik Tak"
  (kum saati + disko topu + synth, #066–#120) → "Acılarım Yakışıklı" (sahilde
  aynaya bakan adam, #121–#131) → "Sevda Köprüsü" (halat örgülü köprü +
  minibüs, #132–#168) → … → "Konsantrasyon" (retrowave kadın, #241) →
  **marka kapanışı (#242–#248):** RETROBESTO plak logosu + "TÜM DİJİTAL
  PLATFORMLARDA" + Spotify/Apple/YT/TikTok/IG ikonları + @retrobesto.
- **Hook (ilk 3 sn):** "Ahım Tutarsa" afişi + şarkının nakaratı — ama tek
  statik afiş 10 sn kaldığı için hook gücü orta; derlemenin asıl tutma
  mekanizması "sıradaki şarkı ne?" merakı.
- **Ekran yazıları:** her afişte şarkı adı büyük retro tipografiyle (başka söz
  katmanı yok). **CTA:** video sonunda görsel marka kartı (#242–#248) +
  açıklamada "takipte kalın".
- **Görsel kimlik:** tutarlı retro afiş estetiği; her kapak farklı renk
  dünyası ama aynı el yazısı tipografi ailesi — güçlü marka dili.

**1c. Sentez — neden izlendi**

1. **"Menü" formatı:** 11 şarkı = 11 ayrı kanca; bir şarkı tutmazsa izleyici
   bir sonrakini bekliyor, kaydırmıyor — tamamlanma yerine "uzun izlenme
   süresi" üretiyor.
2. **AI'yi saklamayıp marka yapmak:** "yapay zekâ müzik projesi" + #aimusic
   merak/tartışma çekiyor (1.451 takipçiyle 43,6k izlenme).
3. **Afiş estetiği:** her kare ekran görüntüsü alınabilir kalitede; şarkı
   adları (Ahım Tutarsa, Acılarım Yakışıklı) tek başına merak uyandıran
   kelime oyunları.
4. **Akşam 18:05 TR yüklemesi** — doğru kuşak.
5. **Zayıf noktası:** yorum 7 — derlemede kimse "hangi şarkı?" diye sormuyor
   çünkü adlar ekranda; etkileşim sorusu yok. HASANCA versiyonunda her afişe
   "hangisi favorin? yorumlara yaz" eklenmeli.

### VIRAL-9 — TAYFUN X & AMİRA, "Kaldım" (7,4k izlenme ama %11,5 beğeni!)

**1a. Metadata analizi**

- **Başlık/açıklama (tam):** "KALDIM TAYFUN X - TAYFUN YENİDÜNYA Yeni klip ve
  şarkımız yayında İZLEYİP DİNLEDİĞİNİZ MÜZİĞİN SÖZ - MÜZİK - BESTE YAPAY ZEKA
  DESTEĞİ OLMADAN TARAFIMIZCA YAPILMIŞTIR VİDEO PRODÜKSİYON YAPAY ZEKA DESTEĞİ
  İLE TARAFIMIZCA YAPILMIŞTIR + Instagram/YouTube/Facebook linkleri + #damar
  #müzik #tayfunx #yapayzekamüzik #keşfet". Dikkat: **şeffaflık beyanı**
  (müzik insan yapımı, görüntü AI) — güven inşası; ama açıklama düz büyük
  harf blok hâlinde, link yığınıyla okunması zor. Etiketlerde #damar (tür,
  arabesk kitlesi) + #yapayzekamüzik + #keşfet.
- **Kanal:** 5.016 takipçi, 97 video, 57,5k beğeni. İmza: "ŞARKILARIN TAMAMI
  YOUTUBE İZLEYEBİLİRSİNİZ". 3 günde 7.451 izlenme (~2.480/gün, takipçinin
  1,5 katı) — keşfete düşmemiş.
- **Yükleme:** 2026-08-17 Pazartesi 13:13 UTC (16:13 TR).
- **Oranlar — kritik bulgu:** Beğeni **%11,5** (çalışmanın AÇIK ARA en
  yükseği; viral-7'nin 20 katı), yorum %0,98, paylaşım %1,6. İçerik kendi
  kitlesini derinden vurmuş ama dağıtım küçük kalmış: klasik "sadık çekirdek
  kitle + zayıf keşfet" profili.

**1b. Kare kare görsel analiz**

- **Format:** dikey 222 sn AI düet klibi.
- **Hook (ilk 3 sn, #001–#006):** "KALDIM — TAYFUN X & AMİRA" altın serif
  logolu afiş: gece Boğaz köprüsü + Kız Kulesi önünde AI çift; altta turkuaz
  "TAYFUN X PRODUCTION" bandı yazı animasyonuyla doluyor. Güçlü, profesyonel
  açılış kartı (#001–#016 sabit kalıyor — 8 sn, biraz uzun).
- **Sahne akışı:** afiş (#001–#016) → rıhtımda kırmızı pantolonlu kadın +
  kruvaziyer gemi (#017–#100) → güvertede kadın (#097–#116) → rıhtımda ateş
  varilleri önünde söyleyen adam (#103–#226) → helikopter pisti sahnesi
  (#217–#219) → panel-flip geçişler (#105–#111, #227, #233) → final:
  "KALDIM" afişine dönüş (#439–#445).
- **Ekran yazıları / CTA'lar (sürekli rotasyonda!):** "TAYFUN X PRODUCTION"
  (açılış), "SÖZ - MÜZİK - BESTE / TAYFUN YENİDÜNYA" (#021–#024, #433–#437),
  "TÜM MÜZİK MARKETLERDE" + **platform ikon şeridi (YouTube/IG/FB/Spotify/
  Apple)** (#109–#120 ve tekrarları). Söz (lyric) katmanı YOK — yazılar hep
  künye/CTA. Video boyunca 5+ kez künye dönüyor: tanıtım ağırlıklı yazı
  stratejisi.
- **Görsel kimlik:** gece İstanbul + kruvaziyer lüksü + ateş varilleri;
  altın/lacivert palet; AI karakter tutarlılığı iyi, geçişlerde hızlı
  bulanıklık (#227, #233).
- **Kapak/ilk kare:** #001 kusursuz single afişi.

**1c. Sentez — neden bu profilde**

1. **%11,5 beğeni + %1,6 paylaşım:** damar/arabesk çekirdek kitle içeriği
   sevmiş — şarkı-kitle uyumu kanıtlı. Sorun içerik değil dağıtım.
2. **222 sn dikey klip, ilk 8 sn statik afiş:** hook yavaş; keşfet
   izleyicisini ilk 2 saniyede yakalayamıyor (viral-2'nin aksine ilk karede
   duygu cümlesi yok).
3. **Söz katmanı yok, künye çok:** izleyiciyi tutan okuma malzemesi yerine
   5 kez tekrarlanan production/platform yazıları — izlenme süresi sinyali
   zayıf kalıyor.
4. **Şeffaflık beyanı güven veriyor** (yorum oranı %0,98 — viral-7'nin 30
   katı) ama açıklama metni SEO'suz düz blok.
5. **Ders:** HASANCA için — güçlü çekirdek etkileşimli içerik + viral-2 tarzı
   söz katmanı + hızlı hook birleştirilirse iki dünyanın iyisi alınır.

### 2. parti — güncellenmiş ana çıkarımlar

1. **Beğeni oranı ile izlenme ters düşebilir:** viral-7 (396k, %0,56) muhtemel
   ücretli erişim; viral-9 (7,4k, %11,5) organik çekirdek sevgisi. Sağlıklı
   hedef: viral-2/3 bandı (%3–5 beğeni + yüksek paylaşım + yüksek izlenme).
2. **Lansman kurgusu işliyor:** "BUGÜN YAYINDA" + gece yarısı yükleme
   (viral-7) ve "28.08'de çıkıyor" (viral-3) — ikisi de tarih/aciliyet
   kancası. HASANCA yeni parça yayınlarında aynı kurgu kullanılmalı.
3. **AI şeffaflığı iki yönde de çalışıyor:** retrobesto (#aimusic, bio'da
   açık) ve TAYFUN X (uzun beyan) — ikisi de cezalandırılmamış; aksine merak
   ve güven üretiyor. HASANCA AI görsel kullanıyorsa gizlemek gerekmiyor.
4. **Derleme/menü formatı** (viral-8) küçük hesap için ucuz ve etkili keşif
   aracı: HASANCA'nın 30+ parçası "10 saniyede 10 şarkı — hangisi favorin?"
   videosuna dönüştürülebilir.
5. **Hassas içerik duvarı** (viral-6) dağıtımı öldürür: kapak/ilk kare
   seçiminde moderasyon tetikleyicilerinden kaçın.

---

## 1C. ÜÇÜNCÜ PARTİ (3. tur, 9 URL — kontrol grubu niteliğinde)

**Analiz zamanı:** 2026-08-20 ~10:30 UTC. Bu parti özellikle değerli çünkü
**aynı kanalların tutan VE tutmayan videolarını** içeriyor (MELEX, FEROV) —
neyin işe yaradığını artık kanal içi karşılaştırmayla da doğrulayabiliyoruz.

### Özet tablo — 3. parti

| | viral-10 | viral-11 | viral-12 | viral-13 | viral-14 | viral-15 | viral-16 | viral-17 | viral-18 |
|---|---|---|---|---|---|---|---|---|---|
| Kanal | Natali 🇹🇷 (@natalishenderyk74) | MELEX | AmandaAzoitei | FEROV | Alphaox (@alphaoxmusic) | Defiant (@defiantresmi) | Solyra (@solyra_music) | mccly57 | ISTANBUL SOUNDS by ILHAN |
| Takipçi / video | 13,8k / 563 | 3,2k / 100 | **911,8k** / 1512 | 3,75k / 203 | 22k / 385 | 11,1k / 63 | 3,65k / 257 | 10,5k / 73 | 8,9k / 52 |
| Ülke | TR | DE | IT | DE | CH | TR | BR | AT | DE |
| İçerik | Gece Alanya sahili araç çekimi + TR/RU söz — **MELEX'in sesiyle hayran videosu** | Karanlık kulüp kalabalığı + karaoke söz (GEL teaser) | Sokakta selfie-kol dans yürüyüşü (Milano) | Bulanık jet-ski POV + renkli kelime animasyonu (teaser) | Festival DJ kabini + kalabalık ("Jambo Merhaba") | 17 sn statik S/B kapak (Mühürlendi Kader) | Gece otoyol + neon söz ("Kıymetimi Bilmedin") | Kulüp DJ seti (Afrodise) "Summerhit🔥🎧" | Türkiye gezi montajı + sabit marka overlay |
| Süre | 32 sn | 23 sn | 15 sn | 30 sn | 47 sn | 17 sn | 42 sn | 59 sn | 100 sn |
| Yükleme (UTC) | 16.08 Pazar 18:19 | 19.08 Çarş. 17:00 | 19.08 Çarş. 15:48 | 06.08 Perş. 19:04 | 28.06 Pazar 13:55 | 09.08 Pazar 18:38 | 16.08 Pazar 19:12 | 02.07 Perş. 08:16 | 09.08 Pazar 14:46 |
| İzlenme | **130.300** | 2.228 | 75.100 | 844 | 72.200 | 4.466 | 4.012 | 11.500 | 13.500 |
| İzlenme/takipçi | **9,4×** | 0,7× | 0,08× | 0,2× | 3,3× | 0,4× | 1,1× | 1,1× | 1,5× |
| Beğeni (oran) | 5.137 (%3,9) | 104 (%4,7) | 5.331 (%7,1) | 43 (%5,1) | 3.218 (%4,5) | 256 (%5,7) | 225 (%5,6) | 447 (%3,9) | 581 (%4,3) |
| Yorum / Paylaşım | 96 / **1.179** | 20 / 14 | 120 / 122 | 1 / 4 | 90 / **490** | 10 / 14 | 16 / 18 | 12 / 75 | 25 / 106 |
| Etiketler | турция, алания, песня, türkiye, şarkı | afrohouse seti | YOK | afrohouse seti | afrohouse, turkey, african, music, viral | YOK | keşfetteyizzz, akım, şarkısözleri, newsong, türkçeşarkı | türkiye, keşfetteyizzz, latin, afrohouse, clubmix | açıklamada 10+ etiket yığını |

### VIRAL-10 — Natali, MELEX sesiyle hayran videosu (partinin kazananı: 130k)

- **1a:** Başlık SADECE 5 etiket: `#турция #алания #песня #türkiye #şarkı` —
  3'ü Rusça (Türkiye, Alanya, şarkı), 2'si Türkçe. Kanal: Alanya'da yaşayan
  Rus içerik üreticisi (13,8k takipçi, 563 video — günlük vlog hacmi). Ses:
  **"Originalton – MELEX"** — viral-3'te analiz ettiğimiz "Gözlerinle Sar
  Beni". Pazar 21:19 TR'de yüklenmiş. 4 günde 130k izlenme (takipçinin 9,4
  katı), **1.179 paylaşım** (%0,9).
- **1b:** Prodüksiyon değeri SIFIR: gece Alanya sahil yolunda seyir hâlindeki
  araçtan telefonla çekilmiş tek plan (65 kare boyunca aynı). Üstünde TikTok'un
  yerel (native) beyaz yazısıyla iki katman: TR söz + RU çevirisi ("Gözlerinle
  sar beni / Обними меня своим взглядом" → "Yavaşça / Медленно" → "Kalbim
  açılınca / Когда моё сердце откроется" → "Ben hâlâ burada / Я всё ещё
  здесь"). CTA yok, efekt yok, kapak özensiz.
- **1c — neden patladı:** (1) MELEX'in sesi + Alanya gecesi + RU çeviri =
  Türkiye'deki/tatildeki Rusça konuşan kitleye nokta atışı; (2) "yaşanmışlık"
  estetiği — araba camından şehir ışıkları, şarkı sözleriyle duygusal anlam
  kazanıyor (paylaşımların motoru); (3) yerel etiketler (алания) şehir bazlı
  arama trafiği. **HASANCA için partinin en önemli dersi:** şarkının kendisi
  değil, şarkıyla kurulan SAHNE viral oluyor; orijinal ses döngüsü üçüncü
  kişilerin videolarıyla asıl patlamayı yapıyor.

### VIRAL-11 & VIRAL-13 — Aynı kanalların TUTMAYAN videoları (MELEX 2,2k; FEROV 844)

- **viral-11 (MELEX "GEL" teaser):** Aynı kanal viral-3'te 13k almıştı; bu
  video 2,2k'da kaldı. Farklar: (1) görüntü **karanlık** kırmızı kulüp
  kalabalığı — viral-3'ün parlak gün batımı FPV'sinin tersi; (2) **Rusça
  çeviri katmanı YOK** (sadece "gel / gel bana gel / kalbim sende"); (3) söz
  tekrarı monoton, plan tek mekân; (4) Çarşamba 20:00 TR yüklemesi iyi ama
  içerik zayıf. Beğeni oranı %4,7 — görenler sevmiş, dağıtım büyütmemiş
  (izlenme süresi sinyali düşük).
- **viral-13 (FEROV "14.08.26" teaser):** 844 izlenme — tüm çalışmanın dibi.
  Bulanık, düşük çözünürlüklü jet-ski POV tek planı; renkli kelime animasyonu
  ("LAN HADI SÖYLE…") çabası var ama zemin görüntü kalitesiz; yüz yok, sahne
  değişimi yok. Perşembe 22:04 TR. Ders: kinetik yazı, kalitesiz görüntüyü
  kurtarmıyor.
- **Kanal içi A/B sonucu:** Parlak + iki dilli + tarihli duyuru (viral-3) ≈
  6× / 15× fark yaratıyor (aynı kanal, aynı tür, aynı hafta bandı).

### VIRAL-12 — AmandaAzoitei (911,8k takipçili dansçı: 75k izlenme = 0,08×)

- **1a:** Açıklama ve etiket TAMAMEN BOŞ. Müzik: "Without You – Mattilo"
  (muhtemel ücretli şarkı işbirliği; bio'da "song collabs" e-postası var).
  Çarşamba 18:48 TR.
- **1b:** 15 sn tek plan: Milano'da uzatılmış kolla selfie çekimi "dans
  yürüyüşü"; yazı katmanı yok; enerji yüksek, yüz kameraya yakın.
- **1c:** %7,1 beğeni (kitlesi sadık) ama izlenme, takipçi sayısının onda
  birinden az. **Ders:** 911k takipçili hesaba şarkı yerleştirmek bile
  garantili erişim satın almıyor; şarkı arka fon olduğunda dönüşüm yok. Küçük
  hesabın doğru içeriği (viral-10) influencer yerleştirmesini 2'ye katlıyor.

### VIRAL-14 — Alphaox "Jambo Merhaba" (72k; İngilizce sosyal kanıt formatı)

- **1a:** Başlık İngilizce konumlandırma cümlesi: "Turkish melodies 🇹🇷 +
  African rhythms 🌍 + Afrohouse 🔥" + 5 etiket (afrohouse, turkey, african,
  music, viral). İsviçre merkezli, 22k takipçi. Pazar 16:55 TR. 53 günde 72k
  (uzun kuyruk), **490 paylaşım**.
- **1b:** Festival ana sahne DJ kabini arkasından çekim; on binlerce kişilik
  kalabalık; kırmızı/pembe filtre; iki sabit overlay: üstte "This Turkish
  African Afrohouse drop is so good" (izleyici ağzından yazılmış!), ortada
  "JAMBO MERHABA" şarkı adı. Kalabalık coşkusu = canlı sosyal kanıt.
- **1c:** (1) Overlay'i sanatçı değil sanki bir izleyici yazmış gibi kurmak
  ("This … is so good") üçüncü şahıs onayı hissi veriyor; (2) dev kalabalık
  görüntüsü şarkıya "zaten hit" algısı yüklüyor; (3) İngilizce + türk-afro
  füzyon konumlandırması global keşfete oynuyor. HASANCA'da canlı sahne/konser
  arşiv görüntüsü varsa bu format birebir uygulanabilir.

### VIRAL-15 & VIRAL-16 — Orta sahanın dersleri (4,5k / 4k)

- **viral-15 (Defiant):** 17 sn boyunca TEK statik siyah-beyaz kapak
  görseli ("MÜHÜRLENDİ KADER"); söz katmanı yok, hareket yok. Açıklama
  duygu sömürüsüne yaslanıyor: "bu şarkıya çok çalıştık, desteği de
  hakediyoruz bence. gösterin gücünüzü🌹" — etiket YOK. %5,7 beğeni ama 4,5k
  izlenmede kalmış. Ders: (1) yalvaran CTA dağıtım getirmiyor; (2) statik
  görsel + söz katmanı yokluğu = izlenme süresi sinyali yok; (3) etiketsiz
  açıklama arama trafiğini bırakıyor. (Kanal 11,1k takipçili — izlenme 0,4×.)
- **viral-16 (Solyra):** Gece otoyol görüntüsü + neon parlamalı söz overlay'i
  ("KIYMETİMİ BİLMEDİN") — görsel fikir iyi, ama 42 sn boyunca tek satır söz
  dönüyor ve etiketler spam kokusu veriyor (#keşfetteyizzz #akım). Brezilya
  lokasyonlu hesap Türkçe içerik atıyor (coğrafi sinyal karışık). 4k izlenme.
  Ders: #keşfetteyizzz/#akım tarzı hile etiketleri işe yaramıyor; tek söz
  satırının 42 sn dönmesi yeterli okuma malzemesi değil.

### VIRAL-17 & VIRAL-18 — Orta-üst saha (11,5k / 13,5k)

- **viral-17 (mccly57 "Bulutların İçinde"):** Kulüp DJ seti (Afrodise
  gecesi), mum ışıkları, kadın DJ, kalabalık; tek overlay "Summerhit🔥🎧".
  59 sn. %3,9 beğeni, 75 paylaşım. Gerçek etkinlik görüntüsü güven veriyor
  ama karanlık sahneler (viral-11 ile aynı sorun) ve tek kelimelik overlay
  sınırlıyor. Perşembe 11:16 TR yüklemesi ölü kuşak.
- **viral-18 (ISTANBUL SOUNDS "tozlu aynalar"):** Türkiye gezi montajı
  (sisli köprü manzarası → şelale → Kapadokya peribacaları → balonlar),
  ~10 sn'de bir sahne; ekran ortasında SABİT blok: "ISTANBUL SOUNDS BY
  ILHAN / TURKISH ANATOLIAN DEEP HOUSE 2026" + dalga formu + logo. Açıklama
  10+ etiketli yığın (deephouse, turkishdeephouse, türkçedeephouse…). Bio:
  "New Drops Daily" — hacim stratejisi. 13,5k izlenme, 106 paylaşım (%0,8).
  Türkiye manzara ikonografisi (Kapadokya!) yine paylaşım getiriyor; ama
  sabit dev overlay görüntüyü kapatıyor ve söz katmanı yok.

### 3. parti — güncellenmiş ana çıkarımlar (strateji için kritik)

1. **Orijinal ses döngüsü kanıtlandı:** MELEX'in sesini kullanan üçüncü kişi
   videosu (viral-10, 130k), MELEX'in kendi en iyi videosunu (13k) 10'a
   katladı. Strateji, "kendi videon patlasın"dan çok **"sesin başkalarının
   videosunda patlasın"** üzerine kurulmalı: sese kolay senaryo (araba camı +
   şehir gecesi + söz) ilham veren içerik üretmek.
2. **Karanlık/bulanık görüntü = ölüm** (viral-11, 13, kısmen 17): aynı
   kanalın parlak videoları 6–15× daha iyi performans veriyor.
3. **İki dilli katman tekrar kazandı** (viral-10 TR+RU 130k; viral-11 tek
   dilli 2,2k).
4. **Takipçi sayısı yanılgısı bir kez daha:** 911k'lık hesap 0,08× yaptı;
   13,8k'lık gurbetçi hesabı 9,4×. İçerik-kitle uyumu her şey.
5. **Yalvaran CTA ve spam etiket çalışmıyor** (viral-15, 16).
6. **Sosyal kanıt overlay'i** ("This … drop is so good", festival kalabalığı)
   güçlü ve HASANCA'ya uyarlanabilir (viral-14, 490 paylaşım).
7. **Yükleme saati örüntüsü korunuyor:** bu partinin kazananları da
   16:00–21:30 TR bandında; tek sabah yüklemesi (viral-17, 11:16 TR)
   ortalamanın altında.

---

## 2. Kullanıcının videolarının analizi (@hasancamuzik — 16 gönderi)

**Analiz zamanı:** 2026-08-20 ~13:00 UTC. Kullanıcı 16 gönderi URL'si verdi;
13'ü tam analiz edildi. **benim-3, benim-4 ve benim-6 fotoğraf (slayt)
gönderileri analiz edilemedi:** TikTok bu üç gönderiyi anonim erişime hiç
açmıyor (yt-dlp, embed API, oEmbed, mobil sayfa — tümü giriş duvarı/boş
dönüyor). Ekran görüntüleri + uygulama içi istatistikleri verilirse aynı
derinlikte analiz eklenecektir.

### Kanal profili

- **@hasancamuzik** — "🎶✦Hasanca✦🎶": 1.285 takipçi, **242 video**, 32.300
  toplam beğeni. İmza: "🎵 Hasanca | Şarkıcı & Söz Yazarı / 🎧 Ay Ay Ay •
  Emanet • Fena Alıştım Sana / Tüm şarkılarıma ve müzik platformlarına
  buradan ulaşabilirsiniz.👇" (iyi kurgulanmış bio; viral referans
  kalıbıyla uyumlu).
- **Konum sinyali: SE (İsveç).** Tüm gönderiler İsveç'ten atılmış görünüyor;
  içerik dili Türkçe. (Aşağıda teşhiste ele alınıyor.)
- **Ses stratejisi:** her gönderi "orijinal ses – Hasanca"; benim-14 doğru
  biçimde adlandırılmış müzik kullanıyor ("Fena Alıştım Sana - HasanCa") —
  bu, ses döngüsü için doğru yöntem.

### Özet tablo — kullanıcının 13 analiz edilebilen gönderisi

| # | İçerik | Süre | Yükleme (UTC) | İzlenme | Beğeni (oran) | Yorum/Paylaşım | Not |
|---|---|---|---|---|---|---|---|
| benim-1 | "EX'den mesaj var! Kabul/Ret" anketi (AI telefon + stüdyo) | 11 sn | 19.08 Çarş. 12:54 | 291 | 5 (%1,7) | 2 / 2 | letterbox'lu |
| benim-2 | "Şeytan mıydı Melek miydi" — dizi/film klibi + soru kartı | 10 sn | 19.08 Çarş. 07:21 | 277 | 11 (%4,0) | 2 / 1 | telifli görüntü |
| benim-5 | "Fena Alıştım Sana" — Spotify söz ekranı kaydı | 37 sn | 18.08 Salı 18:47 | 268 | 10 (%3,7) | 4 / 1 | ekran kaydı + letterbox |
| benim-7 | "Üfle Söndür" mangal skeci (AI çift) | 10 sn | 18.08 Salı 13:56 | 304 | 7 (%2,3) | 3 / 2 | |
| benim-8 | AI kafe skeci + stüdyo söz ("Ben de çoktan bitti ama") | 19 sn | 18.08 Salı 08:45 | 277 | 7 (%2,5) | 4 / 1 | |
| benim-9 | "Eski sevgiliye cevabınız?" — sinematik çakmak/parfüm | 14 sn | 17.08 Pzt 09:49 | 478 | 12 (%2,5) | 2 / 4 | letterbox'lu |
| benim-10 | Afiş + stüdyoda karaoke söz ("EN NET SÖZ") | 10 sn | 16.08 Pazar 12:31 | 274 | 10 (%3,6) | 4 / 4 | **en iyi format** |
| benim-11 | Albüm tanıtımı: 6 şarkı derlemesi (Kalbime Yolculuk) | 80 sn | 15.08 Cmt 21:29 | 256 | 7 (%2,7) | 1 / 3 | |
| benim-12 | "Yapay zekâ ile deneme yaptım, nasıl olmuş?" stüdyo | 15 sn | 14.08 Perş. 06:33 | 280 | 18 (%6,4) | 10 / 6 | **en iyi etkileşim** |
| benim-13 | 💰 REKLAM verilen: "aşk değil alışkanlık mı?" duvar + söz | 14 sn | 11.08 Salı 08:18 | **63.500** | 43 (**%0,07**) | 0 / 16 | reklam gösterimi |
| benim-14 | CapCut şablonu: gece şehri + gül/zambak + söz kartı | 7 sn | 10.08 Pazar 08:46 | 289 | 14 (%4,8) | 1 / 2 | adlandırılmış müzik ✓ |
| benim-15 | "Şeytan mısın Melek misin" + 11 şarkılık albüm listesi | 17 sn | 08.08 Cmt 10:18 | 326 | 20 (%6,1) | 4 / 5 | |
| benim-16 | Deniz kenarı çay + "Hayat çok kısa… ne mutlu ediyorsa onu yap" | 11 sn | 04.08 Salı 10:29 | 303 | 19 (%6,3) | 1 / 3 | müzik dışı içerik |

### Görsel analiz özetleri (1b eş derinlik)

- **benim-1:** #001–#003 afiş kartı ("EX'DEN MESAJ GELSE NE YAPARSIN?"), #004–#011
  AI elde telefon planı, #012–#015 mesaj balonu + "KABUL EDERDİN / REDDEDERDİN :)"
  butonları, #016–#024 stüdyoda söyleyen sanatçı + "Yorum yap ya da Anketi
  cevapla :)". **Video dar bantta, üst/alt geniş siyah bar** (ekran alanının
  ~%45'i boş). Şarkı ancak 7. saniyede giriyor.
- **benim-2:** #001–#019 bir dizi/film sahnesi (vitrin camında yansıma, çift) —
  telifli üçüncü taraf görüntü; #020–#022 siyah zemin soru kartı "Eski sevgilin
  Şeyta[n] mıydı, Melek miydi?" (yazım hatası: "Seyta mıydı"). Şarkı arka planda.
- **benim-5:** 37 sn boyunca **Spotify söz ekranının kaydı** (kırmızı zemin,
  kayan söz duvarı, arkada sanatçı fotoğrafı); tüm sözler aynı anda ekranda,
  punto küçük; üst/alt siyah bar. Kayan vurgu dışında hareket yok.
- **benim-7:** AI mangal skeci: adamın eli yanıyor, soru overlay "Elin yansa
  sevgilinden hangisini beklersin? 💋 Öpsün mü 💨 üflesin mi?", kadın üflüyor →
  "ÜFLE ÜFLE SÖNDÜR" yazısı şarkıyla senkron. Konsept iyi; kadraj tam dikey ✓.
- **benim-8:** AI kafe skeci (yeşil elbiseli kadın geçiyor, adam yakasını
  düzeltiyor) #001–#017 → sert kesmeyle karanlık stüdyoda sanatçı + söz
  "Ben de çoktan bitti ama" #018–#030. İki yarı arasında ışık/ton uçurumu var.
- **benim-9:** Sinematik parfüm/çakmak/yüzleşme planları (kaliteli görüntü) ama
  **çift siyah bar** (üstte soru, altta "Yorumlara bekliyorum 💨", video ortada
  ince şerit). Şarkı kimliği görünmüyor.
- **benim-10:** #001–#003 GERÇEK afiş kartı ("ESKİ SEVGİLİYE SÖYLENECEK EN NET
  SÖZ", kırık kalp + mum görseli) → #004–#021 stüdyoda sanatçı, **kelime kelime
  dev sarı karaoke yazısı**: "BEN DE ÇOKTAN BİTTİ AMA SENDE HALA YANGIN VAR —
  ÜFLE ÜFLE SÖNDÜR". Tam ekran 9:16, yüz + söz + ritim senkron. **Kanaldaki en
  doğru format; viral-2/3 kalıbıyla aynı ailede.**
- **benim-11:** benim-10'un 80 saniyelik albüm versiyonu: 6 şarkıdan pasajlar,
  aynı stüdyo karaoke düzeni (retrobesto'nun "menü" formatının doğru fikri!).
- **benim-12:** Stüdyoda şarkı söyleyen sanatçı (AI görsel deneme), sabit metin:
  "Yapay zekâ ile ufak bir deneme yaptım. Sizce nasıl olmuş?" — kanalın en
  yüksek etkileşim oranı (%6,4 beğeni, 10 yorum): AI sorusu konuşturuyor
  (retrobesto bulgusuyla tutarlı).
- **benim-13 (REKLAM):** Duvara yaslanan sanatçı, kelime kelime söz ("SEN
  GELDİN AYARIM KAÇTI BİR GÜLDÜN KALBİM ŞAŞTI…"), hayalet/çözülme geçişleri,
  üstte soru "Bazen aşk değil de alışkanlık mı canımızı yakıyor?". Kreatif fena
  değil; ama reklam kitlesi hiç etkileşmemiş (43 beğeni / 63.500 gösterim =
  %0,07; 0 yorum). 16 paylaşım muhtemelen "paylaş" butonuyla link kopyalama.
- **benim-14:** 7 sn CapCut şablonu: gece şehri yürüyüşü + gül/zambak makroları
  + siyah söz kartı "Gitmen gerektiğini biliyordun. Ama kalmayı sen seçtin."
  Şık ama 7 sn'de şarkı duyulamadan bitiyor.
- **benim-15:** Karanlık sokak portreleri + ışıklı yazı "ŞEYTAN MISIN / MELEK
  MİSİN?" → 11 şarkılık albüm listesi kartı ("Kalbime Yolculuk": Şeytan mısın
  Melek misin, Kendime not, Kıvırcık, …, Zamanın Doldu). Liste 8. saniyede
  geliyor ve 9 sn ekranda — okunacak yoğunlukta değil.
- **benim-16:** Deniz kenarında çay içen sanatçı + "Hayat çok kısa… Seni ne
  MUTLU ediyorsa onu yap :)" — motivasyon içeriği; şarkı tanıtım işlevi yok;
  kanal kimliğini sulandırıyor.

### Numaralandırılmış hata/eksik listesi (EKSİKSİZ)

Her madde: (a) sorun, (b) nerede görülüyor, (c) viral referanslar doğrusunu
nasıl yapıyor.

1. **~280 izlenme duvarı — hiçbir gönderi ilk test havuzunu aşamıyor.**
   (a) 13 organik gönderinin tamamı 256–478 bandında; bu, TikTok'un her
   gönderiye verdiği ilk örneklem (takipçi + küçük soğuk kitle) seviyesidir —
   keşfet dağıtımı hiç başlamamış. (b) Özet tablodaki izlenme sütunu.
   (c) Referanslarda ilk havuzu aşan sinyal, izlenme süresi + paylaşım
   (viral-2: %1,5 paylaşım; viral-10: %0,9).
2. **Şarkı hiçbir gönderide "kahraman" olarak ilk 2 saniyede duyulmuyor.**
   (a) Gönderiler afiş kartı/soru kartıyla açılıyor (benim-1: 1,5 sn kart;
   benim-10: 1,5 sn kart; benim-13: soru), vokal geç giriyor (benim-1'de 7.
   sn). (b) İlgili kare damgaları: benim-1 #001–#003, benim-10 #001–#003.
   (c) viral-2/7: nakarat 0,0. saniyede tam kurulmuş sahneyle girer; CTA/soru
   videonun İÇİNDE ama sonda ya da kalıcı ince overlay olarak durur.
3. **Letterbox/siyah bar üç videoda ekranın yarısını yutuyor.** (a) Video
   içeriği dar şeritte, üst/alt simsiyah. (b) benim-1 (tüm kareler), benim-5,
   benim-9. (c) Referansların tamamı tam ekran 9:16; TikTok tam dikey
   doldurmayan içeriğe düşük kalite sinyali uygular.
4. **Ekran kaydı formatı (Spotify söz ekranı).** (a) 37 sn statik ekran kaydı;
   küçük punto, tüm sözler aynı anda görünür — okunacak "sıradaki satır"
   merakı yok. (b) benim-5. (c) viral-1/2 sözleri BLOK BLOK, büyük puntoyla ve
   zamanla eşitleyerek verir; izleyici satırı beklerken video izlenmiş olur.
5. **Telifli üçüncü taraf görüntüsü.** (a) Dizi/film sahnesi kullanımı hem
   telif eşleşmesi/dağıtım kısıtlaması riski hem kimliksizlik yaratıyor.
   (b) benim-2 #001–#019. (c) Referanslar ya kendi AI üretimini (viral-7/9) ya
   kendi çekimini (viral-10/14) kullanıyor.
6. **Soru/anket formatı şarkının önüne geçmiş.** (a) 6 gönderi (benim-1, 2, 7,
   9, 10, 13) "eski sevgili sorusu" etrafında; ama soruyu taşıyan şarkı pasajı
   10–14 sn'de tanıtım değeri üretemiyor; kanal "anket kanalı"na benziyor.
   (b) Özet tablo. (c) viral-2'de soru BAŞLIKTA, video tamamen şarkı+söz;
   yorum tetikleyici tek katman yeter.
7. **Yükleme saatleri kazanan banda uymuyor.** (a) 13 gönderiden 9'u 06:33–
   12:54 UTC (09:33–15:54 TR) bandında; kazanan referans bandı 16:00–21:30 TR.
   (b) Özet tablo yükleme sütunu. (c) viral-2 Salı 16:51 TR, viral-7 Pzt 00:49
   TR (lansman istisnası), viral-4 Çarş. 20:32 TR.
8. **7–19 saniyelik süreler izlenme-süresi sinyali biriktiremiyor.** (a) 13
   gönderinin 10'u ≤19 sn; şarkı pasajı akılda kalmadan bitiyor. (b) Süre
   sütunu. (c) Kazanan söz videoları 32–71 sn (viral-2: 71, viral-3: 32).
9. **#keşfetteyizzz / #keşfetbeni / #fyp hile etiketleri.** (a) 5 gönderide
   var; viral-16 analizinde bu etiketlerin işe yaramadığı görülmüştü; arama
   niyeti taşıyan etiketlerin (türkçepop, şarkısözleri, damar) yerini yiyor.
   (b) benim-10, 11, 12, 14, 15. (c) MELEX'in katmanlı seti: geniş tür + kimlik
   + niş tür + arama.
10. **Konum/kitle sinyal karışıklığı (SE→TR).** (a) Hesap İsveç'ten Türkçe
    içerik atıyor; ilk test havuzuna giren yerel (İsveçli) kullanıcı Türkçe söz
    videosuyla etkileşmez → ilk havuz sinyali zayıflar. (b) Tüm gönderilerde
    `olusturuldugu_ulke: SE`. (c) Aynı durumdaki MELEX/FEROV (DE) bunu iki
    dilli içerik + diaspora/global etiketlerle çözüyor (viral-3: TR+RU;
    viral-14: İngilizce başlık); Natali (viral-10) Alanya etiketiyle yerel
    kitleye bağlanıyor.
11. **Reklam kreatifi soğuk kitlede dönüşmemiş.** (a) 63.500 gösterim → 43
    beğeni (%0,07), 0 yorum: gösterim satın alınmış ama içerik reklam
    kitlesini durduramamış; reklam izlenmeleri organik keşfet sinyali de
    üretmez. (b) benim-13. (c) viral-7'nin muhtemel tanıtımlı 396k'sı bile
    %0,56 tutmuştu; sağlıklı organik bant %3–5.
12. **Albüm listesi kartı okunamıyor.** (a) 11 satırlık liste 9 sn ekranda,
    küçük punto. (b) benim-15 #016–#024. (c) retrobesto (viral-8) her şarkıya
    ~10 sn ayrı afiş veriyor — liste değil, sıralı vitrin.
13. **Müzik dışı motivasyon içeriği kanal kimliğini bulandırıyor.** (a) "Hayat
    çok kısa…" videosunun şarkı tanıtımıyla ilgisi yok; algoritmanın kanalı
    sınıflandırmasını zorlaştırıyor. (b) benim-16. (c) Referans kanalların
    tamamı tek konsept (Can Güven: söz videoları; retrobesto: retro afişler).
14. **Yazım hataları.** (a) "Şeyta mıydı" (benim-2 kartı), "ufak bie deneme"
    (benim-12 açıklama). (b) İlgili kare/metadata. (c) Profesyonel algı için
    sıfır tolerans.
15. **Fotoğraf gönderileri erişilemez durumda** (benim-3/4/6). (a) Bu üç
    gönderi anonim/giriş yapmamış kullanıcılara hiç servis edilmiyor — bu
    hâliyle harici paylaşım linkleri de ölü. (b) Bölüm 2 girişindeki not.
    (c) viral-4 (MELEX'in slaytı) anonim erişime açık ve 27k almıştı. Bu üç
    gönderinin uygulama içinden kontrol edilmesi gerekir (kısıtlama uyarısı
    var mı) — gerekiyorsa aynı içerik yeniden gönderilmeli.

### Kullanıcının sorularına doğrudan cevaplar

**a. Neden keşfete düşmedi?**
Tek bir neden değil, birbirini besleyen dört katman:
1. **Sinyal üretimi yetersiz:** İlk test havuzunda (≈300 gösterim) TikTok'un
   büyütme kararı verdiği metrikler tamamlanma + tekrar izlenme + paylaşımdır.
   Gönderiler soru kartı/afişle açılıp şarkıyı geç verdiği, süreler 7–19 sn
   olduğu ve paylaşılacak "cümle/sahne" içermediği için bu eşik hiç aşılmamış
   (13 gönderide toplam paylaşım: 38 — viral-2 tek başına 971).
2. **Format cezaları:** letterbox (3 video), ekran kaydı (1), telifli görüntü
   (1) — bunlar hem izleyici davranışını hem platformun kalite
   sınıflandırmasını olumsuz etkiler.
3. **Kitle-sinyal uyumsuzluğu:** İsveç konumundan tek dilli Türkçe içerik →
   ilk havuzun bir kısmı yanlış kitle; diaspora kanallarının kullandığı iki
   dillilik/yerel etiket köprüsü kurulmamış.
4. **Kanal geçmişi:** 242 gönderinin neredeyse tamamı aynı duvara çarpmış;
   algoritma kanala dair "düşük etkileşimli hesap" önseli biriktirmiş olabilir
   (resmî olarak doğrulanmış bir mekanizma değil, ama gözlemlenen davranışla
   tutarlı). ÖNEMLİ: içerik fikirleri (Üfle Söndür konsepti, stüdyo karaoke)
   ve örneklem içi etkileşim oranları (%4–6) İYİ — sorun yaratıcılıkta değil,
   paketleme ve dağıtım mühendisliğinde.

**b. Değişiklik yapmalı mıyız?**
Evet, ama doğru yerde: **eski gönderileri düzenlemek değil, yeni gönderileri
doğru kalıpla atmak.** TikTok'ta yayınlanmış videonun görüntüsü değiştirilemez;
açıklama/etiket düzenlemesi eski bir gönderiyi yeniden dağıtıma sokmaz. Eski
gönderileri silmeye de gerek yok (kanala zararı yok). Yapılacaklar Bölüm 5'te
gönderi gönderi listelendi; özet: en iyi 4 konsept (benim-10, 7, 12, 11) doğru
kalıpla YENİDEN çekilip/kurgulanıp yeni gönderi olarak atılmalı.

**c. Yapılan değişiklik etki eder mi?**
- Eski gönderide metadata düzenlemesi: **etkisi ihmal edilebilir** (arama
  görünürlüğünde marjinal düzelme dışında).
- Yeni gönderilerde kalıp düzeltmesi: **evet, kanıta dayalı olarak.** Aynı
  kanalın kalıp değişikliğiyle 6–15 kat oynadığını referanslarda ölçtük
  (MELEX viral-3 vs viral-11; FEROV viral-5 vs viral-13). Takipçi sayısı engel
  değil: 1.451 takipçili retrobesto 43,6k; 4.447 takipçili Ayşe Çetin 396k;
  6.608 takipçili Can Güven 63k yaptı. Sizin örneklem içi beğeni oranlarınız
  (%4–6) referans bandında — içerik gösterildiğinde tutuyor; kırılması gereken
  şey ilk havuz eşiği. Gerçekçi hedef: düzeltilmiş kalıpla ilk 4–6 haftada
  1k–10k bandına düzenli çıkmak, tek "isabet"le 50k+ denemesi.
- Reklam: mevcut kreatifle tekrarlanmamalı (%0,07 kanıtı). Reklam ancak
  organik olarak zaten tutmuş bir videoyu büyütmek için anlamlı.

**d. Yeni gönderiler için strateji planı:** Bölüm 4'teki paket bu 18 referans +
16 kendi gönderisi analiziyle güncel; uygulama planı aşağıda (Bölüm 5 sonrası
"STRATEJİ PLANI" alt bölümü).

## 3. Karşılaştırma tablosu

### 3A. Kazanan kalıp vs @hasancamuzik (güncel)

| Boyut | Kazanan referans kalıbı | @hasancamuzik mevcut durum | Fark |
|---|---|---|---|
| Hook (ilk 2 sn) | Nakarat vokali + tam kurulmuş sahne 0,0 sn'de (viral-2/7) | Afiş/soru kartı, şarkı 4.–7. sn'de | ❌ kritik |
| Süre | 32–71 sn söz videosu | 7–19 sn ağırlıklı | ❌ kritik |
| Ekran kullanımı | Tam 9:16 | 3 videoda %45+ siyah bar | ❌ |
| Söz katmanı | Blok blok / kelime kelime büyük punto | Var (benim-10/11/13 ✓), bazılarında yok veya ekran kaydı | ⚠️ kısmen |
| Paylaştırılabilir cümle | "Gözün sadece bende olsun" tipi ikinci şahıs cümle | Var ama soru formatına gömülü | ⚠️ |
| CTA | Tek, geç (son 8–10 sn) veya kalıcı ince soru | Soru ana içerik olmuş | ❌ |
| Etiket | Katmanlı: tür + kimlik + niş + arama | keşfetteyizzz/fyp hileleri karışık | ⚠️ |
| Yükleme saati | Salı–Çarş. 16:00–21:30 TR | Ağırlıkla sabah/öğle TR | ❌ |
| İki dillilik / kitle köprüsü | TR+RU veya EN (diaspora kanalları) | Yok (SE'den tek dilli TR) | ❌ |
| Ses stratejisi | Adlandırılmış tek ses, üçüncü kişi kullanımı hedefli | Çoğu "orijinal ses", benim-14 ✓ | ⚠️ |
| Örneklem içi beğeni | %3–5 | %4–6 ✓ | ✅ güçlü yan |
| Prodüksiyon fikri | Tek şablon, seri üretim | Yaratıcı ve çeşitli ✓ (ama dağınık) | ✅/⚠️ |

### 3B. Viral videolar kendi aralarında (ilk partinin tablosu)

| Boyut | viral-1 | viral-2 ⭐ | viral-3 | viral-4 | viral-5 | Kullanıcı videosu |
|---|---|---|---|---|---|---|
| Hook (ilk 3 sn) | Başlık kartı + AI yüz | Başlık kartı + AI çift + orkestra | FPV drone + 2 dilli kinetik söz | "it's just a song…" tersleme | Sahte Spotify UI | — (video verilmedi) |
| Süre | 61 sn | 71 sn | 32 sn | 3 slayt | 64 sn | — |
| Tempo | Statik + söz değişimi | Statik + söz değişimi | 4–7 sn'de plan | Kullanıcı kaydırır | 1–2 sn'de klip | — |
| Overlay/söz | 8 söz bloğu | 10 söz bloğu | TR+RU çift katman | TR slayt + RU slayt | Söz YOK | — |
| CTA sayısı/zamanı | 1 (00:50–58) | 1 (01:02–08) | 0 (açıklamada tarih) | 0 | 0 (dolaylı) | — |
| Başlık stili | Marka/telif kalıbı | Marka/telif kalıbı | Tarihli duyuru | Yalnız etiket | "OUT NOW" | — |
| Etiket sayısı | 0 | 0 | 5 | 5 | 5 | — |
| Yükleme zamanı (TR) | Çarş. 19:39 | Salı 16:51 | Çarş. 13:52 | Çarş. 20:32 | Pazar 09:37 | — |
| Günlük izlenme | ~5.800 | **~31.500** | ~13.000 | ~652 | ~206 | — |
| Paylaşım | 94 | **971** | 104 | 132 | 24 | — |
| İzlenme/takipçi | 0,9× | **9,5×** | 4,1× | 8,6× | 1,0× | — |

**Tablonun söylediği kazanan kalıp:** ekranda akan Türkçe söz + ilk karede tam
kurulmuş sahne + hafta içi 16:00–20:30 TR yüklemesi + tek geç CTA (veya çıkış
tarihi kancası) + (MELEX örneğinde) TR+RU iki dillilik ve katmanlı etiket seti.
Büyümenin ölçülebilir motoru **paylaşım**: en hızlı iki içerik (viral-2, viral-4)
aynı zamanda "sevgiliye/arkadaşa gönderilecek cümle" içeren iki içerik.

## 4. Yeni video önerisi — EKSİKSİZ paket

Hedef: HASANCA kataloğundan duygusal bir parçayla (öneri: **"Seni İçimden Nasıl
Sökeyim"** veya **"Beni En İyi Sen Kırdın"** — başlıkları zaten viral-2 tarzı
"izleyiciye söylenen cümle") TikTok + Instagram Reels + YouTube Shorts yüklemesi.

### 4a. Başlık alternatifleri (10+; her biri neden işe yarar)

1. **"Beni En İyi Sen Kırdın 💔 bu sözü kime söylerdin?"** — viral-2'nin "sana
   söylenen cümle" kancası + yorum tetikleyen soru.
2. **"🎵 Beni En İyi Sen Kırdın ✍️ Söz & Müzik: HASANCA"** — viral-1/2'nin
   kanıtlanmış marka/telif kalıbının birebir uyarlaması.
3. **"05.09.2026 🖤 Seni İçimden Nasıl Sökeyim çıkıyor!"** — viral-3'ün tarihli
   beklenti kancası (çıkış öncesi teaser için).
4. **"it's just a song... 🇹🇷"** — viral-4'te 27k izlenme almış terslemenin aynen
   kullanımı (slayt gönderisi için).
5. **"Bu şarkıyı gece 2'de dinleyenler bilir 🌙"** — zaman/ruh hâli hedefli merak
   boşluğu; gece kaydırma kitlesine konuşur.
6. **"Sözlerini yazarken ağladığım şarkı 🥀"** — sanatçı itirafı; otantiklik +
   merak, yorum davet eder.
7. **"Turkish Pop x Arabesk — you don't need to understand the words 🎧🇹🇷"** —
   MELEX'in global köprü kalıbı; yabancı kitleye erişim.
8. **"Kalbi kırık olanlar sesi sonuna kadar açsın 🔊"** — komut kipi + duygu
   kimliği; kaydet/paylaş davranışı tetikler.
9. **"Bir şarkı en fazla ne kadar acıtabilir? 60 saniyede test et"** — meydan
   okuma formatı; tamamlanma oranını hedefler.
10. **"Annenize gönderin: bizim kuşağın arabeski geri döndü 📼"** — paylaşım
    (send-to) davranışını doğrudan ister; viral-4'ün 132 paylaşım dersi.
11. **"Gözün Sadece Bende Olsun'u sevenler buraya 👇"** — viral-2'nin kitlesini
    doğrudan çağırır (ses/keşfet komşuluğu).

### 4b. Kopyala-yapıştır açıklama metinleri (platform başına)

**TikTok:**
```
Beni En İyi Sen Kırdın 💔 bu sözü kime söylerdin, yorumlara yaz…
🎵 Söz & Müzik: HASANCA
Tamamı profildeki linkte 🎧
#hasanca #türkçepop #arabesk #şarkısözleri #keşfet
```

**Instagram Reels:**
```
Beni En İyi Sen Kırdın 💔
Bu sözü içinden kime söyledin? 👇
🎵 Söz & Müzik: HASANCA — tamamı bio'daki linkte
Kaydet, gece tekrar dinlersin 🌙
#hasanca #türkçepop #arabesk #aşksözleri #reelsturkiye
```

**YouTube Shorts:**
```
Beni En İyi Sen Kırdın — HASANCA (Official Lyric Short)
Şarkının tamamı kanalda ▶️ Abone olmayı unutmayın.
Söz & Müzik: HASANCA © Tüm hakları saklıdır
#HASANCA #TürkçePop #Arabesk #Shorts
```

### 4c. Etiketler (30+; platform başına geniş/orta/niş)

**TikTok (12):**
- Geniş: `#keşfet` `#fyp` `#müzik` `#viral`
- Orta: `#türkçepop` `#arabesk` `#şarkı` `#şarkısözleri`
- Niş: `#hasanca` `#poparabesk` `#türkçesözler` `#yenişarkı`

**Instagram Reels (12):**
- Geniş: `#reels` `#müzik` `#aşk` `#explore`
- Orta: `#türkçepop` `#arabesk` `#şarkısözleri` `#reelsturkiye`
- Niş: `#hasanca` `#poparabesk` `#duygusalşarkılar` `#gecemodu`

**YouTube Shorts (10):**
- Geniş: `#shorts` `#music` `#türkçemüzik`
- Orta: `#türkçepop` `#arabesk` `#lyricvideo` `#şarkısözü`
- Niş: `#hasanca` `#poparabesk` `#turkishpop`

(Toplam 34; MELEX modeli izlenirse `#russian` / RU altyazılı sürümde
`#турецкиепесни` eklenebilir.)

### 4d. Saniye saniye içerik akışı (60 sn'lik ana video)

| Zaman | Görüntü | Ses | Ekran yazısı |
|---|---|---|---|
| 0:00–0:01 | Tam kurulmuş sahne: şarkı adı altın tipografiyle + atmosferik görsel (viral-1/2 kalıbı: loş mekân, tek figür silüeti) + dalga formu | Şarkının EN vurucu nakarat cümlesi hemen girer (intro yok) | Üstte: "bu sözü kime söylerdin? 👇" |
| 0:01–0:06 | Aynı sahne; ışık nabzı (hafif parlama-kararma döngüsü) | Nakarat devam | Söz satırı 1 ekranda (büyük, ortada) |
| 0:06–0:14 | Işık nabzı sürer; ✨ parıltı animasyonu | 1. kıta | Söz bloğu 2 (satır satır değişir, ~8 sn'de bir) |
| 0:14–0:22 | Renk tonu kısa süre soğuğa kayıp döner (viral-1'deki turkuaz nabız) | 1. kıta devamı | Söz bloğu 3 |
| 0:22–0:30 | Sahnede küçük değişim: kamera çok yavaş zoom-in (statiği kırar) | Pre-chorus | Söz bloğu 4 |
| 0:30–0:38 | Zoom devam; dalga formu genliği artar | NAKARAT (ikinci geliş) | Nakarat cümlesi büyük puntoyla, ❤️ ile |
| 0:38–0:46 | Işık patlaması geçişi; görselde altın parçacıklar | Nakarat devamı | Söz bloğu 5 |
| 0:46–0:52 | Sahne sakinleşir | Köprü/son kıta | Söz bloğu 6 |
| 0:52–0:58 | Aynı sahne | Nakaratın son tekrarı kısılarak | CTA: "Devamı profilde 🎧 Takip et, kaydet" |
| 0:58–1:00 | İlk kareye dönüş (döngü hissi: video başa sarmış gibi biter) | Son vuruş | Şarkı adı + HASANCA logosu |

**Döngü hilesi:** son kare = ilk kare → otomatik tekrar izlenme (viral-3'ün loop
etkisinin statik uyarlaması).

### 4e. Toplam süre önerisi (platform başına, gerekçeli)

- **TikTok:** **60–70 sn** — viral-1 (61) ve viral-2'nin (71) kanıtladığı bölge;
  söz videosunda izleyici okuyarak kaldığı için 60+ sn izlenme süresi sinyalini
  büyütüyor. Teaser varyantı: **30–35 sn** (viral-3 kalıbı).
- **Instagram Reels:** **45–60 sn** — Reels'te tamamlanma oranı daha belirleyici;
  aynı kurgunun 4. söz bloğu kısaltılmış hâli.
- **YouTube Shorts:** **55–60 sn** — Shorts rafında 60 sn sınırına yakın kalıp
  kanala abone CTA'sı için son 8 sn kullanılmalı (viral-2'nin teşekkür kalıbı).

### 4f. Hook planı — ilk 3 saniyenin tam tarifi

- **0,0 sn:** Ekran TAM kurulu açılır (fade-in YOK): üstte soru overlay'i ("bu
  sözü kime söylerdin? 👇"), ortada şarkı adı altın el yazısı tipografiyle
  ("Beni En İyi Sen KIRDIN"), altında "Söz•Müzik HASANCA", ortada animasyonlu
  dalga formu, arkada atmosferik figürlü görsel. Ses: nakaratın en can alıcı
  cümlesi TAM vokal girişiyle başlar — enstrümantal intro kesilir.
- **0,5 sn:** İlk söz satırı ✨ ile belirir (viral-1'de kanca #002'de gelmişti).
- **1,5–3,0 sn:** Işık nabzının ilk döngüsü; dalga formu vokalle oynar. Konu,
  sanatçı ve duygu 1. saniyede belli — viral-1/2'nin birebir açılış disiplini.

### 4g. CTA planı

- **CTA sayısı: 2** (yazılı; sözlü yok — referansların hiçbirinde sözlü CTA yok).
- **CTA-1 (pasif, 0:00–1:00):** üst overlay sorusu "bu sözü kime söylerdin? 👇"
  — yorum CTA'sı, video boyunca kalır (viral-2'nin 198 yorumluk dersi).
- **CTA-2 (aktif, 0:52–0:58):** "Devamı profilde 🎧 Takip et, kaydet ⭐" —
  viral-1 (#101, 00:50) ve viral-2 (#125, 01:02) ile aynı bölgede: SON 8–10
  saniye. İlk 50 saniyede takip çağrısı YAPILMAZ.
- Kelime seçimi: "abone ol" yerine TikTok/IG'de "takip et + kaydet" (kaydet,
  algoritmada en ağır sinyallerden).

### 4h. Efekt ve görsel öneriler

- **Şablon:** siyah + altın palet, altın el yazısı başlık, beyaz/altın dalga
  formu (viral-1/2'nin kanıtlanmış kimliği; HASANCA için tutarlı seri şablonu
  kurulmalı — her şarkıda aynı düzen, farklı görsel).
- **Görsel:** tek yüksek kaliteli sahne (AI veya fotoğraf) — çift/insan figürü
  içeren sahne tek yüzden iyi performans veriyor (viral-2 vs viral-1: 10 kat).
- **Hareket:** statik görselde 3 katman: (1) 8–10 sn'de bir söz bloğu değişimi,
  (2) 15–20 sn'de bir renk/ışık nabzı, (3) çok yavaş zoom. Sert geçiş yok.
- **Yazı stili:** sözler beyaz, yarı saydam koyu şerit üstünde, ortada; nakarat
  satırları daha büyük punto + ❤️/✨. TR+RU çift katman denemesi için: TR kırmızı
  kalın üstte, RU ince beyaz altta (viral-3 düzeni).
- **Teaser varyantı için:** gerçek çekim drone/şehir görüntüsü + kinetik kırmızı
  söz tipografisi + beat-senkron kesme (viral-3), veya 3 slaytlık fotoğraf
  gönderisi: kapak ("it's just a song…" tarzı) + TR söz kartı + RU söz kartı
  (viral-4 — üretim maliyeti en düşük, paylaşım oranı en yüksek format).

### 4i. Yayın zamanı önerisi

Referans verisi: viral-2 Salı 16:51 TR (~31k/gün), viral-1 Çarşamba 19:39 TR,
viral-4 Çarşamba 20:32 TR, viral-3 Çarşamba 13:52 TR — hepsi hafta içi; tek
düşük performanslı yükleme Pazar sabahı (viral-5, 206/gün).

- **Ana öneri:** **Salı veya Çarşamba, 16:30–20:30 TR** (ilk tercih Salı ~17:00 —
  viral-2'nin dilimi).
- **Kaçınılacak:** hafta sonu sabahları (viral-5 dersi).
- Seri strateji: ana video Salı 17:00; teaser/slayt varyantı Çarşamba 20:00.

### 4j. Kapak / ilk kare önerisi

- İlk kare = kapak (viral-1/2/3 hepsinde böyle): şarkı adı ALTIN el yazısı
  tipografiyle ortada, sanatçı adı altında, atmosferik figürlü sahne arkada,
  üstte soru overlay'i. Profil ızgarasında okunması için başlık ekranın orta
  1/3'ünde ve kenarlardan taşmıyor olmalı.
- Slayt gönderisinde kapak: az yazılı, yüksek estetik tek cümle kartı ("it's
  just a song… 🇹🇷" kalıbı — viral-4 foto_1).

### 4k. (Ek) Kanal düzeyi öneriler — referans kanalların metadata'sından

- **Ses stratejisi:** Her yüklemede şarkı "orijinal ses – HASANCA" olarak
  bağlanmalı (5/5 referans böyle yapıyor); sesi kullanan her izleyici videosu
  kanala geri trafik üretir.
- **Bio/imza:** MELEX kalıbı: kimlik + güncel single + tür + diğer platform
  köprüsü. Öneri: "HASANCA 🎤 | Pop • Arabesk | <Güncel Şarkı> (OUT NOW) 🎧 |
  YouTube/Spotify: HASANCA".
- **Takipçi sayısı bahane değil:** referansların hepsi 3–7k takipçili; viral-2
  izlenmesinin %90'ı takipçi dışından geldi. Strateji abone büyütmek değil,
  paylaştırılabilir cümle + tamamlanma süresi üretmek olmalı.
- **Seri üretim + şablon:** Can Güven 176, FEROV 203 video yüklemiş; patlama
  oranı düşük ama şablon maliyeti sıfıra yakın olduğundan deneme sayısı
  arttıkça isabet geliyor. HASANCA'nın 30+ parçalık kataloğu bu şablonla
  haftada 2–3 yüklemeye yeter.

## 5. Eski videolar için yeniden düzenleme planı

Genel kural (Bölüm 2b'deki gerekçeyle): TikTok'ta eski videonun görüntüsü
değiştirilemez; bu yüzden karar üç seçenekten biri: **(K)** olduğu gibi kalsın,
**(Y)** düzeltilmiş versiyonu YENİ gönderi olarak at, **(M)** yalnız metadata
(açıklama/etiket) düzelt. Silme önerilmiyor.

| Gönderi | Karar | Yapılacak |
|---|---|---|
| benim-1 (EX anketi) | **Y** | Yeniden kurgula: siyah barlar at (tam 9:16), nakarat 0,0 sn'de girsin, telefon/mesaj sahnesi 2.–5. sn'e, "Kabul/Ret 👇" kalıcı ince üst overlay olsun, süre 30 sn+. Yeni başlık: "EX'den bu mesaj gelse: kabul mü, ret mi? 👇" |
| benim-2 (dizi klibi) | **K** (tekrarı yok) | Telifli görüntüyü bir daha kullanma; aynı soru konsepti benim-15'in kendi çekimleriyle yeniden üretilebilir. Karttaki "Şeyta mıydı" yazımı ders olsun. |
| benim-5 (Spotify kaydı) | **Y** | Ekran kaydını at; aynı şarkıyı viral-1/2 kalıbıyla yeniden yap: tek estetik sahne + altın tipografi başlık + blok blok söz + dalga formu, 60 sn. |
| benim-7 (mangal skeci) | **Y (öncelikli)** | Konsept güçlü. Yeniden kurgu: 0,0 sn'de "ÜFLE ÜFLE SÖNDÜR" nakarat vokali + üfleme anı; skeç 2.–8. sn; soru kalıcı üst overlay; sona "devamı profilde 🎧". 20–30 sn. |
| benim-8 (kafe + stüdyo) | **M** | Açıklamaya şarkı adı + katmanlı etiket seti; gelecekte iki yarının renk uyumunu eşitle. |
| benim-9 (çakmak sinematik) | **Y** | Görüntüler kaliteli: tam ekrana yeniden kadrajla, soruyu tek satır ince overlay yap, şarkının en vurucu 25 saniyesini koy. |
| benim-10 (EN NET SÖZ) | **Y (şablon adayı)** | Kanalın en iyi formatı. Düzeltme: afiş kartını at (0,0 sn'de vokal + yüz + ilk kelime), 30 sn'e uzat, son 5 sn "kaydet + profil" CTA'sı. Bu düzen HASANCA'nın standart şablonu olsun. |
| benim-11 (albüm medley) | **Y** | retrobesto kalıbına çevir: her şarkıya ~10 sn AYRI afiş/sahne + şarkı adı büyük puntoyla; sonda albüm kapanış kartı + "hangisi favorin? 👇". 60–90 sn. |
| benim-12 (AI deneme) | **M + devam** | En iyi etkileşim. Açıklamaya "yapay zekâ" tartışma sorusunu koymaya devam; yazım hatasını düzelt; bu seriyi düzenli yap ("AI ile şu şarkıyı böyle görselledim, hangisi daha iyi? A/B"). |
| benim-13 (reklamlı) | **K** | Reklamı bu kreatifle yenileme. Ders alındı; organik tutan video çıkınca reklam o videoya verilebilir. |
| benim-14 (CapCut 7 sn) | **M** | 7 sn'lik hâliyle kalsın; adlandırılmış müzik kullanımı doğru — bundan sonra tüm gönderilerde adlandırılmış ses kullan. |
| benim-15 (albüm listesi) | **Y** | Liste kartını parçala: her gönderide 1 şarkı adı + 1 vurucu söz kartı (viral-4 slayt formatı da uygun — 3 kart: kapak/TR söz/albüm listesi). |
| benim-16 (motivasyon) | **K** | Müzik dışı içeriği ayrı seriye/hesaba taşı ya da bırak; ana kanalda tek kimlik: şarkı + söz. |
| benim-3/4/6 (foto, erişilemedi) | **kontrol** | Uygulamada aç: "Bu gönderi bazı bölgelerde gösterilmiyor / uygunluk" uyarısı var mı bak; slaytlar keşfette görünmüyorsa aynı kartları yeni gönderi olarak paylaş (viral-4 kalıbı: kapak-tersleme + TR söz kartı + RU/EN söz kartı). |

---

## STRATEJİ PLANI — yeni gönderiler (d cevabı, uygulamaya hazır)

**Hedef:** 4–6 haftada ilk test havuzu duvarını (≈300) kırıp 1k–10k bandına
düzenli oturmak; ses döngüsünü başlatmak; tek isabetle 50k+ denemek.

### Hafta düzeni (haftada 4 gönderi, toplam üretim ~2-3 saat/hafta)

- **Salı 17:00 TR — ANA SÖZ VİDEOSU** (benim-10 şablonu, 30–45 sn):
  0,0 sn nakarat + yüz/sahne tam kurulu + kelime kelime sarı karaoke söz +
  kalıcı ince soru overlay + son 5 sn "kaydet 🎧 takip et". Her hafta farklı
  şarkı; aynı görsel düzen (marka tanınırlığı).
- **Çarşamba 20:00 TR — SLAYT KARTI** (viral-4 kalıbı, üretim 15 dk):
  3 kart: (1) estetik kapak + tersleme cümlesi ("sadece bir şarkı…" tipi),
  (2) TR söz kartı, (3) aynı görselde EN veya RU çeviri. Ses: o haftaki şarkı.
- **Cuma 17:00 TR — DİYALOG/SKEÇ** (benim-7 konsepti, 20–30 sn):
  Üfle Söndür tipi sahne; nakarat 0,0 sn'de; soru üstte kalıcı.
- **Pazar 20:00 TR — SERİ İÇERİK dönüşümlü:**
  (i) "menü" videosu (11 şarkı × 8 sn afiş — retrobesto kalıbı, ayda 1),
  (ii) AI A/B sorusu (benim-12 serisi),
  (iii) sosyal kanıt denemesi (sahne/prova görüntüsü + "bu nakarat kafamdan
  çıkmıyor" tipi izleyici ağzından overlay — viral-14 kalıbı).

### Kitle köprüsü (SE→TR sorununun çözümü)

- Her ana videoda **ikinci dil katmanı**: hedef kitleye göre TR+EN (global) ya
  da TR+RU (Antalya/diaspora hattı denemesi) — viral-3/10 kanıtı.
- Etiket şablonu (hile etiketleri yok): `#hasanca #türkçepop #şarkısözleri
  #damar|#poparabesk (tür) + #yenişarkı|şarkı adı` + slaytlarda yer/dil
  etiketi (#türkiye, #turkishmusic; RU denemesinde #турция #песня).
- Bio'ya güncel single satırı zaten var ✓; "OUT NOW" formatına çevir.

### Ses döngüsü

- Her şarkıyı TEK adlandırılmış ses olarak yayınla ("Şarkı Adı - HasanCa",
  benim-14'teki gibi) ve sonraki tüm gönderilerde AYNI sesi kullan (bölünmüş
  "orijinal ses"ler sesin izlenme birikimini parçalıyor).
- Slayt ve skeç videoları "bu sese video çek" davranışını tetikleyecek kadar
  basit sahneler göstersin (araba camı + gece ışıkları + söz — viral-10'un
  taklit edilebilirliği).

### Lansman kurgusu (yeni şarkı çıkışlarında)

- Çıkıştan 7–10 gün önce: "GG.AA.2026 🖤 <Şarkı> çıkıyor" teaser'ı (viral-3).
- Çıkış günü: Pazartesi 00:30 TR "BUGÜN YAYINDA" + görev dili ("dinle, izle,
  paylaş — duyguma ortak ol", viral-7 kalıbı).
- Çıkış haftası: ana söz videosu + slayt + skeç aynı sesle art arda.

### Ölçüm ve karar kuralları

- Her gönderide 48 saat sonra bak: izlenme >600 mü (ilk havuz kırıldı mı),
  paylaşım/izlenme >%0,8 mi, tamamlanma (uygulama analitiği) >%60 mı.
- 4 hafta üst üste kıramayan format düşürülür; kıran format haftada 2'ye
  çıkarılır.
- Reklam SADECE organik kırılım yapan videoya, "spark" mantığıyla verilir;
  soğuk kreatife reklam yok (benim-13 kanıtı).
- Hassas içerik/erişim kontrolü: her gönderiden sonra gizli sekmeden linki
  aç — giriş duvarı görürsen (benim-3/4/6 durumu) gönderiyi uygulamadan
  kontrol et.

## 6. Eksiksizlik kontrol listesi

```
- [x] Her viral video için 1a + 1b + 1c tamam (17/18; viral-6 giriş duvarı nedeniyle erişilemedi, gerekçesi Bölüm 1B'de)
- [x] Her kullanıcı videosu için tam analiz + numaralı hata listesi (13/16 tam; benim-3/4/6 foto gönderileri anonim erişime kapalı — gerekçe Bölüm 2 girişinde, kontrol adımı Bölüm 5 tablosunda)
- [x] Karşılaştırma tablosu var (3A: kalıp vs kanal; 3B: viraller arası)
- [x] 10+ başlık (11), tam açıklama (3 platform), 30+ etiket (34)
- [x] Saniye saniye akış planı 0:00'dan 1:00'a kesintisiz
- [x] Süre, hook, CTA, efekt, yayın zamanı, kapak önerileri dolu
- [x] Her eski video için yeniden düzenleme planı (Bölüm 5 tablosu, 16 gönderi)
- [x] Kullanıcının a/b/c/d soruları doğrudan cevaplı (Bölüm 2 sonu + STRATEJİ PLANI)
- [x] Uygulanamayan maddelerin nedeni raporda açıkça yazılı
```

**Sonraki adım önerisi:** Kullanıcı karşılaştırılacak kendi videolarını (ör.
`HASANCA-Beni_en_iyi_sen_kirdin.mp4`) belirtsin; aynı protokolle `benim-N`
analizi yapılıp Bölüm 2, 3 ve 5 tamamlanır.
