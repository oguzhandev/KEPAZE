#!/usr/bin/env python

import os

def install_crunch_fedora():
    os.system("sudo dnf install -y glibc-devel.i686 libgcc.i686")
    os.system("git clone https://github.com/crunchsec/crunch")
    os.chdir("crunch")
    os.system("make")
    os.system("sudo make install")
    os.chdir("..")

def create_wordlist(minimum, maximum, karakter):
    os.system(f"crunch {minimum} {maximum} {karakter} -o temp_wordlist.txt")

def main():
    sistem = input("Dağıtımınızın altyapısı? Fedora(1) Debian (2): ")
    if sistem == "1":
        os.system("figlet Wordlist ARACI")
        print("""
Wordlist Olusturma Aracina Hosgeldin R00T
        """)
        install_crunch_fedora()
    elif sistem == "2":
        os.system("apt-get install figlet")
        os.system("clear")
        os.system("figlet PORT TARAMA R00T")
        print("""
Wordlist Olusturma Aracina Hosgeldin R00T
             """)
    else:
        print("Geçersiz seçim!")
        return

    os.system("clear")
    os.system("figlet WORLDLIST R00T")
    print("""
Wordlist Olusturma Aracina Hosgeldin R00T
    """)

    while True:
        print("1. Kombinasyon oluşturma")
        print("2. Kelime yazma ve kombinasyon ekleme")
        action_choice = input("Seçiminiz: ")

        if action_choice not in ['1', '2']:
            print("Geçersiz seçim!")
            continue

        print("Manuel karakter girişi (1) veya otomatik giriş (2) seçin:")
        char_input_choice = input("Seçiminiz: ")

        if char_input_choice == '1':
            karakter = input("İstediğiniz karakterleri girin: ")
        elif char_input_choice == '2':
            print("Otomatik giriş seçenekleri:")
            print("1. SAYILAR")
            print("2. KÜÇÜK HARFLER")
            print("3. BÜYÜK HARFLER")
            print("4. TÜM HARFLER")
            print("5. ÖZEL KARAKTERLER")
            print("6. TÜM KARAKTERLER")
            auto_choice = input("Seçiminiz: ")

            if auto_choice == '1':
                karakter = '0123456789'
            elif auto_choice == '2':
                karakter = 'abcdefghijklmnopqrstuvwxyz'
            elif auto_choice == '3':
                karakter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            elif auto_choice == '4':
                karakter = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
            elif auto_choice == '5':
                karakter = '!@#$%^&*()_+-=[]{}|;:,.<>?/~`'
            elif auto_choice == '6':
                karakter = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=[]{}|;:,.<>?/~`'
            else:
                print("Geçersiz seçim!")
                continue
        else:
            print("Geçersiz seçim!")
            continue

        if action_choice == '1':
            minimum = input("Minimum karakter sayısını girin: ")
            maximum = input("Maksimum karakter sayısını girin: ")
            create_wordlist(minimum, maximum, karakter)

            # Crunch çıktılarını ekrana yazdırma
            with open("temp_wordlist.txt", 'r') as file:
                for line in file:
                    print(line.strip())

            save_choice = input("Oluşturulan wordlist'i bir dosyaya kaydetmek ister misiniz? (E/H): ").lower()
            if save_choice == 'e':
                filename = input("Dosya adını girin (uzantı .txt olmalı): ")
                os.rename("temp_wordlist.txt", filename)
                print(f"Wordlist {filename} dosyasına kaydedildi.")
            else:
                os.remove("temp_wordlist.txt")
            print("Kombinasyonlar ekrana yazdırıldı.")

        elif action_choice == '2':
            kelime = input("Kelimeyi girin: ")
            minimum = input("Minimum karakter sayısını girin: ")
            maximum = input("Maksimum karakter sayısını girin: ")

            if int(minimum) > int(maximum):
                print("Minimum karakter sayısı, maksimum karakter sayısından büyük olamaz!")
                continue

            create_wordlist(minimum, maximum, karakter)
            
            # Crunch çıktılarını okuma
            with open("temp_wordlist.txt", 'r') as file:
                lines = file.readlines()

            # Kelimeye kombinasyonları ekleme
            combined_list = [kelime + line.strip() for line in lines] + [line.strip() + kelime for line in lines]

            # Geçici dosyayı sil
            os.remove("temp_wordlist.txt")

            # Kombinasyonları ekrana yazdırma
            for item in combined_list:
                print(item)

            # Sonuçları kaydetme
            save_choice = input("Kombinasyonları bir dosyaya kaydetmek ister misiniz? (E/H): ").lower()
            if save_choice == 'e':
                filename = input("Dosya adını girin (uzantı .txt olmalı): ")
                with open(filename, 'w') as file:
                    for item in combined_list:
                        file.write(f"{item}\n")
                print(f"Kombinasyonlar {filename} dosyasına kaydedildi.")
            print("Kombinasyonlar ekrana yazdırıldı.")
        else:
            print("Geçersiz seçim!")
            continue

        continue_choice = input("Başka bir işlem yapmak ister misiniz? (E/H): ").lower()
        if continue_choice == 'h':
            print("Program sonlandırıldı.")
            break

if __name__ == "__main__":
    main()
