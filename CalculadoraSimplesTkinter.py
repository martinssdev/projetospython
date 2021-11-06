from tkinter import *

root = Tk()
root.title("Calculadora Simples")

e= Entry(root,width=35,borderwidth=5)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)


def button_add(number):
    #e.delete(0,END)
    current = e.get()
    e.delete(0,END)
    e.insert(0, str(current) + str(number))


def button_clear():
    e.delete(0,END)
    
def button_soma():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    e.delete(0,END)
    


def button_equal():
    second_number = e.get()
    e.delete(0,END)
    if math == "addition":
        e.insert(0, f_num+int(second_number))
    elif math == "subtraction":
        e.insert(0,f_num - int(second_number))
    elif math == "multiply":
        e.insert(0,f_num * int(second_number))
    elif math == "divide":
        e.insert(0,f_num / int(second_number))

def button_sub():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    e.delete(0,END)


def button_mult():
    first_number = e.get()
    global f_num
    global math
    math = "multiply"
    f_num = int(first_number)
    e.delete(0,END)


def button_div():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    e.delete(0,END)

b1 = Button(root,text='1',padx=40,pady=20,command=lambda: button_add(1))
b2 = Button(root,text='2',padx=40,pady=20,command=lambda:button_add(2))
b3 = Button(root,text='3',padx=40,pady=20,command=lambda:button_add(3))
b4 = Button(root,text='4',padx=40,pady=20,command=lambda:button_add(4))
b5 = Button(root,text='5',padx=40,pady=20,command=lambda:button_add(5))
b6 = Button(root,text='6',padx=40,pady=20,command=lambda:button_add(6))
b7 = Button(root,text='7',padx=40,pady=20,command=lambda:button_add(7))
b8 = Button(root,text='8',padx=40,pady=20,command=lambda:button_add(8))
b9 = Button(root,text='9',padx=40,pady=20,command=lambda:button_add(9))
b0 = Button(root,text='0',padx=40,pady=20,command=lambda:button_add(0))
b_add = Button(root,text='+',padx=39,pady=2,command=lambda:button_soma())
b_sub = Button(root,text='-',padx=41,pady=3,command=button_sub)
b_mult = Button(root,text='*',padx=41,pady=4,command=button_mult)
b_divide = Button(root,text='/',padx=40,pady=3,command=button_div)
b_equal = Button(root,text='=',padx=91,pady=2,command=button_equal)
b_clear = Button(root,text='CE',padx=79,pady=2,command=lambda:button_clear())

b1.grid(row= 3, column=0)
b2.grid(row= 3, column=1)
b3.grid(row= 3, column=2)
b4.grid(row= 2, column=0)
b5.grid(row= 2, column=1)
b6.grid(row= 2, column=2)
b7.grid(row= 1, column=0)
b8.grid(row= 1, column=1)
b9.grid(row= 1, column=2)
b0.grid(row= 4, column=0)

b_add.grid(row=5,column=0)
b_clear.grid(row=4,column=1,columnspan=2)
b_equal.grid(row=5,column=1,columnspan=2)
b_sub.grid(row=6,column=0)
b_divide.grid(row=6,column=2)
b_mult.grid(row=6,column=1)


root.mainloop()
