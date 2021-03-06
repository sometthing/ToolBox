import nmap3
import os
import time
from colorama import Fore, Back, Style

nmap = nmap3.Nmap()
nmapT = nmap3.NmapScanTechniques()
nmapH = nmap3.NmapHostDiscovery()

i = nmapH.arp_discovery
print("ARP is " + i)
o = nmapH.nmaptool
print("Nmap is at " + o)
print(Style.DIM)
g = ("""TARGET SPECIFICATION:
                  - iL < inputfilename >: Input from list of hosts/networks
                  - iR < num hosts >: Choose random targets
                  - -exclude < host1[, host2][, host3], ... > : Exclude hosts/networks
                  - -excludefile < exclude_file >: Exclude list from file
            HOST DISCOVERY:
                  -sL: List Scan - simply list targets to scan
                  - sn: Ping Scan - disable port scan
                  - Pn: Treat all hosts as online - - skip host discovery
                  - PS/PA/PU/PY[portlist]: TCP SYN/ACK, UDP or SCTP discovery to given ports
                  - PE/PP/PM: ICMP echo, timestamp, and netmask request discovery probes
                  - PO[protocol list]: IP Protocol Ping
                  - n/-R: Never do DNS resolution/Always resolve[default: sometimes]
                  - -dns-servers < serv1[, serv2], ... >: Specify custom DNS servers
                  - -system-dns: Use OS's DNS resolver
                  - -traceroute: Trace hop path to each host
            SCAN TECHNIQUES:
                  -sS/sT/sA/sW/sM: TCP SYN/Connect()/ACK/Window/Maimon scans
                  - sU: UDP Scan
                  - sN/sF/sX: TCP Null, FIN, and Xmas scans
                  - -scanflags < flags >: Customize TCP scan flags
                  - sI < zombie host[:probeport] >: Idle scan
                  - sY/sZ: SCTP INIT/COOKIE-ECHO scans
                  - sO: IP protocol scan
                  - b < FTP relay host >: FTP bounce scan
            PORT SPECIFICATION AND SCAN ORDER:
                  -p < port ranges > : Only scan specified ports
                  Ex: -p22
                  - p1-65535
                  - p U: 53, 111, 137, T: 21-25, 80, 139, 8080, S: 9
                  - -exclude-ports < port ranges >: Exclude the specified ports from scanning
                  - F: Fast mode - Scan fewer ports than the default scan
                  - r: Scan ports consecutively - don't randomize
                  - -top-ports < number >: Scan < number > most common ports
                  - -port-ratio < ratio >: Scan ports more common than < ratio >
            SERVICE/VERSION DETECTION:
                  -sV: Probe open ports to determine service/version info
                  - -version-intensity < level >: Set from 0 (light) to 9 (try all probes)
                  - -version-light: Limit to most likely probes(intensity 2)
                  - -version-all: Try every single probe(intensity 9)
                  - -version-trace: Show detailed version scan activity(for debugging)
            SCRIPT SCAN:
                  -sC: equivalent to - -script=default
                  - -script= < Lua scripts > : < Lua scripts > is a comma separated list of
                  directories, script-files or script-categories
                  - -script-args= < n1=v1, [n2=v2, ...] > : provide arguments to scripts
                  - -script-args-file=filename: provide NSE script args in a file
                  - -script-trace: Show all data sent and received
                  - -script-updatedb: Update the script database.
                  --script-help= < Lua scripts >: Show help about scripts.
                  < Lua scripts > is a comma-separated list of script-files or
                  script-categories.
            OS DETECTION:
                  -O: Enable OS detection
                  - -osscan-limit: Limit OS detection to promising targets
                  - -osscan-guess: Guess OS more aggressively
            TIMING AND PERFORMANCE:
                  Options which take < time > are in seconds, or append 'ms' (milliseconds),
                  's' (seconds), 'm' (minutes), or 'h' (hours) to the value(e.g. 30m).
                  -T < 0-5 >: Set timing template (higher is faster)
                  - -min-hostgroup/max-hostgroup < size >: Parallel host scan group sizes
                  - -min-parallelism/max-parallelism < numprobes >: Probe parallelization
                  - -min-rtt-timeout/max-rtt-timeout/initial-rtt-timeout < time >: Specifies
                  probe round trip time.
                  --max-retries < tries > : Caps number of port scan probe retransmissions.
                  --host-timeout < time > : Give up on target after this long
                  - -scan-delay/--max-scan-delay < time >: Adjust delay between probes
                  - -min-rate < number >: Send packets no slower than < number > per second
                  - -max-rate < number >: Send packets no faster than < number > per second
            FIREWALL/IDS EVASION AND SPOOFING:
                  -f
                  - -mtu < val > : fragment packets (optionally w/given MTU)
                  - D < decoy1, decoy2[, ME], ... > : Cloak a scan with decoys
                  - S < IP_Address >: Spoof source address
                  - e < iface >: Use specified interface
                  - g/--source-port < portnum >: Use given port number
                  - -proxies < url1, [url2], ... >: Relay connections through HTTP/SOCKS4 proxies
                  - -data < hex string >: Append a custom payload to sent packets
                  - -data-string < string >: Append a custom ASCII string to sent packets
                  - -data-length < num >: Append random data to sent packets
                  - -ip-options < options >: Send packets with specified ip options
                  - -ttl < val >: Set IP time-to-live field
                  - -spoof-mac < mac address/prefix/vendor name >: Spoof your MAC address
                  - -badsum: Send packets with a bogus TCP/UDP/SCTP checksum
            OUTPUT:
                  -oN/-oX/-oS/-oG < file > : Output scan in normal, XML, s|<rIpt kIddi3,
                  and Grepable format, respectively, to the given filename.
                  -oA < basename > : Output in the three major formats at once
                  - v: Increase verbosity level(use - vv or more for greater effect)
                  - d: Increase debugging level(use - dd or more for greater effect)
                  - -reason: Display the reason a port is in a particular state
  - -open: Only show open ( or possibly open) ports
                  - -packet-trace: Show all packets sent and received
                  - -iflist: Print host interfaces and routes(for debugging)
                  - -append-output: Append to rather than clobber specified output files
                  - -resume < filename >: Resume an aborted scan
                  - -stylesheet < path/URL >: XSL stylesheet to transform XML output to HTML
                  - -webxml: Reference stylesheet from Nmap.Org for more portable XML
                  - -no-stylesheet: Prevent associating of XSL stylesheet w/XML output
            MISC:
                  -6: Enable IPv6 scanning
                  - A: Enable OS detection, version detection, script scanning, and traceroute
                  - -datadir < dirname >: Specify custom Nmap data file location
                  - -send-eth/--send-ip: Send using raw ethernet frames or IP packets
                  - -privileged: Assume that the user is fully privileged
                  - -unprivileged: Assume the user lacks raw socket privileges
                  - V: Print version number
                  - h: Print this help summary page.
            EXAMPLES:
                  nmap - v - A scanme.nmap.org
                  nmap - v - sn 192.168.0.0/16 10.0.0.0/8
                  nmap - v - iR 10000 - Pn - p 80
                  SEE THE MAN PAGE(https: // nmap.org/book/man.html) FOR MORE OPTIONS AND EXAMPLES
                  """)
