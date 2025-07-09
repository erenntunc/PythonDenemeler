import random

loop = 1
print("Rastgele şifre üreten programa hoşgeldiniz")
print("--" * 50)

# Ana while döngüsü
while loop == 1:
    print("Üretmek isterseniz 1'e basın, çıkmak isterseniz 2'ye basın:")

    try:
        kullanicisecim = int(input(""))  # Kullanıcıdan giriş alıyoruz ve sayısal olduğunu kontrol ediyoruz
    except ValueError:
        print("Lütfen geçerli bir sayı girin.")  # Eğer giriş sayısal değilse hata mesajı
        continue  # Hata alındıysa tekrar giriş yapmasını sağlıyoruz

    if kullanicisecim == 1:
        # Şifreyi oluşturmak için listeyi dışarıda tanımlıyoruz
        passaword_list = []


        def random_passaword():
            # Büyük harfler
            upper_letter_list = ["Z", "H", "V", "N", "M"]
            for a in range(3):
                passaword_list.append(random.choice(upper_letter_list))

            # Küçük harfler
            lower_letter_list = ["a", "b", "c", "d", "e", "f", "g"]
            for b in range(3):
                passaword_list.append(random.choice(lower_letter_list))

            # Karakterler
            character_list = ["#", "-", ".", ",", "!", "_", "?"]
            for c in range(2):
                passaword_list.append(random.choice(character_list))

            # Sayılar
            for d in range(2):
                passaword_list.append(str(random.randint(0, 9)))  # Sayıları string olarak ekliyoruz


        random_passaword()

        # Listeyi karıştırıyoruz
        random.shuffle(passaword_list)

        # Şifreyi string'e çeviriyoruz
        result = "".join(passaword_list)

        print("--" * 50)
        print(f"Şifreniz: {result}")
        print("--" * 50)

        # Tekrar şifre üretmek için kullanıcıya seçenek sunuyoruz
        print("Tekrar şifre üretmek isterseniz 1'e basın, çıkmak isterseniz 2'ye basın:")
        print("--" * 50)

    elif kullanicisecim == 2:
        loop = 2
        print("Program Sonlandırılıyor...")
