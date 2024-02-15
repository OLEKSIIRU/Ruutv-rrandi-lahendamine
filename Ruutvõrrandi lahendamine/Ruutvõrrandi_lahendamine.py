from importlib.metadata import entry_points
from tkinter import *
import tkinter as tk
import cmath
import numpy as np
import matplotlib.pyplot as plt

def check_and_solve():
    if ent.get() == "" or entr.get() == "" or enty.get() == "":
        ent.configure(bg="red" if ent.get() == "" else "white")
        entr.configure(bg="red" if entr.get() == "" else "white")
        enty.configure(bg="red" if enty.get() == "" else "white")
        v.configure(text="Ошибка: заполните все поля", bg="#FF0000")
    else:
        ent.configure(bg="white")
        entr.configure(bg="white")
        enty.configure(bg="white")
        try:
            a_val = float(ent.get())
            b_val = float(entr.get())
            c_val = float(enty.get())
            
            discriminant = (b_val ** 2) - (4 * a_val * c_val)
            sqrt_discriminant = cmath.sqrt(discriminant)
            
            root1 = (-b_val + sqrt_discriminant) / (2 * a_val)
            root2 = (-b_val - sqrt_discriminant) / (2 * a_val)

            root1_str = f"{root1.real:.2f}" if root1.imag == 0 else f"{root1:.2f}"
            root2_str = f"{root2.real:.2f}" if root2.imag == 0 else f"{root2:.2f}"
            
            v.configure(text=f"Корень 1: {root1_str}, Корень 2: {root2_str}", bg="#00FF00")
        except ValueError:
            v.configure(text="Ошибка: введите числовые значения для коэффициентов a, b, c", bg="#FF0000")

def graafik():
    ent=float(a.get())
    entr=float(b.get())
    enty=float(c.get())
    x0=(-entr)/2*ent
    y0=ent*x0*x0+entr*x0+enty
    x=np.arrange(x0-15,x0+15,1) #min,max,st
    y=ent*x*x*entr*x+enty
    fig=plt.figure()
    plt.plot(x,y,'r-d')
    plt.title("Ruutvõrrand")
    plt.ylabel('Y')
    plt.xlabel('X')
    plt.grid(True)
    plt.show()



aken = tk.Tk()
aken.geometry("1200x800")
aken.title("Решение квадратного уравнения")
aken.iconbitmap("graph_analytics_icon_261465.ico") 

f = Frame(aken, bg="#E0FFFF", border=10, height=1, width=16)
f.grid(row=0, column=0)  

l = Label(f, text="Решение квадратного уравнения", bg="#0000CD", fg="#FFFFFF", font="Algerian 14", height=3, width=50)
l.grid(row=0, column=1, columnspan=7)  

v = Label(f, text="Решение ", bg="#0000CD", fg="#FFFFFF", font="Algerian 24", height=3, width=54)
v.grid(row=2, column=0, columnspan=7)  

a = Label(f, text="x**2+", bg="#0000CD", fg="#FFFFFF", font="Algerian 24", height=3, width=4)
a.grid(row=1, column=1)  

ent = Entry(f) 
ent.grid(row=1, column=0)  

b = Label(f, text="x+", bg="#0000CD", fg="#FFFFFF", font="Algerian 24", height=3, width=4)
b.grid(row=1, column=3)  

entr = Entry(f)
entr.grid(row=1, column=2)  

c = Label(f, text="=0", bg="#0000CD", fg="#FFFFFF", font="Algerian 24", height=3, width=4)
c.grid(row=1, column=5)  

enty = Entry(f)
enty.grid(row=1, column=4)  

btn = Button(f, text="Решить", font="Arial 18", bg="#00FFFF", relief=RAISED, command=check_and_solve) 
btn.grid(row=1, column=6)  

aken.mainloop()
