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
        os.system("sudo dnf install -y figlet ncrack nikto nmap wafw00f exploitdb python3-pip")
        os.system("pip3 install requests beautifulsoup4 pandas matplotlib scikit-learn networkx")
        print("Gerekli araçlar Fedora sistemine yüklendi.")
    elif sistem == "2":
        os.system("sudo apt-get install -y figlet ncrack nikto nmap wafw00f exploitdb python3-pip")
        os.system("pip3 install requests beautifulsoup4 pandas matplotlib scikit-learn networkx")
        print("Gerekli araçlar Debian sistemine yüklendi.")
    else:
        print("Geçersiz seçim!")

def main():
    print("KEPAZE_V2.2 Aracına Hoşgeldiniz!")
    
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
    subprocess.run("figlet KEPAZE V2.2", shell=True)
    time.sleep(1)
    print("""
https://github.com/oguzhandev

Ana Menü
1- Data Analytics
2- Siber Güvenlik
3- Çıkış

""")

    anasecim = input("Seçiminiz: ")

    if anasecim == "1":
        analytics_menu()
    elif anasecim == "2":
        security_menu()
    elif anasecim == "3":
        print("Programdan çıkılıyor...")
        exit()
    else:
        print("Hatalı seçim yaptınız. Programdan çıkılıyor...")

def analytics_menu():
    while True:
        print("\nDATA ANALYTICS")
        print("1- Gelişmiş Analiz")
        print("2- Sosyal Ağ Analizi")
        print("3- Geri")
        secim = input("Seçiminiz: ")
        if secim == "1":
            subprocess.run("python Araclar/gelismis_analiz.py", shell=True)
        elif secim == "2":
            subprocess.run("python Araclar/sosyal_ag_analizi.py", shell=True)
        elif secim == "3":
            break
        else:
            print("Geçersiz seçim")

def security_menu():
    while True:
        print("\nSİBER GÜVENLİK")
        print("1- Exploit Arama Aracı")
        print("2- Güvenlik Duvarı Tespit Aracı")
        print("3- Kaba Kuvvet Saldırı Aracı")
        print("4- Port Tarama Aracı")
        print("5- Wordlist Aracı")
        print("6- Zaafiyet Analizi")
        print("7- OSINT Aracı")
        print("8- Geri")
        secim = input("Seçiminiz: ")
        if secim == "1":
            subprocess.run("python Araclar/exploit_arama.py", shell=True)
        elif secim == "2":
            subprocess.run("python Araclar/guvenliktespit.py", shell=True)
        elif secim == "3":
            subprocess.run("python Araclar/kaba_kuvvet_saldiri.py", shell=True)
        elif secim == "4":
            subprocess.run("python Araclar/porttarama.py", shell=True)
        elif secim == "5":
            subprocess.run("python Araclar/wordlist.py", shell=True)
        elif secim == "6":
            subprocess.run("python Araclar/zaafiyet_analizi.py", shell=True)
        elif secim == "7":
            subprocess.run("python Araclar/osint_araci.py", shell=True)
        elif secim == "8":
            break
        else:
            print("Geçersiz seçim")

if __name__ == "__main__":
    main()