print(Fore.RED + """

@----=======--------=====-------@
| Nmap (network mapper) scanner |
@---============--------======--@


 ????????????    ???  ???????????? ??????????????? ?????????       ??????????????????  
 ?????? ??????   ??? ????????????????????? ???????????????????????????    ????????????  ?????????
?????????  ?????? ??????????????????    ?????????????????????  ?????????  ???????????? ????????????
????????????  ????????????????????????    ????????? ??????????????????????????? ????????????????????? ???
????????????   ????????????????????????   ???????????? ??????   ???????????????????????? ???  ???
??? ??????   ??? ??? ??? ??????   ???  ??? ??????   ???????????????????????? ???  ???
??? ??????   ??? ?????????  ???      ???  ???   ?????? ????????? ???     
   ???   ??? ??? ???      ???     ???   ???   ??????       
         ???        ???         ???  ???         
                                         


Created by 
  _______   __              _______   __                      __     _______                   __   
 |       | |  |--. .-----. |   _   | |  |--. .-----. .-----. |  |_  |   _   \ .-----. .-----. |  |_ 
 |.|   | | |     | |  -__| |.  |___| |     | |  _  | |__ --| |   _| |.  l   / |  _  | |  _  | |   _|
 `-|.  |-' |__|__| |_____| |.  |   | |__|__| |_____| |_____| |____| |.  _   1 |_____| |_____| |____|
   |:  |                   |:  1   |                                |:  |   |                       
   |::.|                   |::.. . |                                |::.|:. |                       
   `---'                   `-------'                                `--- ---'                       


TOOLBOX WAS CREATED FOR EDUCATION PURPOSES ONLY. DON'T USE ANY OF THE TOOLS FOR MALICIOUS ACTIVITY. I AM NOT RESPONSIBLE FOR ANYTHING DONE BY ANY OF THOSE TOOLS. USE THEM AT YOUR OWN RISK!!!

""")
print(Fore.RESET)
time.sleep(2)
ver = nmap.nmap_version()
ip = input(Fore.RED + " {<[?]>} Enter IP or website " + Fore.BLUE + "[example: youtube.com]" + Fore.RED + " for scan " + Fore.RED + ">}> " + Fore.MAGENTA)
print(Fore.RESET)
print(Fore.YELLOW + " /{<!>}\ You entered this IP or web " + Fore.MAGENTA + ip + Fore.YELLOW +" for scan /{<!>}\ ")
print(Fore.RESET)
time.sleep(1)
s = input(Fore.RED + " {<[?]>} Do you want SYN Stealth Scan? " + Fore.BLUE + "[Y/N]" + Fore.RED + " >}> " + Fore.BLUE)
print(Fore.RESET)
if s == 'y':
    print(Fore.RED + " /{<->}\ Please enter Y /{<->}\ ")
    print(Fore.RESET)
