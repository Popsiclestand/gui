from Tkinter import *
root = Tk()
root.title("DR PHIL PROMO STATUS")

topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side = BOTTOM)

instructions = Label(topFrame, text = "WELCOME TO THE DR PHIL PROMO STATUS PROGRAM!", bg = "light blue").pack(fill = X)
button1 = Button(topFrame, text = "New Record", fg = "red").pack(side = RIGHT)
button2 = Button(topFrame, text = "Update Record", fg = "blue").pack(side = RIGHT)
button3 = Button(bottomFrame, text = "Print Record", fg = "green").pack()



root.mainloop()

