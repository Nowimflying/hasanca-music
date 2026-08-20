"""Viral video analiz sistemi (API'siz).

YouTube / TikTok / Instagram linklerinden videolari indirir, 0.5
saniyede bir kare cikarip her karenin kosesine sira numarasi ve zaman
damgasi basar, metadata'yi (baslik, aciklama, etiket, yukleme
tarihi/saati, izlenme) kaydeder.

Analizin kendisi bir yapay zeka ajani (Claude Code, Codex vb.)
tarafindan oturum icinde yapilir: ajan kareleri gorsel olarak okur,
metadata'yi inceler ve ANALIZ_REHBERI.md'deki protokole gore EKSIKSIZ
rapor yazar. Harici bir LLM API cagrisi YOKTUR.
"""

__version__ = "2.0.0"
