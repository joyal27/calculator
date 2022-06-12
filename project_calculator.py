from tkinter import *

window=Tk()
window.geometry('180x230')
window.title('Calculator')
window.config(bg='red')



def hello():
    print('button clicked')

def enter_zero():
    text.get(0,'end')





frame1=Frame(window,bg='yellow')

text=Text(window,width=24,height=6)


#Creating buttons for numbers
button0=Button(frame1,text='0',width=5,height=1,command=enter_zero)
button1=Button(frame1,text='1',width=5,height=1)
button2=Button(frame1,text='2',width=5,height=1)
button3=Button(frame1,text='3',width=5,height=1)
button4=Button(frame1,text='4',width=5,height=1)
button5=Button(frame1,text='5',width=5,height=1)
button6=Button(frame1,text='6',width=5,height=1)
button7=Button(frame1,text='7',width=5,height=1)
button8=Button(frame1,text='8',width=5,height=1)
button9=Button(frame1,text='9',width=5,height=1)

#creating buttons for symbols
cancel=Button(frame1,text='C',width=5,height=1)
equal=Button(frame1,text='=',width=5,height=1)
dot=Button(frame1,text='.',width=5,height=1)
bracopen=Button(frame1,text='(',width=5,height=1)
bracclose=Button(frame1,text=')',width=5,height=1)
singledelete=Button(frame1,text='<--',width=5,height=1)

#creating buttons for operators
plus=Button(frame1,text='+',width=5,height=1)
subtct=Button(frame1,text='-',width=5,height=1)
multipl=Button(frame1,text='x',width=5,height=1)
div=Button(frame1,text='/',width=5,height=1)








#positioning of button inside  grid
plus.grid(row=0,column=0)
bracopen.grid(row=0,column=1)
bracclose.grid(row=0,column=2)
singledelete.grid(row=0,column=3)

subtct.grid(row=1,column=0)
button1.grid(row=1,column=1)   #when we use grid we don't need to type button2.pack()
button2.grid(row=1,column=2)
button3.grid(row=1,column=3)


multipl.grid(row=2,column=0)
button4.grid(row=2,column=1)
button5.grid(row=2,column=2)
button6.grid(row=2,column=3)

div.grid(row=3,column=0)
button7.grid(row=3,column=1)
button8.grid(row=3,column=2)
button9.grid(row=3,column=3)


cancel.grid(row=4,column=0)
dot.grid(row=4,column=1)
button0.grid(row=4,column=2)
equal.grid(row=4,column=3)
























text.pack()
frame1.place(x=0,y=100)
window.mainloop()