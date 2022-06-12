from tkinter import*
expression = ""
def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)
def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""
    except:
       equation.set("fied is empty??? ")
       expression = ""
def clear():
    global expression
    expression = ""
    equation.set("")
window=Tk()
window.geometry("500x600")
equation = StringVar()
title=window.title("GUI CALCULATOR...")
l1=Label(window,text="WELCOME TO GUI CALCULATOR",bg="red",fg="white",font=("Areal",15))
l1.place(x=100,y=35)
l11=Label(window,text="Feel Your Experience...!",fg="blue")
l11.place(x=200,y=70)
expression_field = Entry(window, textvariable=equation,font=("Areal",20))
expression_field.place(x=100,y=100)
b1=Button(window,text="1",width=5,activebackground="pink",borderwidth=10,relief="groove",bg="black",fg="white",font=("Areal",17),command=lambda: press(1))
b1.place(x=90,y=170)
b2=Button(window,text="2",activebackground="pink",width=5,borderwidth=10,relief="groove",bg="black",fg="white",font=("Areal",17),command=lambda: press(2))
b2.place(x=220,y=170)
b3=Button(window,text="3",activebackground="pink",width=5,borderwidth=10,relief="groove",bg="black",fg="white",font=("Areal",17),command=lambda: press(3))
b3.place(x=350,y=170)
b4=Button(window,text="4",activebackground="pink",width=5,borderwidth=10,relief="groove",bg="black",fg="white",font=("Areal",17),command=lambda: press(4))
b4.place(x=90,y=260)
b5=Button(window,text="5",activebackground="pink",width=5,borderwidth=10,relief="groove",bg="black",fg="white",font=("Areal",17),command=lambda: press(5))
b5.place(x=220,y=260)
b6=Button(window,text="6",activebackground="pink",width=5,borderwidth=10,relief="groove",bg="black",fg="white",font=("Areal",17),command=lambda: press(6))
b6.place(x=350,y=260)
b7=Button(window,text="7",activebackground="pink",width=5,borderwidth=10,relief="groove",bg="black",fg="white",font=("Areal",17),command=lambda: press(7))
b7.place(x=90,y=350)
b8=Button(window,text="8",activebackground="pink",width=5,borderwidth=10,relief="groove",bg="black",fg="white",font=("Areal",17),command=lambda: press(8))
b8.place(x=220,y=350)
b9=Button(window,text="9",activebackground="pink",width=5,borderwidth=10,relief="groove",bg="black",fg="white",font=("Areal",17),command=lambda: press(9))
b9.place(x=350,y=350)
b10=Button(window,text="-",activebackground="orange",width=5,borderwidth=10,relief="groove",bg="black",fg="white",font=("Areal",17),command=lambda: press("-"))
b10.place(x=90,y=440)
b11=Button(window,text="0",activebackground="pink",borderwidth=10,relief="groove",width=5,bg="black",fg="white",font=("Areal",17),command=lambda: press(0))
b11.place(x=220,y=440)
b12=Button(window,text="+",activebackground="orange",borderwidth=10,relief="groove",width=5,bg="black",fg="white",font=("Areal",17),command=lambda: press("+"))
b12.place(x=350,y=440)
b13=Button(window,text="CLEAR",activebackground="red",borderwidth=10,relief="raised",width=26,bg="red",fg="white",font=("Areal",17),command=clear)
b13.place(x=90,y=530)
b14=Button(window,text="=",width=10,bg="red",fg="white",font=("Areal",7),command=equalpress)
b14.place(x=420,y=110)
window.mainloop()
