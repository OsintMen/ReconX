import socket
from concurrent.futures import ThreadPoolExecutor

COMMON_PORTS = [21,22,25,53,80,110,139,143,443,445,8080]

def scan_port(ip, port):
    try:
        sock = socket.socket()
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        sock.close()
        if result == 0:
            return port
    except:
        pass
    return None

def scan_ports(domain):
    try:
        ip = socket.gethostbyname(domain)
    except:
        return []

    open_ports = []
    with ThreadPoolExecutor(max_workers=25) as executor:
        results = executor.map(lambda p: scan_port(ip, p), COMMON_PORTS)

    for r in results:
        if r:
            open_ports.append(r)

    return open_ports