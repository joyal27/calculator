#programs to control the possiblities of  buttons


#for all operator buttons
def put_operator(str,oper,txt):
    T_indexval = len(str)-1                                     #str is current string
    if str[T_indexval].isnumeric() == True or str[T_indexval] == ')' :   #oper is operator
        return txt.insert('end',oper)                  #txt is to make a link with text widget so to insert in it


#for all numbers buttons
def put_num(str, num,txt):
     flag = 1
     T_indexval = len(str)-1                                   #num is the corresponding number
     if len(str) == 0:                                #if there is no value in the text widget we need to add without a condition
         txt.insert('end',num)
         flag = 0
     if flag == 1:
         conditions=str[T_indexval] =='+' or str[T_indexval] =='-' or str[T_indexval] =='*' or str[T_indexval] =='/'
         if str[T_indexval] == '(' or str[T_indexval] == '.' or str[T_indexval].isnumeric() == True or conditions:
             return txt.insert('end',num)


#for dot button
def empty_dot(str,txt):
    if str[0] == '\n':
        txt.insert('end','0.')
