from Tkinter import *
root = Tk()
root.title("DR PHIL PROMO STATUS")

topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side = BOTTOM)

button1 = Button(topFrame, text = "New Record", fg = "red").pack()
button2 = Button(topFrame, text = "Update Record", fg = "blue").pack()
button3 = Button(bottomFrame, text = "Update Record", fg = "green").pack()



root.mainloop()