if s == 'n':
    print(Fore.RED + " /{<->}\ Please enter N /{<->}\ ")
    print(Fore.RESET)
if s == 'Y':
    print(Fore.GREEN + " /{<+>}\ You choosed YES /{<+>}\ ")
    print(Fore.RESET)
    time.sleep(1)
    resp = input(Fore.YELLOW + """
    \n {<[!]>} Type of scan SYN Stealth: """ + Fore.BLUE + """
    +====-====-======-======-======+ """ + Fore.CYAN + """
    > 1) Nmap version
    > 2) Intense scan
    > 3) Intense scan plus UDP
    > 4) Intense scan, all TCP ports
    > 5) Intense scan, no ping
    > 6) Quick scan
    > 7) Quick scan plus
    > 8) Regular scan
    > 9) Slow comprehensive scan
    > 10) Custom scan
    > 11) Nmap help
    > 12) Find OS
    > 13) Full scan
    > 14) Target vuln scan """ + Fore.BLUE + """
    <-----.---------.---------.--------.-------.------> """ + Fore.RED + """
    {<[?]>} Choose a option: """ + Fore.MAGENTA)
    print(Fore.RESET)
    ver = nmap.nmap_version()
    y = Fore.YELLOW + ' /{<!>}\ You choosed '
    print(Fore.RESET)
    if resp == '1':
        print( ver)
    if resp == '2':
        print(y + 'Intense scan /{<!>}\ ')
        print(Fore.RESET)
        time.sleep(1)
        print(Fore.RED + "nmap -sS -T4 -A -v " + Fore.MAGENTA + ip + Fore.RED)
        time.sleep(1)
        os.system("nmap -sS -T4 -A -v " + ip)
        print(Fore.RESET)
    if resp == '3':
        print(y + 'Intense scan plus UDP /{<!>}\ ')
        print(Fore.RESET)
        time.sleep(1)
        print(Fore.RED + "nmap -sS -sU -T4 -A -v " + Fore.MAGENTA + ip + Fore.RED)
        time.sleep(1)
        os.system("nmap -sS -sU -T4 -A -v " + ip)
        print(Fore.RESET)
    if resp == '4':
        print(y + 'Intense scan, all TCP ports /{<!>}\ ')
        print(Fore.RESET)
        time.sleep(1)
        print(Fore.RED + "nmap -sS -p 1-65535 -T4 -A -v " + Fore.MAGENTA + ip + Fore.RED)
        time.sleep(1)
        os.system("nmap -sS -p 1-65535 -T4 -A -v " + ip)
        print(Fore.RESET)
    if resp == '5':
        print(y + 'Intense scan, no ping /{<!>}\ ')
        print(Fore.RESET)
        time.sleep(1)
        print(Fore.RED + "nmap -sS -T4 -A -v -Pn " + Fore.MAGENTA + ip + Fore.RED)
        time.sleep(1)
        os.system("nmap -sS -T4 -A -v -Pn " + ip)
        print(Fore.RESET)
    if resp == '6':
        print(y + 'Quick scan /{<!>}\ ')
        print(Fore.RESET)
        time.sleep(1)
        print(Fore.RED + "nmap -sS -T4 -F " + Fore.MAGENTA + ip + Fore.RED)
        time.sleep(1)
        os.system("nmap -T4 -F " + ip)
        print(Fore.RESET)
    if resp == '7':
        print(y + 'Quick scan plus /{<!>}\ ')
        print(Fore.RESET)
        time.sleep(1)
        print(Fore.RED + "nmap -sS -sV -T4 -O -F --version-light " + Fore.MAGENTA + ip + Fore.RED)
        time.sleep(1)
        os.system("nmap -sS -sV -T4 -O -F --version-light " + ip)
        print(Fore.RESET)
    if resp == '8':
        print(y + 'Regular scan /{<!>}\ ')
        print(Fore.RESET)
        time.sleep(1)
        print(Fore.RED + "nmap -sS " + Fore.MAGENTA + ip + Fore.RED)
        time.sleep(1)
        os.system("nmap -sS " + ip)
        print(Fore.RESET)
    if resp == '9':
        print(y + 'Slow comprehensive scan /{<!>}\ ')
        print(Fore.RESET)
        time.sleep(1)
        print(Fore.RED + 'nmap -sS -sU -T4 -A -v -PE -PP -PS80,443 -PA3389 -PU40125 -PY -g 53 --script "default or (discovery and safe)" ' + Fore.MAGENTA + ip + Fore.RED)
        time.sleep(1)
        os.system('nmap -sS -sU -T4 -A -v -PE -PP -PS80,443 -PA3389 -PU40125 -PY -g 53 --script "default or (discovery and safe)" ' + ip)
        print(Fore.RESET)
    if resp == '10':
        print(y + 'Custom scan /{<!>}\ ')
        time.sleep(1)
        print(Fore.RESET)
        p = nmapT.default_args
        print(p)
        cs = input(Fore.RED + " {<[?]>} Enter custom scan without puting " + Fore.YELLOW + "nmap" + Fore.RED + " at the start and without puting the IP at the end >}> ")
        print(Fore.RESET)
        print(Fore.RED + 'nmap -sS ' + Fore.BLUE + cs + " " + Fore.MAGENTA + ip + Fore.RED)
        time.sleep(1)
        os.system('nmap -sS ' + cs + " " + ip)
        print(Fore.RESET)
    if resp == '11':
        print(y + 'Nmap help menu /{<!>}\ ')
        print(Fore.RESET)
        time.sleep(1)
        print(Fore.RED + g)
        print(Fore.RESET)
    if resp == '12':
        print(y + "to find target OS system /{<!>}\ ")
        print(Fore.RESET)
        time.sleep(1)
        print(Fore.RED + "nmap -sS -O " + Fore.MAGENTA + ip + Fore.RED)
        os.system("nmap -sS -O " + ip)
        print(Fore.RESET)
    if resp == '13':
        print(y + "full scan with /{<!>}\ ")
        print(Fore.RESET)
        time.sleep(1)
        print(Fore.RED + "nmap -sS -A " + Fore.MAGENTA + ip + Fore.RED)
        os.system("nmap -sS -A " + ip)
        print(Fore.RESET)
    if resp == '14':
        print(y + "Target vuln scan /{<!>}\ ")
        print(Fore.RESET)
        time.sleep(1)
        print(Fore.RED + "nmap --script vuln " + Fore.MAGENTA + ip + Fore.RED)
        time.sleep
        os.system("nmap --script vuln " + ip)
        print(Fore.RESET)
