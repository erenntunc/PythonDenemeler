import tkinter

window = tkinter.Tk()
window.title("BMI CALCULATOR")
window.minsize(width="250", height="250")


layer_1 = tkinter.Label(text="ENTER YOUR WEIGHT(Kg)")
layer_1.pack()


user_weight = tkinter.Entry()
user_weight.pack()

layer_0 = tkinter.Label(text="***********************************")
layer_0.pack()


layer_2 = tkinter.Label(text="ENTER YOUR HEIGHT(Cm)")
layer_2.pack()


user_height = tkinter.Entry()
user_height.pack()


def calculated():
    try:
        weight0 = int(user_weight.get())
        height0 = int(user_height.get()) / 100

        if weight0 > 0 and height0 >= 1:
            bmi = weight0 / (height0 * height0)
            result_text = f"Your BMI is: {bmi:.2f}"
            if bmi<16:
                calculate_text = "Severe Thinness"
            elif bmi>18.5 and bmi<=25:
                calculate_text ="Normal"
            elif bmi>25 and bmi<=30:
                calculate_text = "Overweight"
            elif bmi>30:
                calculate_text = "Obese"
        else:
            result_text = "Invalid weight or height entered."
    except ValueError:

        result_text = "Please enter valid numbers."


    layer_3.config(text=result_text)
    layer_4.config(text=calculate_text)

my_button = tkinter.Button(text="Calculate", command=calculated)
my_button.pack()

layer_3 = tkinter.Label(text="Result will appear here.")
layer_3.pack()

layer_4 = tkinter.Label(text="")
layer_4.pack()
tkinter.mainloop()
