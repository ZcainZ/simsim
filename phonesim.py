#pylint:disable=W0311
#Import
import time
import datetime
import random
import calendar
x = datetime.date.today()
#Welcome
print("🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟")
print("🌟WELCOME TO MOBILE PHONE SIMULATOR🌟")
print("🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟")
print("di translate oleh ZcainZ")
time.sleep(1)
name = input("\nMASUKAN NAMAMU: ")
print(f"\nHALO {name.upper()}")
time.sleep(0.5)
print(f"TANGGAL - {x}")
time.sleep(0.5)
print("BATRAI TERSISA - 100%")
time.sleep(0.5)
#Apps
while 1 > 0:
  time.sleep(1)
  print("\n___APLIKASI___")
  time.sleep(0.5)
  print("1.CHAT.")
  time.sleep(0.5)
  print("2.TELEPON.")
  time.sleep(0.5)
  print("3.KONTAK.")
  time.sleep(0.6)
  print("4.PESAN.")
  time.sleep(0.6)
  print("5.KALENDER.")
  time.sleep(0.6)
  print("6.KALKULATOR.")
  time.sleep(0.7)
  print("7.KALKULATOR UMUR.")
  time.sleep(0.7)
  print("8.NOMOR ACAK.")
  time.sleep(0.8)
  print("9.GAME.")
  time.sleep(0.5)
  option = int(input("PILIH: "))
  time.sleep(0.5)
  #Games
  if option == 9:
    print("\n___GAME___")
    time.sleep(0.5)
    print("1.GAME TEBAK NOMOR.")
    time.sleep(0.5)
    print("2.DOWNLOAD GAME LAIN.")
    time.sleep(0.5)
    print("3.KEMBALI KE APLIKASI.")
    time.sleep(0.5)
    option0 = int(input("PILIH: "))
    time.sleep(0.5)
    if option0 == 2:
      print("\nMAAF, PULSAMU TIDAK CUKUP.")
    if option0 == 1:
      print("\n___GAME TEBAK NOMOR___")
      guess = 1
      win_number = random.randrange(1,100)
      number = int(input("TEBAK NOMOR DARI 1 - 100: "))
      while number != win_number:
        if number < win_number:
          guess += 1
          print("\nTEBAKANMU SALAH! COBA TEBAK LEBIH TINGGI.")
          time.sleep(0.5)
          number = int(input("TEBAK NOMOR DARI 1 - 100: "))
        if number > win_number:
          guess += 1
          print("\nTEBAKANMU SALAH! COBA TEBAK LEBIH RENDAH.")
          time.sleep(0.5)
          number = int(input("TEBAK NOMOR DARI 1 - 100: "))
      print("\n👏👌👍SELAMAT👍👌👏")
      time.sleep(0.5)
      print(f"KAMU BERHASIL MENEBAK DALAM {guess} PERCOBAAN.")
  #Random Number Generator
  if option == 8:
    print("\n___NOMOR ACAK___")
    time.sleep(0.5)
    n1 = int(input("TULIS NOMOR PERTAMA: "))
    n2 = int(input("TULIS NOMOR TERAKHIR: "))
    n3 = random.randrange(n1,n2)
    time.sleep(0.5)
    print(f"\nNOMOR ACAKNYA ADALAH {n3}")
  #Age Calculator
  if option == 7:
    print("\n___KALKULATOR UMUR___")
    time.sleep(0.5)
    year1 = int(input("TAHUN SEKARANG: "))
    year2 = int(input("TAHUN KELAHIRANMU: "))
    age = year1 - year2
    time.sleep(0.5)
    print(f"\nDALAM TAHUN, UMURMU ADALAH {age} TAHUN.")
    time.sleep(1)
    print(f"DALAM BULAN, UMURMU ADALAH {age*12} BULAN.")
    time.sleep(1)
    print(f"DALAM HARI, UMURMU ADALAH {age*365} HARI.")
    time.sleep(1)
    print(f"DALAM JAM, UMURMU ADALAH {age*365*24} JAM.")
    time.sleep(1)
    print(f"DALAM MENIT, THE AGE IS {age*365*24*60} MENIT.")
    time.sleep(1)
    print(f"IN DETIK, THE AGE IS {age*365*24*60*60} DETIK.")
  #Calculator
  if option == 6:
    def calc():
      print("\n___KALKULATOR___")
      time.sleep(0.5)
      num1 = int(input("TULIS NOMOR PERTAMA: "))
      num2 = int(input("TULIS NOMOR KEDUA: "))
      time.sleep(0.5)
      print("\n1.DITAMBAHKAN (+).")
      time.sleep(0.5)
      print("2.DIKURANGKAN (-).")
      time.sleep(0.5)
      print("3.DIKALI(×).")
      time.sleep(0.5)
      print("4.DIBAGI (÷).")
      time.sleep(0.5)
      option1 = int(input("PILIH: "))
      time.sleep(0.5)
      print("")
      if option1 == 1:
        print(f"HASIL = {num1+num2}")
      if option1 == 2:
        print(f"HASIL = {num1-num2}")
      if option1 == 3:
        print(f"HASIL = {num1*num2}")
      if option1 == 4:
        print(f"HASIL = {num1/num2}")
      time.sleep(0.6)
      print("\n1.ULANGI LAGI.")
      time.sleep(0.5)
      print("2.KEMBALI.")
      time.sleep(0.5)
      cal = int(input("PILIH: "))
      if cal == 1:
        calc()
    calc()
  #Calendar
  if option == 5:
    print("\n___KALENDER___")
    time.sleep(0.5)
    print("1.KALENDER 1 TAHUN.")
    time.sleep(0.5)
    print("2.KALENDER 1 BULAN.")
    time.sleep(0.5)
    option2 = int(input("PILIH: "))
    time.sleep(0.5)
    print("")
    if option2 == 1:
      year = int(input("MASUKKAN TAHUNNYA: "))
      time.sleep(0.5)
      print(f"\nKALENDER 1 TAHUN {year}")
      print("")
      print(calendar.calendar(year))
      time.sleep(3)
    if option2 == 2:
      year2 = int(input("TULIS TAHUNNYA: "))
      month = int(input("TULIS BULANNYA: "))
      print("")
      time.sleep(0.5)
      print(calendar.month(year2,month))
  #Messages
  if option == 4:
    print("\n___📨PESAN📨___")
    time.sleep(0.5)
    print("\nJIO- BATRAI MU HABIS.")
    print("     CAS HP MU...")
    time.sleep(0.5)
    print("___________________________")
    time.sleep(0.5)
    print("\nJIO- PAKETMU SUDAH")
    print("     HABIS..")
    time.sleep(0.5)
    print("____________________________")
  #Contacts
  if option == 3:
    print("\n___KONTAK___")
    time.sleep(0.5)
    print("1.TAMBAHKAN KONTAK BARU.")
    time.sleep(0.5)
    print("2.LIHAT KONTAK.")
    time.sleep(0.5)
    option3 = int(input("PILIH: "))
    time.sleep(0.5)
    print("")
    if option3 == 1:
      name2 = input("TULIS NAMANYA: ")
      nu = int(input("TULIS NOMOR TELEPON: "))
      time.sleep(0.5)
      print(f"\n👤 {name2}")
      print(f"{nu}")
      time.sleep(0.5)
      print("\nPEMBERITAHUAN: KONTAK BARU BUTUH BEBERAPA SAAT UNTUK DITAMBAHKAN.")
    if option3 == 2:
      print("1.MY LOVE")
      print("   8908904190")
      time.sleep(0.5)
      print("\n2.BEST FRIEND")
      print("   8249457627")
  #Call
  if option == 2:
    print("\n___📞TELEPON📞___")
    time.sleep(0.5)
    print("1.RIWAYAT TELEPON.")
    time.sleep(0.5)
    print("2.TELEPON SESEORANG.")
    time.sleep(0.5)
    option4 = int(input("PILIH: "))
    time.sleep(0.5)
    print("")
    if option4 == 1:
      print("KEMARIN 17:00: MY LOVE [8908904190]")
      time.sleep(0.5)
      print("KEMARIN 17:00: BEST FRIEND [8249457627]")
    if option4 == 2:
      print("MAAF, PULSAMU SUDAH HABIS.")
  #Chat
  if option == 1:
    print("\n___CHAT___")
    time.sleep(0.5)
    print("\n1.CHAT DENGAN 'MY LOVE'")
    time.sleep(0.5)
    print("\n2.CHAT DENGAN 'BEST BUDDY'")
    time.sleep(0.5)
    option5 = int(input("PILIH KONTAK UNTUK CHAT:"))
    time.sleep(0.5)
    print("")
    if option5 == 1:
      print("TULIS")
      input("PESANMU: ")
      time.sleep(0.5)
      print("\nMY LOVE: Maaf Sayang, aku sedang sibuk...")
      print("         Nanti aku chat lagi.")
    if option5 == 2:
      print("HALO... APA KABARMU?")
      time.sleep(0.5)
      print("TULIS")
      input("PESANMU: ")
      time.sleep(0.5)
      print("\nTERMA KASIH UNTUK WAKTUNYA.")
      time.sleep(1)
      print("TEKAN BINTANGNYA 🌟 JIKA KAMU PUAS.")
      time.sleep(1.5)
      print("PROGRAM INI MASIH DALAM PENGEMBANGAN.")
      time.sleep(1.5)
      print("BERI SARAN DI KOLOM KOMENTAR.")
      time.sleep(1.5)
#Thanks for your time.
#Please tap the star 🌟 if you appreciate my work.
#This programme is under development and needs your suggestions.
#Suggest changes in comment section if any.
#Please visit my profile for other amazing programmes.
