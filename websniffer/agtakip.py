from scapy.all import sniff, DNS, DNSQR
import signal
import sys
import os

def cikis_yap(signum, frame):
    print("\n" + "="*50)
    print("Sistem kapatiliyor...")
    print("Goodbye, Neo.")
    print("="*50)
    sys.exit(0)

signal.signal(signal.SIGINT, cikis_yap)

print("="*50)
print(" WEB IZLEYICI AKTIF...")
print("Cikis yapmak icin 'Ctrl + C' tusuna basin.")
print("="*50)

gorulen_siteler = set()

def dns_callback(packet):
    if packet.haslayer(DNSQR):
        try:
            site_ismi = packet[DNSQR].qname.decode('utf-8').strip(".")
            
            gereksizler = ["google", "microsoft", "windows", "akamai"]
            if site_ismi not in gorulen_siteler and not any(x in site_ismi for x in gereksizler):
                print(f"[BAGLANTI] Hedef Site: {site_ismi}")
                gorulen_siteler.add(site_ismi)
        except:
            pass

sniff(filter="udp port 53", prn=dns_callback, store=0, promisc=True)