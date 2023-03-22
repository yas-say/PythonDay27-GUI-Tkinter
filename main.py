import tkinter


def button_clicked():
    print("I got clicked")
    if input_field.get() == "":
        my_label["text"] = "I got clicked"
    else:
        my_label["text"] = input_field.get()

window = tkinter.Tk()
window.title("My window")
window.minsize(width=500, height=600)

my_label =tkinter.Label(text="Here goes my label", font=("Arial", 25))
my_label.pack()
#my_label["text"] = " New label via dict"
#my_label.config(text="New label via config")


button = tkinter.Button(text  = "click me", command=button_clicked)
button.pack()

input_field = tkinter.Entry()
input_field.pack()






window.mainloop()