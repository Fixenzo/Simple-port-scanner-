import socket
ip = input("IP target: ")
for port in range(1, 100):
    sock = socket.socket()
    sock.settimeout(0.5)
    if sock.connect_ex((ip, port)) == 0:
        print(f"Port {port} terbuka")
    sock.close()