import tkinter


window = tkinter.Tk()
window.title("My window")
window.minsize(width=500, height=600)

my_label =tkinter.Label(text="Here goes my label", font=("Arial", 25))
my_label.pack()

window.mainloop()