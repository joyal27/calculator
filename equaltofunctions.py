from tkinter import messagebox
#different operation functions





#to calculate inside brackets
def bracket(str,txt,flag):
    if flag == 1:
        bracket_found = 0
        open_bracket_list = list()
        close_bracket_list = list()
        open_close_same = 0
        close_pos = 0
        opeartors_found = 0

        #to check whether there is a open bracket present
        for i in range(0,len(str)):
            if str[i] == '(':
                bracket_found = 1
                break

        if bracket_found == 0 or :
                    return str,1          #if there is no bracket then there may be operators
        if bracket_found == 1:
            #to take the position of open brackets
            for i in range(0,len(str)):
                if str[i] == '(':
                    open_bracket_list.append(i)
                    #to take the position of close brackets
            for i in range(0,len(str)):
                if str[i] == ')':
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
            left_part = str[0:open_bracket_list[len(open_bracket_list)-1]]
            right_part = str[close_bracket_list[close_pos+1]:]
            operation_part = str[(open_bracket_list[len(open_bracket_list)-1])+1:close_bracket_list[close_pos]]
            #now to check if any operator is present in the operation_part
            for i in range(0,len(opeartion_part)):
                operators = str[i] == '+' or str[i] == '-' or str[i] == '*' or str[i] == '/'
                if operators:
                    operators_found = 1
        if operators_found == 0:
            str = left_part + operation_part + right_part
            open_bracket_list = []
            close_bracket_list = []
            brackets(str,txt,1) #to loop until only numeric values left
        if operators_found ==1:
            operation_part = operations(operation_part,txt,1)
            str = left_part + opeation_part + right_part
            open_bracket_list = []
            close_bracket_list = []
            brackets(str,txt,1)#to loop until inside part of bracket is only numeric left and without brackets














def operations(str,numbers,txt):
    if numbers == 1:
        division(str):
        multiplication(str):
        addition(str):
        substraction(str):

        txt.delete('1.0','end')
        txt.insert('end',str)


# To make operations easy by using a single function
def any_operator_taker(str,operator):
    operator_list = []
    counter = 0
    left_operator = 0
    right_operator = 0
    for oper in operator_list:
        for i in range(0,len(str)): #to find the specified operator
            if str[i] == operator:
                operator_list.append(i)
        if len(operator_list) >= 1:
        #for looping through the operator_list in each indexes
            for i in range(0,operator_list[counter]:
            #looking in to left side
                operators = str[i] == '+' or str[i] == '-' or str[i] == '*' orstr[i] == '/'
                if operators :
                    left_operator = 1
                    left_operator_pos = i
                    break
            if left_operator == 1:
                left_no = str[left_operator_pos+1:operator_list[counter]] #when a operator is on left side
                left_part = str[:left_operator_pos]                       #and we want a number only
            if left_operator == 0:
                left_no = str[:operator_list[counter]] #when no operator is found
        #looking in to right side
            for i in range(operator_list[counter],len(str)):
                if operators :
                    right_operator = 1
                    right_operator_pos = i
                    break
                if right_operator == 1:
                    right_no = str[operator_list[counter+1]:right_operator_pos]
                    right_part = str[right_operator_pos+1:]
                if right_operator == 0:
                    right_no = str[operator_list[counter+1]:]







        else :
            return str
        counter = counter +1


# +,-,*,/ functions
def division(str):

def multiplication(str):

def addition(str):

def substraction(str):











#different types of checking in equalto
 #to avoid situations like 1+2+,(1. etc
def last_nonnum(str):
    T_indexval = len(str)-1
    operators = str[T_indexval] == '+' or str[T_indexval] == '-' or str[T_indexval] == '*' or str[T_indexval] == '/'

    if str[T_indexval] == '(' or str[T_indexval] == '.' or operators :
        return 0
    else :
        return 1
