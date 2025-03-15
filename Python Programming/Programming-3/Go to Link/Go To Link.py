from tkinter import *
import webbrowser
root = Tk()
root.geometry("400x300")
root.title("Go To Link")
labelTitle = Label(root, text="Go To Link" , bg="#34B626" , fg="#D5DE30")
labelTitle.pack()
labelLink = Label(root, text="Enter a link" , bg="#34B626" , fg="#D12B29")
labelLink.pack()
entryLink = Entry(root)
entryLink.pack()
def call_link():
    link = entryLink.get()
    webbrowser.open(link)
buttonLink = Button(root, text="Go", command=call_link)
buttonLink.pack()
root.mainloop()