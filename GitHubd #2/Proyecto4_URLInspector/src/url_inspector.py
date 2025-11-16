import validators
import tldextract
import re
from colorama import Fore, Style, init

init(autoreset=True)

print("="*50)
print("          🔍 URL INSPECTOR v1.0")
print("="*50)

url = input("Ingresa la URL a analizar: ").strip()
print("\nAnalizando la URL...\n")

valid = validators.url(url)

print("\n===== RESULTADOS =====")

if not valid:
    print(f"{Fore.RED}✘ URL inválida o malformada")
else:
    print(f"{Fore.GREEN}✔ Formato de URL válido")

    ext = tldextract.extract(url)
    dominio = f"{ext.domain}.{ext.suffix}"

    patrones = [
        r"\d{5,}",
        r"(verify|update|secure|login)",
        r"\.zip$|\.exe$"
    ]

    sospechoso = False
    for p in patrones:
        if re.search(p, url, re.IGNORECASE):
            sospechoso = True
            break

    if not sospechoso:
        print(f"{Fore.GREEN}✔ No se detectaron patrones sospechosos")
    else:
        print(f"{Fore.RED}✘ Se detectaron patrones sospechosos")

print("\nAnálisis completado.\n")
