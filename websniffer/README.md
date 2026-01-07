#  Network Sniffer

Python tabanlı, düşük seviyeli ağ paketlerini analiz eden ve gerçek zamanlı olarak ziyaret edilen web adreslerini (DNS) ayıklayan bir terminal aracıdır.

##  Özellikler
- **Real-time DNS Tracking:** Ağ üzerinden yapılan web sitesi sorgularını anlık yakalar.
- **Smart Filtering:** Google, Microsoft gibi arka plan servislerini filtreleyerek sadece kullanıcı trafiğine odaklanır.
- **Graceful Shutdown:** `signal` kütüphanesi ile güvenli çıkış ve Matrix tarzı veda mesajı.
- **Zero-GUI:** Tamamen terminal odaklı, hafif ve hızlı.

### Gereksinimler
- Python 3.x
- [Npcap](https://npcap.com/#download) (Windows için gereklidir)

### Kütüphanelerin Kurulumu
```bash
pip install scapy
