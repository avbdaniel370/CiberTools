import socket

def scan_port(host, port):
    try:
        s = socket.socket()
        s.settimeout(0.5)
        s.connect((host, port))
        s.close()
        return True
    except:
        return False

def main():
    host = input("Host objetivo: ")
    start_port = int(input("Puerto inicial: "))
    end_port = int(input("Puerto final: "))

    print(f"\nEscaneando {host}...\n")

    for port in range(start_port, end_port + 1):
        if scan_port(host, port):
            print(f"⚡ Puerto {port} ABIERTO")
        else:
            print(f"· Puerto {port} cerrado")

if __name__ == "__main__":
    main()