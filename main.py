import socket

def ping(ip: str, port: int) -> bool:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)
        sock.connect((ip, port))
        sock.close()
        return True
    except socket.error:
        return False

with open("servers_ip.txt", "r") as f:
    servers_raw = f.read()

servers_list = servers_raw.split("\n")

for server in servers_list:
    ip,port = server.split(":")
    print(f"{ip:<15}:{port} | {ping(ip,int(port))}")
