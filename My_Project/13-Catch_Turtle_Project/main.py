import time
import turtle
import random
from random import randint

background = turtle.Screen()
background.bgcolor("light blue")
background.title("Catch The Turtle")
MyTurtle = turtle.Turtle()
background.setup(800,700)# ekranın boyutunu ayarlıyor
MyTurtle.hideturtle()

countdown =30
pen=turtle.Turtle()
pen.hideturtle()
pen.color("black")
pen.up()
pen.setposition(0, 260)
pen.down()
MyTurtle.showturtle()
MyTurtle.shapesize(stretch_wid=2, stretch_len=2)
MyTurtle.speed(8)
written = 0  # Global değişken

def click(x, y):
    global written  # Global değişkeni kullanacağımızı belirtiyoruz
    written += 1  # Sayacı artırıyoruz
    sayac_turtle.clear()  # Önceki yazıyı temizliyoruz
    sayac_turtle.write(f"SCORE: {written} ", align="center", font=("Arial", 10, "normal"))  # Yeni sayıyı yazdırıyoruz


sayac_turtle = turtle.Turtle()
sayac_turtle.speed(0)
sayac_turtle.color("black")
sayac_turtle.penup()
sayac_turtle.hideturtle()
sayac_turtle.goto(0, 300)
sayac_turtle.write(" SCORE: ", align="center", font=("Arial", 10, "normal"))  # Başlangıçta 0 yazıyor


for timer in range(countdown,-1,-1): #(countdown,-1,-1): ilk -1 ne zaman duracağı yani 0 da duracak diğeri de -1 -1 azaltacağını gösteriyor
    background.listen()
    randomx = randint(-300,300)
    randomy = randint(-300,300)
    pen.clear()
    pen.write("SAYAÇ: %s" % timer, align="center", font=("Arial", 10, "normal"))
    MyTurtle.shape('turtle')
    MyTurtle.penup()
    MyTurtle.goto(randomx,randomy)
    MyTurtle.onclick(click)
    time.sleep(0.5)
    if timer == 0:
        time.sleep(2)
        turtle.bye()
turtle.mainloop()






