from tkinter import *
root = Tk()
root.title("ألة حاسبة ")
root.geometry("300x400")
root.resizable(0,0)
root.configure(bg="black")
e = Entry(root, bd=10,width=30, font="Arial 21", bg="LightGrey")
def click(number):
    e.insert(32, number)

def add():
    e.insert(32, "+")

def clear():
    e.delete(0, END)

def equle():
    current = e.get()
    list = current.split("+")
    result = int(list[0]) + int(list[1])
    clear()
    e.insert(32, result)

e.pack()
btnl =Button(root, text="7",font="Arial 18 bold",bg="Grey", bd=10,padx=10,pady=5, command=lambda : click(7))
btnl.place(x=10,y=60)
btn2 =Button(root, text="8",font="Arial 18 bold",bg="Grey", bd=10,padx=10,pady=5, command=lambda : click(8))
btn2.place(x=85,y=60)
btn3 =Button(root, text="9",font="Arial 18 bold",bg="Grey", bd=10,padx=10,pady=5 , command=lambda : click(9))
btn3.place(x=160,y=60)
btn4 =Button(root, text="4",font="Arial 18 bold",bg="Grey", bd=10,padx=10,pady=5 ,command=lambda : click(4)) 
btn4.place(x=10,y=145)
btn5 =Button(root, text="5",font="Arial 18 bold",bg="Grey", bd=10,padx=10,pady=5 ,command=lambda : click(5))
btn5.place(x=85,y=145)
btn6 =Button(root, text="6",font="Arial 18 bold",bg="Grey", bd=10,padx=10,pady=5 , command=lambda : click(6))
btn6.place(x=160,y=145)
btn7 =Button(root, text="1",font="Arial 18 bold",bg="Grey", bd=10,padx=10,pady=5 , command=lambda : click(1))
btn7.place(x=10,y=230)
btn8 =Button(root, text="2",font="Arial 18 bold",bg="Grey", bd=10,padx=10,pady=5 , command=lambda : click(2))
btn8.place(x=85,y=230)
btn9 =Button(root, text="3",font="Arial 18 bold",bg="Grey", bd=10,padx=10,pady=5 , command=lambda : click(3))
btn9.place(x=160,y=230)
btn10 =Button(root, text="0",font="Arial 18 bold",bg="Grey", bd=10,padx=10,pady=5 , command=lambda : click(0))
btn10.place(x=10,y=320)


btn11 =Button(root, text="+",font="Arial 18 bold", height=4, bd=10, bg="crimson", command= add())
btn11.place(x=235,y=60)

btn12 =Button(root, text="c",font="Arial 18 bold", width=8, height=1, bd=10, bg="skyBlue", command= clear())
btn12.place(x=85,y=320)

btn13 =Button(root, text="=",font="Arial 18 bold", height=4, bd=10, bg="khaki", command= equle())
btn13.place(x=235,y=230)

root.mainloop()