import socket

ip = input("[+} Enter IP to scan for open ports: ")
print(' <+> This is the IP ' + ip + ' for scan <+> ')
rf = input("[+} Enter the start port: ")
print(" <+> This is the first port to start " + rf + ' <+> ')
rfi = int(rf)
rl = input("[+} Enter the last port for scan: ")
print(" <+> This is the last port for scan " + rl + " <+> ")
rli = int(rl)
port = range(rfi, rli)
print("""

@====-===---========------=======--===-------=====---===--@
| Port scanner for open ports (trusted zone for firewall) |
@--------===========------------==========-----------=====@

─────────────────────────────────────────────────────────────────
─██████████████─██████████████─████████████████───██████████████─
─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░░░██───██░░░░░░░░░░██─
─██░░██████░░██─██░░██████░░██─██░░████████░░██───██████░░██████─
─██░░██──██░░██─██░░██──██░░██─██░░██────██░░██───────██░░██─────
─██░░██████░░██─██░░██──██░░██─██░░████████░░██───────██░░██─────
─██░░░░░░░░░░██─██░░██──██░░██─██░░░░░░░░░░░░██───────██░░██─────
─██░░██████████─██░░██──██░░██─██░░██████░░████───────██░░██─────
─██░░██─────────██░░██──██░░██─██░░██──██░░██─────────██░░██─────
─██░░██─────────██░░██████░░██─██░░██──██░░██████─────██░░██─────
─██░░██─────────██░░░░░░░░░░██─██░░██──██░░░░░░██─────██░░██─────
─██████─────────██████████████─██████──██████████─────██████─────
─────────────────────────────────────────────────────────────────

$+++++++____+__+++________$
| Created by TheGhostRoot |
$_______+++++___++++++++++$


TOOLBOX WAS CREATED FOR EDUCATION PURPOSES ONLY. DON'T USE ANY OF THE TOOLS FOR MALICIOUS ACTIVITY. I AM NOT RESPONSIBLE FOR ANYTHING DONE BY ANY OF THOSE TOOLS. USE THEM AT YOUR OWN RISK!!!

""")

def portscan(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((ip, port))
        return True
    except:
        return False

for port in range(rfi, rli):
    result = portscan(port)
    if result:
        print(" <+> Port {} is open!".format(port) + ' <+> ')
    else:
        continue
