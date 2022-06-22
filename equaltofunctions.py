from tkinter import messagebox
#different operation functions


#the main issue in any_operator_taker only need to focus there as the case is str showes None after getting there



#to calculate inside brackets
def brackets(got_str,txt,flag):
    if flag == 1:
        bracket_found = 0
        open_bracket_list = list()
        close_bracket_list = list()
        open_close_same = 0
        close_pos = 0
        operators_found = 0
        operation_part = ''

        #to check whether there is a open bracket present
        for i in range(0,len(got_str)):
            if got_str[i] == '(':
                bracket_found = 1
                break

        if bracket_found == 0  :

            return got_str,1
                          #if there is no bracket then there may be operators
        if bracket_found == 1:
            #to take the position of open brackets
            for i in range(0,len(got_str)):
                if got_str[i] == '(':
                    open_bracket_list.append(i)
                    #to take the position of close brackets
            for i in range(0,len(got_str)):
                if got_str[i] == ')':
                    close_bracket_list.append(i)
                    #to check if the count of open and close bracket is same
        if len(open_bracket_list) == len(close_bracket_list):
                open_close_same = 1
        else:
            messagebox.showerror('showerror','closing bracket not matching with open bracket')

        if open_close_same == 1:
            #from the open list we take from last index and we check in close list until the
            # position of close bracket from the list is larger
            while open_bracket_list[len(open_bracket_list)-1] > close_bracket_list[close_pos]:
                close_pos += 1
            #now to take only that part of inside the bracket and store others until we join after operations
            try:
                left_part = got_str[0:open_bracket_list[len(open_bracket_list)-1]]
            except :
                left_part = ''



            try :
                right_part = got_str[close_bracket_list[close_pos+1]:]
            except :
                right_part = ''
            operation_part = got_str[(open_bracket_list[len(open_bracket_list)-1])+1:close_bracket_list[close_pos]]

            #now to check if any operator is present in the operation_part
            for i in range(0,len(operation_part)):
                operators = got_str[i] == '+' or got_str[i] == '-' or got_str[i] == '*' or got_str[i] == '/'
                if operators:
                    operators_found = 1
        if operators_found == 0:
            got_str = left_part + operation_part + right_part
            open_bracket_list = []
            close_bracket_list = []
            brackets(got_str,txt,1) #to loop until only numeric values left
        if operators_found ==1:

            operation_part = operations(operation_part,2,txt)

            got_str = left_part + operation_part + right_part
            open_bracket_list = []
            close_bracket_list = []
            brackets(got_str,txt,1)#to loop until inside part of bracket is only numeric left and without brackets














def operations(got_str,numbers,txt):
    if numbers == 1:

        str = division(got_str)
        str = multiplication(got_str)
        str = addition(got_str)

        str = substraction(got_str)

        txt.delete('1.0','end')
        txt.insert('end',got_str)
    if numbers == 2:

        got_str = division(got_str)

        got_str = multiplication(got_str)

        got_str = addition(got_str)

        got_str = substraction(got_str)


        return got_str



# To make operations easy by using a single function
def any_operator_taker(got_str,operator):
   pass






# +,-,*,/ functions

def division(got_str):
    #any_operator_taker(got_str,'/')
    pass

def multiplication(got_str):
    #any_operator_taker(got_str,'*')
    pass
def addition(got_str):
    #any_operator_taker(got_str,'+')
    pass
def substraction(got_str):
    #any_operator_taker(got_str,'-')
    pass










#different types of checking in equalto
 #to avoid situations like 1+2+,(1. etc
def last_nonnum(got_str):
    T_indexval = len(got_str)-1
    operators = got_str[T_indexval] == '+' or got_str[T_indexval] == '-' or got_str[T_indexval] == '*' or got_str[T_indexval] == '/'

    if got_str[T_indexval] == '(' or got_str[T_indexval] == '.' or operators :
        return 0
    else :
        return 1