if s == 'N':
    print(Fore.YELLOW + " /{<!>}\ You selected " + Fore.BLUE + "NO" + Fore.YELLOW + " /{<!>}\ ")
    print(Fore.RESET)
    time.sleep(1)
    respn = input(Fore.YELLOW + """
    \n /{<!>}\ Type of scan: """ + Fore.BLUE + """
    +====-====-======-======-======+ """ + Fore.CYAN + """
    > 1) Nmap version
    > 2) Intense scan
    > 3) Intense scan plus UDP
    > 4) Intense scan, all TCP ports
    > 5) Intense scan, no ping
    > 6) Ping scan
    > 7) Quick scan
    > 8) Quick scan plus
    > 9) Quick traceroute
    > 10) Regular scan
    > 11) Slow comprehensive scan
    > 12) Custom scan
    > 13) Nmap help
    > 14) IP range
    > 15) Find OS
    > 16) Full scan
    > 17) Target vuln scan
    > 18) Fin scan """ + Fore.BLUE + """
    <-----.---------.---------.--------.-------.------> """ + Fore.RED + """
    {<[?]>} Choose a option >}> """ + Fore.MAGENTA)
    print(Fore.RESET)
    ver = nmap.nmap_version()
    y = Fore.YELLOW + ' /{<!>}\ You choose '
    print(Fore.RESET)
    if respn == '1':
        print(ver)
    if respn == '2':
        print(y + 'Intense scan /{<!>}\ ')
        print(Fore.RESET)
        time.sleep(1)
        print(Fore.RED + "nmap -T4 -A -v " + Fore.MAGENTA + ip + Fore.RED)
        time.sleep(1)
        os.system("nmap -T4 -A -v " + ip)
        print(Fore.RESET)
    if respn == '3':
        print(y + 'Intense scan plus UDP /{<!>}\ ')
        print(Fore.RESET)
        time.sleep(1)
        print(Fore.RED + "nmap -sU -T4 -A -v " + Fore.MAGENTA + ip + Fore.RED)
        time.sleep(1)
        os.system("nmap -sU -T4 -A -v " + ip)
        print(Fore.RESET)
    if respn == '4':
        print(y + 'Intense scan, all TCP ports /{<!>}\ ')
        print(Fore.RESET)
        time.sleep(1)
        print(Fore.RED + "nmap -p 1-65535 -T4 -A -v " + Fore.MAGENTA + ip + Fore.RED)
        time.sleep(1)
        os.system("nmap -p 1-65535 -T4 -A -v " + ip)
        print(Fore.RESET)
    if respn == '5':
        print(y + 'Intense scan, no ping /{<!>}\ ')
        print(Fore.RESET)
        time.sleep(1)
        print(Fore.RED + "nmap -T4 -A -v -Pn " + Fore.MAGENTA + ip + Fore.RED)
        time.sleep(1)
        os.system("nmap -T4 -A -v -Pn " + ip)
        print(Fore.RESET)
    if respn == '6':
        print(y + 'Ping scan /{<!>}\ ')
        print(Fore.RESET)
        time.sleep(1)
        print(Fore.RED + "nmap -sn " + Fore.MAGENTA + ip + Fore.RED)
        time.sleep(1)
        os.system("nmap -sn " + ip)
        print(Fore.RESET)
    if respn == '7':
        print(y + 'Quick scan /{<!>}\ ')
        print(Fore.RESET)
        time.sleep(1)
        print(Fore.RED + "nmap -T4 -F " + Fore.MAGENTA + ip + Fore.RED)
        time.sleep(1)
        os.system("nmap -T4 -F " + ip)
        print(Fore.RESET)
    if respn == '8':
        print(y + 'Quick scan plus /{<!>}\ ')
        print(Fore.RESET)
        time.sleep(1)
        print(Fore.RED + "nmap -sV -T4 -O -F --version-light " + Fore.MAGENTA + ip + Fore.RED)
        time.sleep(1)
        os.system("nmap -sV -T4 -O -F --version-light " + ip)
        print(Fore.RESET)
    if respn == '9':
        print(y + 'Quick traceroute /{<!>}\ ')
        print(Fore.RESET)
        time.sleep(1)
        print(Fore.RED + "nmap -sn --traceroute " + Fore.MAGENTA + ip + Fore.RED)
        time.sleep(1)
        os.system("nmap -sn --traceroute " + ip)
        print(Fore.RESET)
    if respn == '10':
        print(y + 'Regular sca /{<!>}\ ')
        print(Fore.RESET)
        time.sleep(1)
        print(Fore.RED + "nmap " + Fore.MAGENTA + ip + Fore.RED)
        time.sleep(1)
        os.system("nmap " + ip)
        print(Fore.RESET)
    if respn == '11':
        print(y + 'Slow comprehensive scan /{<!>}\ ')
        print(Fore.RESET)
        time.sleep(1)
        print(Fore.RED + 'nmap -sU -T4 -A -v -PE -PP -PS80,443 -PA3389 -PU40125 -PY -g 53 --script "default or (discovery and safe)" ' + Fore.MAGENTA + ip + Fore.RED)
        time.sleep(1)
        os.system('nmap -sU -T4 -A -v -PE -PP -PS80,443 -PA3389 -PU40125 -PY -g 53 --script "default or (discovery and safe)" ' + ip)
        print(Fore.RESET)
    if respn == '12':
        print(y + 'Custom scan /{<!>}\ ')
        print(Fore.RESET)
        time.sleep(1)
        p = nmapT.default_args
        print(p)
        csn = input(Fore.RED + " {<[?]>} Enter swich options for scan without puting " + Fore.YELLOW + "nmap" + Fore.RED + " at the start and without puting the " + Fore.YELLOW + "ip" + Fore.RED + " at the end >}> " + Fore.BLUE)
        print(Fore.RED + 'nmap ' + Fore.BLUE + csn + Fore.RED + " " + Fore.MAGENTA + ip + Fore.RED)
        time.sleep(1)
        os.system('nmap ' + csn + " " + ip)
        print(Fore.RESET)
    if respn == '13':
        print(y + 'Nmap help /{<!>}\ ')
        print(Fore.RESET)
        time.sleep(1)
        print(Fore.RED + g)
        print(Fore.RESET)
    if respn == '14':
        print(y + "IP range /{<!>}\ ")
        print(Fore.RESET)
        time.sleep(1)
        nw = input(Fore.RED + " {<[?]>} Enter IP for scan " + Fore.BLUE + "[example: hostIP/range]" + Fore.RED + " >}> " + Fore.BLUE)
        print(Fore.YELLOW + " /{<!>}\ You entered " + Fore.BLUE + nw + Fore.YELLOW + " /{<!>}\ ")
        print(Fore.RESET)
        print(Fore.RED + "nmap -sP " + Fore.MAGENTA + nw + Fore.RED)
        time.sleep(1)
        os.system("nmap -sP " + nw)
        print(Fore.RESET)
    if respn == '15':
        print(y + "to find target OS system /{<!>}\ ")
        print(Fore.RESET)
        time.sleep(1)
        print(Fore.RED + "nmap -O " + Fore.MAGENTA + ip + Fore.RED)
        time.sleep(1)
        os.system("nmap -O " + ip)
        print(Fore.RESET)
    if respn == '16':
        print(y + "full scan /{<!>}\ ")
        print(Fore.RESET)
        time.sleep(1)
        print(Fore.RED + "nmap -A " + Fore.MAGENTA + ip + Fore.RED)
        time.sleep(1)
        os.system("nmap -A " + ip)
        print(Fore.RESET)
    if respn == '17':
        print(y + "Target vuln scan /{<!>}\ ")
        print(Fore.RESET)
        time.sleep(1)
        print(Fore.RED + "nmap --script vuln " + Fore.MAGENTA + ip + Fore.RED)
        time.sleep(1)
        os.system("nmap --script vuln " + ip)
        print(Fore.RESET)
    if respn == '18':
        print(y + "Fin scan /{<!>}\ ")
        print(Fore.RESET)
        time.sleep(1)
        print(Fore.RED + "nmap -sF " + Fore.MAGENTA + ip + Fore.RED)
        time.sleep(1)
        os.system("nmap -sF " + ip)
        print(Fore.RESET)
