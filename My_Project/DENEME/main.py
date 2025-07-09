class book():
    def __init__(self,book_name,writer,condition="mevcut"):
        self.book_name = book_name
        self.writer = writer
        self.condition = condition

    def __str__(self):
        return f"Kitap: {self.book_name}, Yazar: {self.writer}, Durum: {self.condition}"


class library():
    def __init__(self):
        self.books = []


    def book_add(self,book):
        self.books.append(book)

    def borrowing_a_book(self,book_name):
        for book in self.books:
            if book.book_name == book_name and book.condition == "mevcut":
                print(f"{book_name} adlı kitap mevcut")
                book.condition = "mevcut değil"
                return
            else:
                print(f"{book_name} adlı kitap mevcut değil veya zaten ödünç alındı.")

    def book_return(self,return_name):
        for book in self.books:
            if book.book_name == return_name and book.condition == "mevcut değil":
                print(f"{return_name} adlı kitap geri alındı teşekkürler")
                book.condition = "mevcut"
                return
            else:
                print(f"{return_name} adlı kitap mevcut değil ya da ödünç alınmış")

    def show_books(self):
        if not self.books:
            print("kütüphane boş")
        else:
            for x in self.books:
                print(f"{x} ")


library = library()

while True:
    print("kütüphane sistemi")
    print("*"*75)
    print("1. Kitap ekle")
    print("2. Kitap ödünç al")
    print("3. Kitap geri ver")
    print("4. Kitapları görüntüle")
    print("5. Çıkış")

    choose = input("1 2 3 4 5 değerlerinden bir tanesini girin")
    if choose == "1" :
        name =  input("eklemek istediğiniz kitabı yazınız")
        writername = input("eklemek istediğiniz yazarı yazınız")
        yeni_kitap = book(book_name=name,writer=writername)
        library.book_add(yeni_kitap)
        print(f"{yeni_kitap} başarıyla eklendi")
    elif choose == "2" :
        borrowbook =  input("ödünç almak istediğiniz kitabı girin:")
        library.borrowing_a_book(borrowbook)
    elif choose == "3" :
        book_to_return = input("geri vermek istediğiniz kitabı girin:")
        library.book_return(book_to_return)
    elif choose == "4":
        print(library.show_books())
    elif choose == "5":
        print("Program sonlandırılıyor...")
        break
    else:
        print("geçersiz bir sayı girdiniz")