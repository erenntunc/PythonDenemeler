import turtle

wn = turtle.Screen()
wn.title("Button Counting")
wn.bgcolor("red")  # Arka plan rengi kırmızı
wn.setup(width=800, height=600)

written = 0  # Global değişken

def click(x, y):
    global written  # Global değişkeni kullanacağımızı belirtiyoruz
    written += 1  # Sayacı artırıyoruz
    pen.clear()  # Önceki yazıyı temizliyoruz
    pen.write(f" {written} ", align="center", font=("Arial", 30, "normal"))  # Yeni sayıyı yazdırıyoruz

button = turtle.Turtle()
button.penup()
button.color("yellow")  # Buton rengi sarı
button.shape("square")
button.shapesize(stretch_wid=5, stretch_len=5)  # Buton boyutları
button.goto(0, -100)  # Butonu aşağıya yerleştiriyoruz
button.onclick(click)  # Butona tıklanınca click fonksiyonunu çağırır

sayac_turtle = turtle.Turtle()
sayac_turtle.speed(0)
sayac_turtle.color("black")
sayac_turtle.penup()
sayac_turtle.hideturtle()
sayac_turtle.goto(0, 200)
sayac_turtle.write(" 0 ", align="center", font=("Arial", 30, "normal"))  # Başlangıçta 0 yazıyor

turtle.done()
