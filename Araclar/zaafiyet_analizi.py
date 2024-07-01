#!/usr/bin/env python

import os

sistem = input("Dağıtımınızın altyapısı? Fedora(1) Debian (2): ")

if sistem == "1":
    os.system("sudo dnf install figlet")
    os.system("sudo dnf install nikto")
    os.system("clear")
    os.system("figlet ZAAFIYET ANALIZI")
    print("""
Zaafiyet Analizi Aracina Hosgeldin 
    """)
elif sistem == "2":
    os.system("sudo apt-get install figlet")
    os.system("sudo apt-get install nikto")
    os.system("clear")
    os.system("figlet ZAAFIYET ANALIZI")
    print("""
Zaafiyet Analizi Aracina Hosgeldin 
    """)
else:
    print("Geçersiz seçim!")
    exit()

hedefip = input("Hedef IP Girin: ")
os.system("nikto -h " + hedefip)
