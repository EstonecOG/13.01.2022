from tkinter import *

win=Tk()
win.title("Okno")
win.geometry("600x600")
c=IntVar()
c.set(1)
c=Canvas(win, width=900, height=900, bg="white") 
# Овал
c.create_oval(300, 350, 100, 100, outline="#f11", fill="#1f1", width=2)
c.create_oval(250, 250, 180, 180, outline="red", fill="red", width=2)
c.create_oval(120, 120, 170, 170, outline="red", fill="red", width=2)




c.pack()
win.mainloop()




