from tkinter import*
expression=""
def press(num):
    global expression
    expression=expression+str(num)
    equation.set(expression)
def equalpress():
    try:
        global expression
        total=str(eval(expression))
        equation.set(total)
        expression=""
    except:
        equation.set("error")
        expression=""
def clear():
    global expression
    expression=""
    equation.set("")
root=Tk()
root.title("Calculator")
root.geometry("500x400")
root.configure(background='black')
equation=StringVar()
txt=Entry(root,textvariable=equation,font=("Comic Sans MS",20),
          bd=10,justify='right')
txt.grid(columnspan=4,ipadx=40,ipady=20)
button1=Button(root,text='1',fg='black',
               command=lambda:press(1),height=6,width=12)
button1.grid(row=2,column=0,padx=5,pady=5)

button2=Button(root,text='2',fg='black',
               command=lambda:press(2),height=6,width=12)
button2.grid(row=2,column=1,padx=5,pady=5)

button3=Button(root,text='3',fg='black',
               command=lambda:press(3),height=6,width=12)
button3.grid(row=2,column=2,padx=5,pady=5)

button4=Button(root,text='4',fg='black',
               command=lambda:press(4),height=6,width=12)
button4.grid(row=3,column=0,padx=5,pady=5)

button5=Button(root,text='5',fg='black',
               command=lambda:press(5),height=6,width=12)
button5.grid(row=3,column=1,padx=5,pady=5)

button6=Button(root,text='6',fg='black',
               command=lambda:press(6),height=6,width=12)
button6.grid(row=3,column=2,padx=5,pady=5)

button7=Button(root,text='7',fg='black',
               command=lambda:press(7),height=6,width=12)
button7.grid(row=4,column=0,padx=5,pady=5)

button8=Button(root,text='8',fg='black',
               command=lambda:press(8),height=6,width=12)
button8.grid(row=4,column=1,padx=5,pady=5)

button9=Button(root,text='9',fg='black',
               command=lambda:press(9),height=6,width=12)
button9.grid(row=4,column=2,padx=5,pady=5)

dot=Button(root,text='.',fg='black',
               command=lambda:press('.'),height=6,width=12)
dot.grid(row=5,column=0,padx=5,pady=5)

button0=Button(root,text='0',fg='black',
               command=lambda:press(0),height=6,width=12)
button0.grid(row=5,column=1,padx=5,pady=5)

equal=Button(root,text='=',fg='black',
              command=equalpress,height=6,width=12)
equal.grid(row=5,column=2,padx=5,pady=5)

addition=Button(root,text='+',fg='black',
                command=lambda:press("+"),height=6,width=12)
addition.grid(row=2,column=3,padx=5,pady=5)

subtract=Button(root,text='-',fg='black',
                command=lambda:press("-"),height=6,width=12)
subtract.grid(row=3,column=3,padx=5,pady=5)

multiply=Button(root,text='*',fg='black',
                command=lambda:press("*"),height=6,width=12)
multiply.grid(row=4,column=3,padx=5,pady=5)

divide=Button(root,text='/',fg='black',
              command=lambda:press("/"),height=6,width=12)
divide.grid(row=5,column=3,padx=5,pady=5)

clear=Button(root,text='Clear',fg='black',
             command=clear,height=6,width=12)
clear.grid(row=6,column=3)
root.mainloop()