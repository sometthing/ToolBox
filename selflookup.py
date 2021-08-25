import socket
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
print(" - Devise name - : " + hostname)
print(" - Device IP - : " + IPAddr)
