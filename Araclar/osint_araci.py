#!/usr/bin/env python
import os


def main():
    sistem = input("Dağıtımınızın altyapısı? Fedora(1) Debian (2): ")
    if sistem == "1":
        os.system("figlet OSINT ARACI")
    elif sistem == "2":
        os.system("apt-get install figlet")
        os.system("clear")
        os.system("figlet OSINT ARACI")
    else:
        print("Geçersiz seçim!")

    print("""
OSINT Aracına Hoşgeldiniz

1) whois
2) dnsrecon
3) theHarvester
""")

    secim = input("İşlem Numarasını Girin: ")

    if secim == "1":
        domain = input("Domain Adı: ")
        os.system(f"whois {domain}")
    elif secim == "2":
        domain = input("Domain Adı: ")
        os.system(f"dnsrecon -d {domain}")
    elif secim == "3":
        domain = input("Domain Adı: ")
        os.system(f"theHarvester -d {domain} -b all")
    else:
        print("Geçersiz Seçim")


if __name__ == "__main__":
    main()
