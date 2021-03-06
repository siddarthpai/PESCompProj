from tkinter import *
root = Tk()
root.title("Simple Calculator")
e= Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))


def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number) )
    pass

def button_clear():
    e.delete(0, END)

def button_add():
    c = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(c)
    e.delete(0, END)

def button_sub():
    c=e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(c)
    e.delete(0, END)

def button_mul():
    c=e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(c)
    e.delete(0, END)

def button_div():
    c=e.get()
    global f_num
    global math
    math = "division"
    f_num = int(c)
    e.delete(0, END)

def button_equal():
    if math == 'addition':
        sec_num = e.get()
        e.delete(0, END)
        e.insert(0, f_num + int(sec_num))
    elif math == 'subtraction':
        sec_num = e.get()
        e.delete(0, END)
        e.insert(0, f_num - int(sec_num))
    elif math == 'multiplication':
        sec_num = e.get()
        e.delete(0, END)
        e.insert(0, f_num * int(sec_num))
    elif math == 'division':
        sec_num = e.get()
        e.delete(0, END)
        e.insert(0, int(f_num / int(sec_num)))


button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
button_eq = Button(root, text='=', padx=91, pady=20, command=lambda: button_equal())
button_ad = Button(root, text='+', padx=39, pady=20, command=lambda: button_add())
button_su = Button(root, text='-', padx=39, pady=20, command=lambda: button_sub())
button_mu = Button(root, text='*', padx=39, pady=20, command=lambda: button_mul())
button_di = Button(root, text='/', padx=39, pady=20, command=lambda: button_div())
button_clr = Button(root, text='clr', padx=90, pady=20, command=button_clear)

# PUT BUTTONS ON SCREEN
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=1)

button_eq.grid(row=6, column=1, columnspan=2)
button_ad.grid(row=4, column=0)
button_su.grid(row=5, column=0)
button_mu.grid(row=5, column=1)
button_di.grid(row=5, column=2)
button_clr.grid(row=4, column=1, columnspan=2)
root,mainloop()
