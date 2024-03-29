from tkinter import *
import parser

root=Tk()
root.title("Calculator")

#get the user input and place it in the text field
i=0
def get_variables(num):
    global i
    display.insert(i,num)
    i+=1

def all_clear():
    display.delete(0,END)

def undo():
    entire_string=display.get()
    if len(entire_string):
        new_string = entire_string[:-1]
        all_clear()
        display.insert(0,new_string)
    else:
        all_clear()
        display.insert(0,"Error")

def get_operator(operator):
    global i
    length=len(operator)
    display.insert(i, operator)
    i+=length

def calculate():
    entire_string=display.get()
    try:

        a=parser.expr(entire_string).compile()
        result=eval(a)
        all_clear()
        display.insert(0,result)
    except Exception:
        all_clear()
        display.insert(0,"Error")

def factorial():
    global f
    n = display.get()
    n = int(n)
    f=1
    for i in range(1,n+1):
        f = f * i
    all_clear()
    display.insert(0, f)

#adding the input field
display = Entry(root)
display.grid(row=1, columnspan = 6, sticky = W+E)

#adding buttons
Button(root, text="1", command=lambda :get_variables(1)).grid(row=2,column=0)
Button(root, text="2", command=lambda :get_variables(2)).grid(row=2,column=1)
Button(root, text="3", command=lambda :get_variables(3)).grid(row=2,column=2)

Button(root, text="4", command=lambda :get_variables(4)).grid(row=3,column=0)
Button(root, text="5", command=lambda :get_variables(5)).grid(row=3,column=1)
Button(root, text="6", command=lambda :get_variables(6)).grid(row=3,column=2)

Button(root, text="7", command=lambda :get_variables(7)).grid(row=4,column=0)
Button(root, text="8", command=lambda :get_variables(8)).grid(row=4,column=1)
Button(root, text="9", command=lambda :get_variables(9)).grid(row=4,column=2)

Button(root, text="0", command=lambda :get_variables(0)).grid(row=5,column=0)
Button(root, text="AC", command=lambda :all_clear()).grid(row=5,column=1)
Button(root, text="=",command=lambda :calculate()).grid(row=5,column=2)

Button(root, text="+",command=lambda :get_operator("+")).grid(row=2,column=3)
Button(root, text="-",command=lambda :get_operator("-")).grid(row=3,column=3)
Button(root, text="*",command=lambda :get_operator("*")).grid(row=4,column=3)
Button(root, text="/",command=lambda :get_operator("/")).grid(row=5,column=3)

#addin new operations
Button(root, text="pi",command=lambda :get_operator("*3.14")).grid(row=2,column=4)
Button(root, text="%",command=lambda :get_operator("%")).grid(row=3,column=4)
Button(root, text="(",command=lambda :get_operator("(")).grid(row=4,column=4)
Button(root, text="exp",command=lambda :get_operator("**")).grid(row=5,column=4)

Button(root, text="<-", command=lambda:undo()).grid(row=2,column=5)
Button(root, text="x!", command = lambda : factorial()).grid(row=3,column=5)
Button(root, text=")",command=lambda :get_operator(")")).grid(row=4,column=5)
Button(root, text="^2",command=lambda :get_operator("**2")).grid(row=5,column=5)

root.mainloop()



