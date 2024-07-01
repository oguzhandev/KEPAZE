#!/usr/bin/env python

import os 

sistem = input("Dağıtımınızın altyapısı? Fedora(1) Debian (2): ")
if sistem == "1":

    os.system("figlet PORT TARAMA R00T")
    print("""

    Port Tarama Aracına Hosgeldin!

1) Hizli Tarama
2) Servis Versiyon Bilgisi
3) Isletim Sistemi Bilgisi 
    """) 
elif(sistem=="2"):

   os.system("apt-get install figlet")
   os.system("clear")
   os.system("figlet PORT TARAMA R00T")
   print("""

   Port Tarama Aracına Hosgeldin!

1) Hizli Tarama
2) Servis Versiyon Bilgisi
3) Isletim Sistemi Bilgisi 
   """) 
else:
    print("Geçersiz seçim!")



islemno = input("Islem Numarasini Girin: ")

if(islemno=="1"):
    hedefip = input("Hedef Ip Girin: ")
    os.system("nmap " + hedefip)
elif(islemno=="2"):
    hedefip = input ("Hedef Ip Girin: ")
    os.system("nmap -sS -sV " + hedefip)
elif(islemno=="3"):
    hedefip = input ("Hedef Ip Girin: ")
    os.system("nmap -0 " + hedefip)
else:

    print("Hatali Secim :(")






