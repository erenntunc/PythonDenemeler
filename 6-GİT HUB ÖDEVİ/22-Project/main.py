from tkinter import *
from bs4 import BeautifulSoup
import requests
import webbrowser

#request 1 start
url = "https://news.ycombinator.com/"
response = requests.get(url)
soup = BeautifulSoup(response.content,"html.parser")

veri = soup.find_all("a",href=True)
links = []
for i in veri:
    href = i.get('href')
    if href and not href.startswith('#') and "?" not in href and href.startswith("http"):
        links.append(href)

#request 1 end

#panel start
username = "admin"
passaword = "1234"
def login_window():
    window = Tk()
    window.title("Login Screen")
    window.minsize(width=300,height=210)
    username_label = Label(text="Enter Your Username")
    username_label.pack(pady=10)
    username_get = Entry()
    username_get.pack()
    passaword_label = Label(text="Enter Your Username")
    passaword_label.pack(pady=10)
    passaword_get = Entry()
    passaword_get.pack()
    login_button = Button(text="Login",command=lambda:check_and_login(username_get,passaword_get,window))
    login_button.pack(pady=10)
    register_button = Button(text="Register",command=lambda:admin_panel(username_get,passaword_get,window))
    register_button.pack()
    window.mainloop()

def register_window():
    r_window = Tk()
    r_window.minsize(width=300, height=210)

    register_username = Label(r_window, text="Enter Your Username")
    register_username.pack(pady=10)
    register_username_get = Entry(r_window)
    register_username_get.pack()

    register_passaword_label = Label(r_window, text="Enter Your Password")
    register_passaword_label.pack(pady=10)
    register_passaword_get = Entry(r_window, show="*")
    register_passaword_get.pack()

    register_button = Button(r_window, text="Register",
                             command=lambda: for_register(register_username_get, register_passaword_get, r_window))
    register_button.pack()

    register_button.config(state=DISABLED)

    def check_entries(*args):
        if register_username_get.get() != "" and register_passaword_get.get() != "":
            register_button.config(state=NORMAL)
        else:
            register_button.config(state=DISABLED)


    register_username_get.bind("<KeyRelease>", check_entries)
    register_passaword_get.bind("<KeyRelease>", check_entries)

    r_window.mainloop()


def admin_panel(username,password,window):
    window.destroy()
    a_window = Tk()
    a_window.title("Admin Screen")
    a_window.minsize(width=300, height=210)
    register_username = Label(a_window, text="Enter Your Username")
    register_username.pack(pady=10)
    register_username_get = Entry(a_window)
    register_username_get.pack()
    register_passaword_label = Label(a_window, text="Enter Your Password")
    register_passaword_label.pack(pady=10)
    register_passaword_get = Entry(a_window)
    register_passaword_get.pack()
    register_button = Button(a_window, text="Login",command=lambda:check_admin(register_username_get,register_passaword_get,a_window))
    register_button.pack()
    a_window.mainloop()

def check_admin(username,passaword,window):
    username = username.get()
    passaword = passaword.get()
    if username == "admin" and passaword == "1234":
        window.destroy()
        register_window()



def for_register(register_username_get,register_passaword_get,r_window):

    username = register_username_get.get()
    passaword = register_passaword_get.get()
    r_window.destroy()
    print(username,passaword)
    if username !="" and passaword !="":
        with open("user_info.txt", mode="a") as dosya:
            dosya.write(username+"\n")
        with open("user_info.txt", mode="a") as dosya:
            dosya.write(passaword+"\n")
    login_window()

def for_login(window):
    window.destroy()
    register_window()

def check_and_login(username_get,passaword_get,window):
    username = username_get.get()
    passaword =passaword_get.get()

    if username == "" or passaword == "":
        print("Lütfen kullanıcı adı ve şifre girin!")
        return

    with open("user_info.txt", mode="r") as dosya:
        lines = dosya.readlines()
    for i in range(0, len(lines), 2):
        file_username = lines[i].strip()
        file_password = lines[i + 1].strip() if i + 1 < len(lines) else ""

        if username == file_username and passaword == file_password:
            window.destroy()
            main_window()
            return
    print("Kullanıcı adı veya şifre yanlış!")

