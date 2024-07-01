#!/usr/bin/env python

import os

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

if __name__ == "__main__":
    install_tools()
