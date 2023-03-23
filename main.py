import tkinter


#
#
# def button_clicked():
#     print("I got clicked")
#     if input_field.get() == "":
#         my_label["text"] = "I got clicked"
#     else:
#         my_label["text"] = input_field.get()
#
# window = tkinter.Tk()
# window.title("My window")
# window.minsize(width=500, height=600)
# window.config(padx=50,pady=100)
#
# my_label =tkinter.Label(text="Here goes my label", font=("Arial", 25))
# my_label.grid(column=0,row=0)
# #my_label["text"] = " New label via dict"
# #my_label.config(text="New label via config")
#
#
# button = tkinter.Button(text  = "click me", command=button_clicked)
# button.grid(column=1,row=1)
#
# newbutton = tkinter.Button(text  = "new button", command=button_clicked)
# newbutton.grid(column=2,row=0)
#
# input_field = tkinter.Entry()
# input_field.grid(column=3,row=2)

def calculate():
    label3["text"] = round(float(miles_input.get()) * 1.609,2)


window = tkinter.Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)


miles_input = tkinter.Entry(width = 15)
miles_input.grid(row=0, column=1, padx=20, pady=20)

label1 = tkinter.Label()
label1["text"] = "Miles"
label1.grid(column=1, row=0)

label2 = tkinter.Label()
label2["text"] = "is equal to"
label2.grid(column=0, row=1)

label3 = tkinter.Label()
label3["text"] = "0"
label3.grid(column=1, row=1)

label4 = tkinter.Label()
label4["text"] = "KM"
label4.grid(column=2, row=1)

button = tkinter.Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)

window.mainloop()
