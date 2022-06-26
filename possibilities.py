from tkinter import *
#programs to control the possiblities of  buttons


#for all operator buttons
def put_operator(got_str,oper,txt):
    T_indexval = len(got_str)-1
    print('t-index',T_indexval)
    if oper == '-' :
        if T_indexval == -1:
            return txt.insert('end',oper) #when there is nothing present ,and to give -ve values
        if got_str[T_indexval] == '-':
            messagebox.showerror('showerror','there is already a substract sign') #to avoid --2 kind of situations
        else:
            return txt.insert('end',oper)
                                                            #str is current string
    if got_str[T_indexval].isnumeric() == True or got_str[T_indexval] == ')' :   #oper is operator
        return txt.insert('end',oper)                  #txt is to make a link with text widget so to insert in it


#for all numbers buttons
def put_num(got_str, num,txt):
     flag = 1
     T_indexval = len(got_str)-1               #num is the corresponding number
     if len(got_str) == 0:                     #if there is no value in the text widget we need to add without a condition
         txt.insert('end',num)
         flag = 0
     if flag == 1:
         operators = got_str[T_indexval] =='+' or got_str[T_indexval] =='-' or got_str[T_indexval] =='*' or got_str[T_indexval] =='/'
         if got_str[T_indexval] == '(' or got_str[T_indexval] == '.' or got_str[T_indexval].isnumeric() == True or operators:
             return txt.insert('end',num)

#for zero we need to do a seperate function
def put_zero(got_str,txt):
    flag = 1
    T_indexval = len(got_str)-1
    if len(got_str) == 0:
        txt.insert('end','0')
        flag = 0
    if flag == 1:
        if got_str[T_indexval] == '/': #to show zero division error
             return 1
        operators = got_str[T_indexval] =='+' or got_str[T_indexval] =='-' or got_str[T_indexval] =='*'
        if got_str[T_indexval] == '(' or got_str[T_indexval] == '.' or got_str[T_indexval].isnumeric() == True or operators:
            return txt.insert('end','0')


#for dot button
def empty_dot(got_str,txt):
    if len(got_str) == 1 and got_str[0] == '\n': #if text widget is empty
        txt.insert('end','0.')


def num_dot(got_str,txt):
    flag = 1
    T_indexval = len(got_str)-1
    for i in range(T_indexval,-1,-1):
        if got_str[i].isnumeric() == False: #to put 11.11 kind of stuff single etc
            not_num = i
            flag = 0
            break
    if flag == 1:
        txt.insert('end','.')
    diff = T_indexval - not_num
    if flag == 0 and not_num != T_indexval and  diff >= 1: #to put dot like in case --> (1.2
        txt.insert('end','.')


def afternumeric_dot(got_str,txt):
    T_indexval = len(got_str)-1
    oper_openbrace_pos = 0
    dot_pos = 0

    for i in range(T_indexval,-1,-1):
        operators = got_str[i] == '+' or got_str[i] == '-' or got_str[i] == '*' or got_str[i] == '/' #to get the postion of operators and ( from backwards
        if got_str[i] == '('  or operators:
            oper_openbrace_pos = i
            break
    for i in range(T_indexval,-1,-1):
        if got_str[i] == '.':     #to get first occurence of dot in backwards
            dot_pos = i
            break

    needed_diff = oper_openbrace_pos - dot_pos  #to avoid situation (.
    if needed_diff >= 1 and got_str[T_indexval].isnumeric() == True:
        txt.insert('end','.')


#for open brace
def empty_open_brace(got_str,txt):
    if len(got_str) == 1 and got_str[0] == '\n':
        txt.insert('end','(')

def put_open_brace(got_str,txt):
    T_indexval = len(got_str)-1
    if len(got_str) >= 1:
        operators = got_str[T_indexval] == '+' or got_str[T_indexval] == '-' or got_str[T_indexval] == '*' or got_str[T_indexval] == '/'
        if got_str[T_indexval] == '(' or operators:
            txt.insert('end','(')


#for close brace
def put_close_brace(got_str,txt):
    T_indexval = len(got_str)-1
    open_count = 0
    close_count = 0
    num_check = 0

    for i in range(0,len(got_str)):
        if got_str[i] == '(':     #to get the count of ( occurence
            open_count += 1

    for i in range(0,len(got_str)):
        if got_str[i] == ')':     #to get the count of ) occurence
            close_count += 1

    if open_count != close_count and len(got_str) >=2 and got_str[T_indexval] != '.' : # to put close upto same open bracket
        txt.insert('end',')')                                                           #to avoid () and to avoid (0.)
