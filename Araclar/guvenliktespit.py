#!/usr/bin/env python

import os 




sistem = input("Dağıtımınızın altyapısı? Fedora(1) Debian (2): ")
if sistem == "1":
    os.system("dnf install figlet")
    os.system("clear")
    os.system("figlet GUVENLIK DUVARI TESPIT R00T")
    print("""

   Guvenlik Duvari Tespit Araci R00T

    """) 
elif(sistem=="2"):

    os.system("apt-get install figlet")
    os.system("clear")
    os.system("figlet GUVENLIK DUVARI TESPIT R00T")
    print("""
    Guvenlik Duvari Tespit Araci R00T
          """)
else:
    print("Geçersiz seçim!")





site = input("Site Adresini Girin: ")
os.system("wafw00f -a " + site)

