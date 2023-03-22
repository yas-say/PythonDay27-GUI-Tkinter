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
my_label.grid(column=0,row=0)
#my_label["text"] = " New label via dict"
#my_label.config(text="New label via config")


button = tkinter.Button(text  = "click me", command=button_clicked)
button.grid(column=1,row=1)

newbutton = tkinter.Button(text  = "new button", command=button_clicked)
newbutton.grid(column=2,row=0)

input_field = tkinter.Entry()
input_field.grid(column=3,row=2)






window.mainloop()