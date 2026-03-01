from scapy.all import *
import socket

def quick_scan(ip):
    """Scansione porte comuni su qualsiasi IP"""
    print(f"\n\033[93m[SCAN] Controllo porte su: {ip}\033[0m")
    common_ports = [80, 443, 8080, 21, 22, 3389]
    for port in common_ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.3)
        if s.connect_ex((ip, port)) == 0:
            print(f"  \033[92m>> Porta {port}: APERTA\033[0m")
        s.close()

def monitor_all_traffic(pkt):
    """Mostra tutto il traffico IP rilevato"""
    if IP in pkt:
        src = pkt[IP].src
        dst = pkt[IP].dst
        print(f"\033[97m[INFO] {src} \033[94m-->\033[97m {dst}\033[0m")
