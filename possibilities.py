from tkinter import *
#programs to control the possiblities of  buttons

#for all operator buttons
def put_operator(got_str,oper,txt):
    T_indexval = len(got_str)-1   #oper is operator
                                  #txt is to make a link with text widget so to insert in it
    slice_error = 0       #if there is nothing in the text there will be slicing error in the 21st line
                                  
    if oper == '-' :
        if T_indexval == -1:
            return txt.insert('end',oper) #when there is nothing present ,and to give -ve values
        if got_str[T_indexval] == '-':
            messagebox.showerror('showerror','there is already a substract sign') #to avoid --2 kind of situations
        else:
            return txt.insert('end',oper)

    if T_indexval == -1:
        slice_error = 1

    if slice_error == 0:
      if got_str[T_indexval].isnumeric() == True or got_str[T_indexval] == ')' :
          return txt.insert('end',oper)                 #operators work only when there is a number or ")"

#for all numbers buttons
def put_num(got_str, num,txt):
     flag = 1
     T_indexval = len(got_str)-1               #num is the corresponding number
     if len(got_str) == 0:            #if there is no value in the text widget we need to add without a condition
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
    if len(got_str) == 1 and got_str[0] == '\n': #if text widget is empty in that case there will be \n present
        txt.insert('end','0.')                   #when '.' clicked in empty case we place dot in widget as '0.'


def notempty_dot(got_str,txt):
    openbrac_operator = 0
    closebrac = 0
    dot_found = 0
    openbrac_operator_pos = 0
    openbrac_operator_diff = 0
    closebrac_pos = 0
    closebrac_diff = 0
    T_indexval = len(got_str)-1

    for i in range(T_indexval,-1,-1):
        operators = got_str[i] == '+' or got_str[i] == '-' or got_str[i] == '*' or got_str[i] == '/'
        if got_str[i] == '(' or operators:
            openbrac_operator_pos = i
            openbrac_operator_diff = T_indexval - openbrac_operator_pos #For the situations (1.,+1. and not for (.,+.
            openbrac_operator = 1
            break
        if got_str[i] == ')':
            closebrac_pos = i
            closebrac_diff = T_indexval - closebrac_pos #For the situation )+1. and to escape )+. and ).
            closebrac = 1
            break
        if got_str[i] == '.':
            dot_found = 1
            break

#now to apply conditions based on them
    if openbrac_operator == 1 and openbrac_operator_diff >= 1:
        txt.insert('end','.')
    if closebrac == 1 and closebrac_diff >= 2:
        txt.insert('end','.')
    if openbrac_operator == 0 and closebrac == 0 and dot_found == 0: #In this case there maybe (0.) or there maybe numbers only without dot
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
