#calculator using tkinter 

from tkinter import *

window=Tk()
window.geometry('180x230')
window.title('Calculator')
window.config(bg='red')

#fucntions for the buttons

def enter_zero():
    text.insert('end','0')

def enter_one():
    text.insert('end','1')

def enter_two():
    text.insert('end','2')

def enter_three():
    text.insert('end','3')

def enter_four():
    text.insert('end','4')

def enter_five():
    text.insert('end','5') 

def enter_six():
    text.insert('end','6')

def enter_seven():
    text.insert('end','7')

def enter_eight():
    text.insert('end','8')

def enter_nine():
    text.insert('end','9')    

#functions for operator buttons

def enter_add():
    text.insert('end','+') 

def enter_substract():
    text.insert('end','-')

def enter_multiple():
    text.insert('end','*')

def enter_division():
    text.insert('end','/')    

#functions for other buttons

def cancelled():
    text.delete('1.0','end')

def equalto():
    pass 

def enter_dot():
    text.insert('end','.') 

def bracket_open():
    text.insert('end','(' ) 

def bracket_close():
    text.insert('end',')')

def previous_entry():
   string=text.get('1.0','end')
   x=len(string)-1
   print('x',x)
   string=string[0:x-1]
   print('new',string)
   text.delete('1.0','end')
   text.insert('end',string)











frame1=Frame(window,bg='yellow')
text=Text(window,width=24,height=6)


#Creating buttons for numbers
button0=Button(frame1,text='0',width=5,height=1,command=enter_zero)
button1=Button(frame1,text='1',width=5,height=1,command=enter_one)
button2=Button(frame1,text='2',width=5,height=1,command=enter_two)
button3=Button(frame1,text='3',width=5,height=1,command=enter_three)
button4=Button(frame1,text='4',width=5,height=1,command=enter_four)
button5=Button(frame1,text='5',width=5,height=1,command=enter_five)
button6=Button(frame1,text='6',width=5,height=1,command=enter_six)
button7=Button(frame1,text='7',width=5,height=1,command=enter_seven)
button8=Button(frame1,text='8',width=5,height=1,command=enter_eight)
button9=Button(frame1,text='9',width=5,height=1,command=enter_nine)

#creating buttons for symbols
cancel=Button(frame1,text='C',width=5,height=1,command=cancelled)
equal=Button(frame1,text='=',width=5,height=1,command=equalto)
dot=Button(frame1,text='.',width=5,height=1,command=enter_dot)
bracopen=Button(frame1,text='(',width=5,height=1,command=bracket_open)
bracclose=Button(frame1,text=')',width=5,height=1,command=bracket_close)
singledelete=Button(frame1,text='<--',width=5,height=1,command=previous_entry)

#creating buttons for operators
plus=Button(frame1,text='+',width=5,height=1,command=enter_add)
subtct=Button(frame1,text='-',width=5,height=1,command=enter_substract)
multipl=Button(frame1,text='x',width=5,height=1,command=enter_multiple)
div=Button(frame1,text='/',width=5,height=1,command=enter_division)








#positioning of button inside  grid
plus.grid(row=0,column=0)
bracopen.grid(row=0,column=1)
bracclose.grid(row=0,column=2)
singledelete.grid(row=0,column=3)

subtct.grid(row=1,column=0)
button1.grid(row=1,column=1)   
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