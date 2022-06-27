#calculator using tkinter
from tkinter import *
from tkinter import messagebox
import platform

import possibilities as pos
import equaltofunctions as equ



window=Tk()

my_os = platform.system()
if my_os == 'Windows':
    window.geometry('180x230')
    window.resizable(0,0)
else:
    window.geometry('176x262')
    window.resizable(0,0)


window.title('Calculator')
window.config(bg='red')


#function for getting string without newline
def get_string():
    string=text.get('1.0','end')
    string=string.rstrip() #to remove the new line inside the string
    return string


#fucntions for the number buttons

def enter_zero():
    problem_div = pos.put_zero(get_string(),text)
    if problem_div == 1:
        messagebox.showerror('showerror','can\'t divide by zero')
def enter_one():
    pos.put_num(get_string(),'1',text)

def enter_two():
    pos.put_num(get_string(),'2',text)

def enter_three():
    pos.put_num(get_string(),'3',text)

def enter_four():
    pos.put_num(get_string(),'4',text)

def enter_five():
    pos.put_num(get_string(),'5',text)

def enter_six():
    pos.put_num(get_string(),'6',text)

def enter_seven():
    pos.put_num(get_string(),'7',text)

def enter_eight():
    pos.put_num(get_string(),'8',text)

def enter_nine():
    pos.put_num(get_string(),'9',text)


#functions for operator buttons

def enter_add():
   pos.put_operator( get_string(),'+',text)

def enter_substract():
   pos.put_operator( get_string(),'-',text)

def enter_multiple():
   pos.put_operator( get_string(),'*',text)

def enter_division():
   pos.put_operator( get_string(),'/',text)


#functions for other buttons

def cancelled():
    text.delete('1.0','end')

def equalto():
    flag = equ.last_nonnum(get_string())
    got_str = equ.brackets(get_string(),flag,text)
    final_str = equ.operations(got_str,flag,text)

    if flag != None: #in cases like '1+' flag will be None so to escape from it
        text.delete('1.0','end')
        text.insert('end',final_str)



def enter_dot():
    pos.empty_dot(text.get('1.0','end'),text)
    pos.num_dot(get_string(),text)
    pos.afternumeric_dot(get_string(),text)

def bracket_open():
    pos.put_open_brace(get_string(),text)
    pos.empty_open_brace(text.get('1.0','end'),text)

def bracket_close():
    pos.put_close_brace(get_string(),text)

def previous_entry():
  string=get_string()
  x=len(string)-1
  string=string[0:x]
  text.delete('1.0','end')
  text.insert('end',string)


frame1=Frame(window,bg='yellow')
text=Text(window,width=22,height=6)


#Creating buttons for numbers
button0=Button(frame1,text='0',width=2,height=1,command=enter_zero)

button1=Button(frame1,text='1',width=2,height=1,command=enter_one)

button2=Button(frame1,text='2',width=2,height=1,command=enter_two)

button3=Button(frame1,text='3',width=2,height=1,command=enter_three)

button4=Button(frame1,text='4',width=2,height=1,command=enter_four)

button5=Button(frame1,text='5',width=2,height=1,command=enter_five)

button6=Button(frame1,text='6',width=2,height=1,command=enter_six)

button7=Button(frame1,text='7',width=2,height=1,command=enter_seven)

button8=Button(frame1,text='8',width=2,height=1,command=enter_eight)

button9=Button(frame1,text='9',width=2,height=1,command=enter_nine)



#creating buttons for symbols
cancel=Button(frame1,text='C',width=2,height=1,command=cancelled)

equal=Button(frame1,text='=',width=2,height=1,command=equalto)

dot=Button(frame1,text='.',width=2,height=1,command=enter_dot)

bracopen=Button(frame1,text='(',width=2,height=1,command=bracket_open)

bracclose=Button(frame1,text=')',width=2,height=1,command=bracket_close)

singledelete=Button(frame1,text='<--',width=2,height=1,command=previous_entry)



#creating buttons for operators
plus=Button(frame1,text='+',width=2,height=1,command=enter_add)

subtct=Button(frame1,text='-',width=2,height=1,command=enter_substract)

multipl=Button(frame1,text='x',width=2,height=1,command=enter_multiple)

div=Button(frame1,text='/',width=2,height=1,command=enter_division)








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
frame1.place(x=0,y=107)
window.mainloop()
