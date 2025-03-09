import random
print("-"*50)
print("çarpım tablosu oyununa hoşgeldiniz")
print("-"*50)
print("kolaydan başlayıp en zor levele kadar gidecek bir oyun")
print("-"*50)
print("yanlış cevap verirseniz aynı levelden başlayacaksınız farklı sorular ile")
print("-"*50)

def carpimsorulari4():
    sayi1 = random.randint(70, 100)
    sayi2 = random.randint(70, 100)
    sonuc = sayi2 * sayi1
    kullanicisonuc = int(input(f"{sayi1}*{sayi2}= "))
    if kullanicisonuc == sonuc:
        print(f"TEBRİKLER DOĞRU CEVAP VERDİNİZ SONUC TÜM LEVELLERİ TAMAMLADINIZ={sonuc}")
        return True
    else:
        print(f"YANLIŞ CEVAP VERDİNİZ SİZİN SONUCUNUZ={kullanicisonuc} DOĞRU CEVAP={sonuc}")
        carpimsorulari4()

def carpimsorulari2():
    sayi1 = random.randint(10, 30)
    sayi2 = random.randint(10, 30)
    sonuc = sayi2 * sayi1
    kullanicisonuc = int(input(f"{sayi1}*{sayi2}= "))
    if kullanicisonuc == sonuc:
        print(f"TEBRİKLER DOĞRU CEVAP VERDİNİZ SONUC 1 ÜST LEVELE GECİYORSUNUZ={sonuc}")
        carpimsorulari3()
    else:
        print(f"YANLIŞ CEVAP VERDİNİZ SİZİN SONUCUNUZ={kullanicisonuc} DOĞRU CEVAP={sonuc}")
        carpimsorulari2()
def carpimsorulari3():
    sayi1 = random.randint(30, 70)
    sayi2 = random.randint(30, 70)
    sonuc = sayi2 * sayi1
    kullanicisonuc = int(input(f"{sayi1}*{sayi2}= "))
    if kullanicisonuc == sonuc:
        print(f"TEBRİKLER DOĞRU CEVAP VERDİNİZ SONUC 1 ÜST LEVELE GECİYORSUNUZ={sonuc}")
        carpimsorulari4()
    else:
        print(f"YANLIŞ CEVAP VERDİNİZ SİZİN SONUCUNUZ={kullanicisonuc} DOĞRU CEVAP={sonuc}")
        carpimsorulari3()
def carpimsorulari():
    sayi1 =random.randint(1,10)
    sayi2 =random.randint(1,10)
    sonuc = sayi2*sayi1
    kullanicisonuc=int(input(f"{sayi1}*{sayi2}= "))
    if kullanicisonuc ==sonuc:
        print(f"TEBRİKLER DOĞRU CEVAP VERDİNİZ SONUC 1 ÜST LEVELE GEÇİYORSUNUZ={sonuc}")
        carpimsorulari2()
    else:
        print(f"YANLIŞ CEVAP VERDİNİZ SİZİN SONUCUNUZ={kullanicisonuc} DOĞRU CEVAP={sonuc}")
        carpimsorulari()
while True:
    if carpimsorulari():
        break


