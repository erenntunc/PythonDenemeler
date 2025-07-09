import tkinter
from tkinter import Label
from PIL import ImageTk, Image
from tkinter import Text, messagebox

title_key = {}
#root yazma ekranı
root = tkinter.Tk()
root.title("Secret Note")
root.minsize(width=500, height=800)
#end root

#kayıt ekranı
def change_passaword_Window(window):
        window.destroy()
        root_4 = tkinter.Tk()
        root_4.minsize(width=300,height=100)
        root_4.title("register")
        enter_login_label = tkinter.Label(root_4, text="Enter Your username")
        enter_login_label.pack()

        enter_login = tkinter.Entry(root_4, width=40)
        enter_login.pack()

        enter_passaword_label = tkinter.Label(root_4, text="Enter Your Passaword")
        enter_passaword_label.pack()

        enter_passaword = tkinter.Entry(root_4, width=40)
        enter_passaword.pack()

        last_button = tkinter.Button(root_4, text="Register",command=lambda: change_passaword(enter_login, enter_passaword))

        last_button.pack()


def change_passaword(username1,passaword1):

    un = username1.get().strip()
    ps = passaword1.get().strip()

    if not un or not ps:
        messagebox.showwarning("UYARI","BOŞ BIRAKMAYIN")
    else:
        title_key[un] = ps
        messagebox.showwarning("UYARI", "BAŞARILI BİR ŞEKİLDE KAYIT EDİLDİ")


#kayıt ekranı sonu

# çözme ekranı
def root2_panel():
    root2 = tkinter.Tk()
    root2.minsize(width=300,height=100)
    root2.title("screen")

    enter_login_label = tkinter.Label(root2,text="Enter Your username")
    enter_login_label.pack()

    enter_login = tkinter.Entry(root2, width=40)
    enter_login.pack()

    enter_passaword_label = tkinter.Label(root2, text="Enter Your Passaword")
    enter_passaword_label.pack()

    enter_passaword = tkinter.Entry(root2,width=40)
    enter_passaword.pack()

    last_button = tkinter.Button(root2, text="LOGİN",command=lambda:kontrol_et(enter_login,enter_passaword,root2) )
    last_button.pack()

    register_button = tkinter.Button(root2,text="Change Passaword",command=lambda:change_passaword_Window(root2))
    register_button.pack()




#çözme ekranı sonu

#son çözüm ekranı

def kontrol_et(enter_login,enter_passaword,root2):

    login_value = enter_login.get().strip()
    enter_passaword = enter_passaword.get().strip()

    if login_value in title_key and title_key[login_value] ==enter_passaword :
        root2.destroy()
        root_3_ekranı()


    else:
        pass




#son çözüm ekranı sonu

#son son çözüm ekranı
def root_3_ekranı():
    kaydrma=3
    root_3 = tkinter.Tk()
    root_3.minsize(width=500,height=800)

    enter_secret_label = enter_title_label = tkinter.Label(root_3, text="Enter Your Secret Massage")
    enter_secret_label.pack()

    enter_massage1 = tkinter.Text(root_3,width="40", height="20")
    enter_massage1.pack()

    decrypt_button = tkinter.Button(text="DECRYPT", command=lambda:sifre_cözme(enter_massage1,kaydrma))

    decrypt_button.pack()


#son son çözüm ekranı sonu

kaydirma = 3
#image
my_pic = Image.open("lock.jpg")
resized = my_pic.resize((150, 125), Image.Resampling.LANCZOS)

my_pic_tk = ImageTk.PhotoImage(resized)

my_label = Label(root, image=my_pic_tk)
my_label.pack(pady=20)
#end image

#funcitons
def encrypt(mesaj, kaydirma):
    encrypted_message = ""
    for char in mesaj:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            encrypted_message += chr((ord(char) - start + kaydirma) % 26 + start)
        else:

            encrypted_message += char
    return encrypted_message


def button2():
    root2_panel()
    root.destroy()

def sifre_cözme(massage,kaydırma):

    mesaj_value = massage.get("1.0",tkinter.END)
    last_value = decrypt(mesaj_value,kaydirma)
    massage.delete(1.0,tkinter.END)
    massage.insert(tkinter.END,last_value)

def decrypt(encrypted_message, kaydirma):

    return encrypt(encrypted_message, -kaydirma)


def write_file(mesaj):
    name = enter_title.get()

    with open(f"{name}.txt", "a") as file:
        file.write(f"{mesaj}")

def button():

    title = enter_title.get().strip()
    encrypted_mesaj = encrypt(enter_massage.get("1.0",tkinter.END),kaydirma)
    if not title or not encrypted_mesaj :
        messagebox.showwarning("uyarı","LÜTFEN GEREKLİ ALANLARI DOLDURUNUZ")
    else:
        write_file(encrypted_mesaj)
        messagebox.showwarning("BAŞARILI","İŞLEMİNİZ BAŞARIYLA KAYIT EDİLDİ")
#end functions


#widgets
enter_title_label = tkinter.Label(root,text="Enter Your Title")
enter_title_label.pack()

enter_title = tkinter.Entry(width="50")
enter_title.pack()

enter_secret_label = enter_title_label = tkinter.Label(root,text="Enter Your Secret Massage")
enter_secret_label.pack()

enter_massage = tkinter.Text(width="40",height="20")
enter_massage.pack()

save_button = tkinter.Button(text="SAVE&ENCRYPT",command=button)
save_button.pack()
decrypt_button = tkinter.Button(text="DECRYPT",command=button2)
decrypt_button.pack()
#end widgets

root.mainloop()
