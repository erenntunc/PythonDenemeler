from datetime import datetime

# Otoparkta bulunan araçları ve giriş zamanlarını saklamak için bir dictionary kullanıyoruz.
car_list = {}
çıkış = True

while çıkış:
    print("1-araba ekle")
    print("2-araba çıkış")
    print("3-araçları göster")
    print("4-çıkış")
    print("-"*50)
    kullanici_secim = input("YAPMAK İSTEDİĞİNİZ İŞLEMİ SEÇİN: ")

    if kullanici_secim == "1":
        car = input("ARABA PLAKASINI GİRİN: ")
        car = car.upper()
        if car not in car_list:
            # Araba plakasını ve giriş zamanını kaydediyoruz
            car_list[car] = datetime.now()
            print(f"{car} plakalı araç başarılı bir şekilde eklendi")
        else:
            print(f"{car} zaten bu plaka mevcut")

    elif kullanici_secim == "2":
        if len(car_list) == 0:
            print("OTOPARK BOŞ")
        else:
            print("Otoparktaki araçlar:")
            for car in car_list:
                print(f"- {car}")

            silinecek_araba = input("Silmek istediğiniz plakayı yazınız: ")
            if silinecek_araba in car_list:

                cikis_zamani = datetime.now()

                giris_zamani = car_list.pop(silinecek_araba)

                gecen_sure = cikis_zamani - giris_zamani
                dakika = gecen_sure.seconds // 60
                saniye = gecen_sure.seconds % 60

                print(f"{silinecek_araba} plakalı araç çıkış yaptı.")
                print(f"Bu araç {dakika} dakika {saniye} saniye otoparkta kaldı.")
            else:
                print("Böyle bir araba otoparkta mevcut değil")

    elif kullanici_secim == "3":
        if len(car_list) == 0:
            print("OTOPARK BOŞ")
        else:
            print("Otoparktaki araçlar:")
            for car, giris_zamani in car_list.items():
                suanki_zaman = datetime.now()
                gecen_sure = suanki_zaman - giris_zamani
                dakika = gecen_sure.seconds // 60  # Dakikayı hesaplayalım
                saniye = gecen_sure.seconds % 60
                print(f"- {car}: {dakika} dakika {saniye} saniye otoparkta kaldı")

    elif kullanici_secim == "4":
        print("Çıkış yapılıyor...")
        çıkış = False
    else:
        print("LÜTFEN GEÇERLİ BİR DEĞER GİRİNİZ")
    print("-"*50)
