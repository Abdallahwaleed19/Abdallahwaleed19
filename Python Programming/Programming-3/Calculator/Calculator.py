from tkinter import *
from functools import partial
def call_result(label_result, n1, n2): 
    num1 = (n1.get())
    num2 = (n2.get())
    result = int(num1)+int(num2) 
    label_result.config(text="Result is %d" % result) 
    return
root = Tk() 
root.geometry('400x200') 
root.title('Simple Calculator') 
number1 = StringVar()
number2 = StringVar()
labelTitle = Label(root, text="Simple Calculator" , bg="#34B626" , fg="#D5DE30")
labelTitle.grid(row=0, column=2)
labelNum1 = Label(root, text="Enter a number" , bg="#34B626" , fg="#D12B29")
labelNum1.grid(row=1, column=0)
labelNum2 = Label(root, text="Enter another number" , bg="#34B626" , fg="#D12B29")
labelNum2.grid(row=2,column=0)
labelResult = Label(root) 
labelResult.grid(row=7, column=2)
entryNum1 = Entry(root, textvariable=number1)
entryNum1.grid(row=1, column=2)
entryNum2 = Entry(root, textvariable=number2)
entryNum2.grid(row=2, column=2)
call_result = partial(call_result, labelResult, number1, number2)
buttonCal = Button(root, text="Calculate", 
command=call_result).grid(row=3, column=0)
root.mainloop()