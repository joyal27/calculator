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
         operators = str[T_indexval] =='+' or str[T_indexval] =='-' or str[T_indexval] =='*' or str[T_indexval] =='/'
         if str[T_indexval] == '(' or str[T_indexval] == '.' or str[T_indexval].isnumeric() == True or operators:
             return txt.insert('end',num)


#for dot button
def empty_dot(str,txt):
    if len(str) == 1 and str[0] == '\n': #if text widget is empty
        txt.insert('end','0.')


def num_dot(str,txt):
    flag = 1
    T_indexval = len(str)-1
    for i in range(T_indexval,-1,-1):
        if str[i].isnumeric() == False: #to put 11.11 kind of stuff single etc
            not_num = i
            flag = 0
            break
    if flag == 1:
        txt.insert('end','.')
    diff = T_indexval - not_num
    if flag == 0 and not_num != T_indexval and  diff >= 1: #to put dot like in case --> (1.2 
        txt.insert('end','.')


def afternumeric_dot(str,txt):
    T_indexval = len(str)-1
    oper_openbrace_pos = 0
    dot_pos = 0

    for i in range(T_indexval,-1,-1):
        operators = str[i] == '+' or str[i] == '-' or str[i] == '*' or str[i] == '/' #to get the postion of operators and ( from backwards
        if str[i] == '('  or operators:
            oper_openbrace_pos = i
            break
    for i in range(T_indexval,-1,-1):
        if str[i] == '.':     #to get first occurence of dot in backwards
            dot_pos = i
            break

    needed_diff = oper_openbrace_pos - dot_pos  #to avoid situation (.
    if needed_diff >= 1 and str[T_indexval].isnumeric() == True:
        txt.insert('end','.')


#for open brace
def empty_open_brace(str,txt):
    if len(str) == 1 and str[0] == '\n':
        txt.insert('end','(')

def put_open_brace(str,txt):
    T_indexval = len(str)-1
    operators = str[T_indexval] == '+' or str[T_indexval] == '-' or str[T_indexval] == '*' or str[T_indexval] == '/'
    if operators:
        txt.insert('end','(')


#for close brace
def open_check_close(str):
    open_brace_pos = 0
    close_brace_pos = 0
    T_indexval = len(str)-1
    local_flag = 0

    for i in range(T_indexval,-1,-1):
        if str[i] == '(':
            open_brace_pos = i
            local_flag = 1
            break                      #To check that a open brace is there without a closing brace and
    for i in range(T_indexval,-1,-1):   #also to avoid taking open brace which have closing brace i.e:(1+2)+2
        if str[i] == ')':
            close_brace_pos = i
            break

    if local_flag == 1: # if open brace comes in the start without a closing brace
        open_brace_pos = 1

    brace = open_brace_pos - close_brace_pos
    if brace >= 1 :
        return 1
    if brace == 0:
        return 0



def put_close_brace(str,txt,flag):
    T_indexval = len(str)-1
    if str[T_indexval].isnumeric() == True and flag == 1:
        txt.insert('end',')')