def main_window():
    new_window = Tk()
    new_window.minsize(width=1400, height=700)
    new_window.title("GÜNCEL HABERLERİN LİSTESİ")

    new_label = Label(new_window, text="GÜNCEL HABERLERİN LİSTESİ", font=("Arial", 16))
    new_label.grid(row=0, column=0, padx=10, pady=10)

    new_listbox = Listbox(new_window, width=100, height=40)
    for link in links:
        new_listbox.insert(END, link)
    new_listbox.grid(row=1, column=0, padx=10, pady=10)

    new_label_weather = Label(new_window, text="ÖĞRENMEK İSTEDİĞİNİZ ŞEHRİN HAVA DURUMUNU GİRİN", font=("Arial", 16))
    new_label_weather.grid(row=0, column=2, pady=(0, 0),padx=(50,0))

    new_text = Entry(new_window, width=30)
    new_text.grid(row=1, column=2, pady=(0, 0), sticky="n",padx=(10,0))

    city_weather = Label(new_window,text=f"")
    city_weather.grid(row=1, column=2,pady=(40, 0),sticky="n")
    weather_label = Label(new_window, text="Hava Durumu: ")
    weather_label.grid(row=1, column=2,pady=(80, 0),sticky="n")

    tempeture_label = Label(new_window, text="Sıcaklık: ")
    tempeture_label.grid(row=1, column=2,pady=(120, 0),sticky="n")

    feel_tempeture_label = Label(new_window, text="Hissedilen Sıcaklık: ")
    feel_tempeture_label.grid(row=1, column=2,pady=(160, 0),sticky="n")

    max_tempeture_label = Label(new_window, text="Maksimum Sıcaklık: ")
    max_tempeture_label.grid(row=1, column=2,pady=(200, 0), sticky="n")

    min_tempeture_label = Label(new_window, text="Minimum Sıcaklık: ")
    min_tempeture_label.grid(row=1, column=2,pady=(240, 0), sticky="n")

    wind_speed_label = Label(new_window, text="Rüzgar Hızı: ")
    wind_speed_label.grid(row=1, column=2,pady=(280, 0), sticky="n")

    def weather(event):
        API_KEY = "43b8c88a67f0f1e70f12663ed838280d"
        user_input = event.widget.get()
        weather_url = f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&appid={API_KEY}&units=metric&lang=tr"
        res = requests.get(weather_url)
        data = res.json()

        if data.get("cod") != 200:
            weather_label.config(text="Şehir bulunamadı!")
            tempeture_label.config(text="")
            feel_tempeture_label.config(text="")
            max_tempeture_label.config(text="")
            min_tempeture_label.config(text="")
            wind_speed_label.config(text="")
            return
        city= user_input.upper()
        weather = data["weather"][0]["main"]
        tempeture = data["main"]["temp"]
        feel_tempeture = data["main"]["feels_like"]
        max_tempeture = data["main"]["temp_max"]
        min_tempeture = data["main"]["temp_min"]
        wind_speed = data["wind"]["speed"]
        city_weather.config(text=f"{city} ŞEHRİNDE HAVA DURUMU")
        weather_label.config(text=f"Hava Durumu: {weather}")
        tempeture_label.config(text=f"Sıcaklık: {tempeture} °C")
        feel_tempeture_label.config(text=f"Hissedilen Sıcaklık: {feel_tempeture} °C")
        max_tempeture_label.config(text=f"Maksimum Sıcaklık: {max_tempeture} °C")
        min_tempeture_label.config(text=f"Minimum Sıcaklık: {min_tempeture} °C")
        wind_speed_label.config(text=f"Rüzgar Hızı: {wind_speed} m/s")

    new_text.bind("<Return>", weather)

    def open_link(event):
        selection = new_listbox.curselection()
        if selection:
            index = selection[0]
            url = new_listbox.get(index)
            webbrowser.open(url)

    new_listbox.bind("<Double-Button-1>", open_link)

    new_window.mainloop()


login_window()

















