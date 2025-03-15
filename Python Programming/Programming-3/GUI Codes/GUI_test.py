# from tkinter import *
# window = Tk()
# window.title("Students")
# window.geometry("400x300")
# name = Label(window , text="Name : " , font="Candara" , fg="#48CDC8")
# name.grid(row=0 , column=0 , padx=10 , pady=5)
# e1 = Entry(window)
# e1.grid(row=0 , column=1)
# regno = Label(window , text="Regd No : " , font="Candara" , fg="#48CDC8")
# regno.grid(row=1 , column=0 , padx=10 , pady=5)
# e2 = Entry(window)
# e2.grid(row=1 , column=1)
# btn = Button(window , text="Submit" , fg="#F44C2A" , font="Consolas")
# btn.grid(row=3 , column=1)
# window.mainloop()


# from tkinter import *
# window = Tk()
# window.title("tk#2")
# window.geometry("400x300")
# last_name = Label(window , text="Last Name : " , font="Candara" , fg="#48CDC8")
# last_name.grid(row=0 , column=0 , padx=10 , pady=5)
# e1 = Entry(window)
# e1.grid(row=0 , column=1)
# First_name = Label(window , text="First Name : " , font="Candara" , fg="#48CDC8")
# First_name.grid(row=1 , column=0 , padx=10 , pady=5)
# e2 = Entry(window)
# e2.grid(row=1 , column=1)
# Job = Label(window , text="Job : " , font="Candara" , fg="#48CDC8")
# Job.grid(row=2 , column=0 , padx=10 , pady=5)
# e3 = Entry(window)
# e3.grid(row=2 , column=1)
# Country = Label(window , text="Country : " , font="Candara" , fg="#48CDC8" )
# Country.grid(row=3 , column=0 , padx=10 , pady=5)
# e4 = Entry(window)
# e4.grid(row=3 , column=1)
# bt1 = Button(window , text="Show")
# bt1.grid(row=4 , column=0)
# bt2 = Button(window , text="Quit" , command= exit)
# bt2.grid(row=4 , column=1)
# window.mainloop()


# from tkinter import *
# top = Tk()
# top.geometry("400x300")
# cbtn1 = Checkbutton(top , text = "Red" , fg = "red")
# cbtn1.pack()
# cbtn2 = Checkbutton(top , text = "Green" , fg = "green")
# cbtn2.pack()
# cbtn3 = Checkbutton(top , text = "Yellow" , fg = "yellow")
# cbtn3.pack()
# top.mainloop()


# from tkinter import *
# top  =Tk()
# top.geometry("400x300")
# enty1 = Entry(top , width="30")
# enty1.pack()
# enty2 = Entry(top , bg="yellow")
# enty2.pack()
# enty3 = Entry(top , show="*")
# enty3.pack()
# top.mainloop()


# from tkinter import *
# top = Tk()
# top.geometry("400x300")
# tframe = Frame(top , width="100" , height="100" , bg="yellow")
# tframe.pack()
# iframe = Frame(top , width="30" , height="30" ,  bg="red")
# iframe.pack(side=RIGHT)
# rframe = Frame(top , width="30" , height="30" ,  bg="green")
# rframe.pack(side=LEFT)
# btn1 = Button(tframe , text="Red" , fg="red")
# btn1.place(x=10,y=10)
# top.mainloop()

# from tkinter import *
# top = Tk()
# top.geometry("400x300")
# lbl1 = Label(top , text="List of colors" , fg="red" , bg= "yellow")
# lbl1.place(x=10,y=10)
# lb = Listbox(top , height=5)
# lb.insert(1 , "Red")
# lb.insert(2 , "Green")
# lb.insert(3 , "Blue")
# lb.insert(4 , "Yellow")
# lb.place(x=10,y=40)
# top.mainloop()

# from tkinter import *
# top = Tk()
# top.geometry("400x300")
# rad1 = Radiobutton(top , text="Male" , value=1)
# rad1.pack()
# rad2 = Radiobutton(top , text="Female" , value=2)
# rad2.pack()
# top.mainloop()

# from tkinter import *
# top = Tk()
# top.geometry("400x300")
# tx = Text(top , height=10 , width=30)
# tx.pack()
# tx.insert(INSERT , "Hello World\nThis is my first GUI \nI am learning Python\nIt is so much fun")
# top.mainloop()


# from tkinter import *
# top = Tk()
# top.geometry("200x200")
# lbl = Label(top , text="Price" , bg="red" , fg="yellow")
# lbl.pack()
# scale = Scale(top , from_=100 , to=1000 , orient=HORIZONTAL)
# scale.pack(anchor=CENTER)
# top.mainloop()


# from tkinter import *
# top = Tk()
# top.geometry("400x300")
# def fun ():
#     top1 = Toplevel(top)
#     top1.geometry("400x300")
#     top1.mainloop()
# btn1 = Button(top , text="Open" , command=fun)
# btn1.pack()
# top.mainloop()

