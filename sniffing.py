from scapy.all import *
import socket

def quick_scan(ip):
    print(f"\n[SCAN] Avvio scansione rapida su: {ip}")
    # Porte comuni da controllare (80=HTTP, 443=HTTPS, 8080=Proxy, etc.)
    common_ports = [80, 443, 8080, 5222, 17500]
    for port in common_ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5) # Veloce, per non bloccare lo sniffer
        result = s.connect_ex((ip, port))
        if result == 0:
            print(f"  >> Porta {port}: APERTA")
        s.close()
    print("[SCAN] Completato.\n")

def monitor_with_scan(pkt):
    if IP in pkt:
        dst = pkt[IP].dst
        # Se l'IP è quello cinese che hai trovato nei log
        if dst == "103.235.46.102":
            print(f"!!! RILEVATO TRAFFICO VERSO BAIDU ({dst}) !!!")
            quick_scan(dst)

# Avvio
print("--- MONITORAGGIO + SCAN ATTIVO ---")
sniff(filter="ip", prn=monitor_with_scan, store=0)