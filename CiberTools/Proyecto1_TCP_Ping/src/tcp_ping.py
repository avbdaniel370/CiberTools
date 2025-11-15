import socket
import time

def tcp_ping(host, port, attempts):
    for i in range(attempts):
        try:
            s = socket.socket()
            s.settimeout(2)
            start = time.time()
            s.connect((host, port))
            end = time.time()
            print(f"[{i+1}] Respuesta en { (end - start)*1000 :.2f} ms")
            s.close()
        except Exception as e:
            print(f"[{i+1}] Falló: {e}")

def main():
    host = input("Host: ")
    port = int(input("Puerto: "))
    attempts = int(input("Intentos: "))
    tcp_ping(host, port, attempts)

if __name__ == "__main__":
    main()