import socket
import ssl
import time

def get_headers(host):
    ctx = ssl.create_default_context()
    s = ctx.wrap_socket(socket.socket(), server_hostname=host)
    s.settimeout(3)

    start = time.time()
    s.connect((host, 443))
    elapsed = (time.time() - start) * 1000

    s.send(b"GET / HTTP/1.1\r\nHost: " + host.encode() + b"\r\n\r\n")
    data = s.recv(4096).decode(errors="ignore")
    s.close()

    return data, elapsed

def analyze(headers):
    result = []
    if "Strict-Transport-Security" in headers:
        result.append("✔ HSTS presente")
    else:
        result.append("⚠ HSTS no detectado")

    if "X-Frame-Options" in headers:
        result.append("✔ XFO presente")
    else:
        result.append("⚠ Falta X-Frame-Options")

    if "Content-Security-Policy" in headers:
        result.append("✔ CSP presente")
    else:
        result.append("⚠ Falta CSP")

    return result

def main():
    host = input("Sitio a analizar (ej: google.com): ")

    print("\n🔍 Recuperando cabeceras HTTPS...\n")
    data, tls = get_headers(host)

    print("===== CABECERAS =====\n")
    print(data)

    print("\n===== ANÁLISIS DE SEGURIDAD =====")
    for r in analyze(data):
        print(r)

    print(f"\nTiempo TLS: {tls:.2f} ms")

if __name__ == "__main__":
    main()