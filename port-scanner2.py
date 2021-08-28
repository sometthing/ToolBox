import socket
import threading
import concurrent.futures
import colorama
from colorama import Fore
colorama.init()

print_lock = threading.Lock()

print("""

%<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>%
| Port scanner for open port (trusted zone for firewall) |
%---=======------======---------======-------------------%

█▀▀█ █▀▀█ █▀▀█ ▀▀█▀▀ 
█──█ █──█ █▄▄▀ ──█── 
█▀▀▀ ▀▀▀▀ ▀─▀▀ ──▀──

!^^^^+++++++++^^^^^^++^^^^!
| Created by TheGhostRoot |
!^+^^^^^^^+++++++++^^^^^^^!

""")

ip = input("[+} Enter IP to scan for open ports: ")
print(' <+> This is the IP ' + ip + ' for scan <+> ')
rf = input("[+} Enter the start port: ")
print(" <+> This is the first port to start " + rf + ' <+> ')
rfi = int(rf)
rl = input("[+} Enter the last port for scan: ")
print(" <+> This is the last port for scan " + rl + " <+> ")
rli = int(rl)

def scan(ip, port):
    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scanner.settimeout(1)
    try:
        scanner.connect((ip, port))
        scanner.close()
        with print_lock:
            print(" <+> " + Fore.WHITE + f"[{port}]" + Fore.GREEN + " Opened <+> ")
    except:
        pass

with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
    for port in range(rfi, rli):
        executor.submit(scan, ip, port + 1)
