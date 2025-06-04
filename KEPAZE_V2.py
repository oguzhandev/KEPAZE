#!/usr/bin/env python

import os
import subprocess
import time

def readme():
    with open("README.txt", "r") as file:
        content = file.read()
        print(content)

def install_tools():
    sistem = input("Dağıtımınızın altyapısı? Fedora(1) Debian (2): ")
    if sistem == "1":
        os.system("sudo dnf install -y figlet ncrack nikto nmap wafw00f exploitdb")
        print("Gerekli araçlar Fedora sistemine yüklendi.")
    elif sistem == "2":
        os.system("sudo apt-get install -y figlet ncrack nikto nmap wafw00f exploitdb")
        print("Gerekli araçlar Debian sistemine yüklendi.")
    else:
        print("Geçersiz seçim!")

def main():
    print("KEPAZE_V1 Aracına Hoşgeldiniz!")
    
    language = input("Dil Seçimi / Language Selection (TR/EN): ").lower()
    if language == 'tr':
        readme_file = "README_TR.txt"
    elif language == 'en':
        readme_file = "README_EN.txt"
    else:
        print("Geçersiz seçim!")
        return
    
    with open(readme_file, "r") as file:
        content = file.read()
        print(content)

    tools_install = input("Gerekli araçları kurmak ister misiniz? (E/H): ").lower()
    if tools_install == 'e':
        install_tools()

    subprocess.run("clear", shell=True)
    subprocess.run("figlet KEPAZE V2", shell=True)
    time.sleep(1)
    print("""
https://github.com/oguzhandev

Lütfen Bir Seçim Yapınız!
1- Exploit Arama Aracı
2- Güvenlik Duvarı Tespit Aracı
3- Kaba Kuvvet Saldırı Aracı
4- Port Tarama Aracı
5- Wordlist Aracı
6- Zaafiyet Analizi
7- OSINT Aracı
8- Çıkış

""")

    anasecim = input("Lütfen Bir Seçim Yapınız: ")

    if anasecim == "1":
        subprocess.run("python Araclar/exploit_arama.py", shell=True)
    elif anasecim == "2":
        subprocess.run("python Araclar/guvenliktespit.py", shell=True)
    elif anasecim == "3":
        subprocess.run("python Araclar/kaba_kuvvet_saldiri.py", shell=True)
    elif anasecim == "4":
        subprocess.run("python Araclar/porttarama.py", shell=True)
    elif anasecim == "5":
        subprocess.run("python Araclar/wordlist.py", shell=True)
    elif anasecim == "6":
        subprocess.run("python Araclar/zaafiyet_analizi.py", shell=True)
    elif anasecim == "7":
        subprocess.run("python Araclar/osint_araci.py", shell=True)
    elif anasecim == "8":
        print("Programdan çıkılıyor...")
        exit()
    else:
        print("Hatalı seçim yaptınız. Programdan çıkılıyor...")

if __name__ == "__main__":
    main()
