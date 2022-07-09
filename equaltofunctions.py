from tkinter import messagebox

def brackets(got_str,flag,txt):
    open_brac = list()
    close_brac = list()
    open_close_same = 0
    no_open = 0
    for_operators = 0
    counter = 0
    there_is_brac = 'yes'
    left_part = 0
    right_part = 0

    #to check if is there any opening brackets and closing brackets
    for i in range(0,len(got_str)):
        if got_str[i] == '(':
            open_brac.append(i)
            no_open = 1
        if got_str[i] == ')':
            close_brac.append(i)

    if len(open_brac) != 0 and  len(open_brac) == len(close_brac) and flag == 1:  #to check there is same number of close brackets for open brackets
        while open_brac[len(open_brac)-1] > close_brac[counter] :                 #for including ((1+2)*3) and (1+2)+(3+4) kind of situations
            counter +=1                                                           #counter is used to take close bracket in close_brac list ,which is of higher index value
                                                                                  #than the index value of open bracket taken from the open_brac list

        for_oper = got_str[open_brac[len(open_brac)-1]+1:close_brac[counter]]     #now all set ,now taking things inside bracket

        #to take left and right part outside brackets if any exist
        #to take left
        if open_brac[len(open_brac)-1] == 0:
            left_part = 0
        else:
            left_part = got_str[:open_brac[len(open_brac)-1]]

        #to take right
        if close_brac[counter] == len(got_str)-1:
            right_part = 0
        else:
            right_part = got_str[close_brac[counter]+1:]

        #now giving the for_oper to the function operations
        from_oper = operations(for_oper,1,txt)

        #when there is no operators present and if there is left or right part then we must make new string
        if left_part == 0 and right_part == 0:
            got_str = from_oper
            there_is_brac = 'no'         #so that there is no bracket and only numbers or maybe operators exists
        if left_part != 0 and right_part == 0 :
            got_str = left_part + from_oper
        if left_part == 0 and right_part != 0 :
            got_str = from_oper + right_part
        if left_part !=0 and right_part != 0 :
            got_str = left_part + from_oper + right_part

        #to return the value when last single bracket is taken but there is a left or right part without bracket
        #in that case there_is_brac will not be 'no',if it is not 'no' then returning process will not work
        if len(open_brac) == 1:
            there_is_brac = 'no'  #we need to change there_is_brac = 'no' if only one bracket exist
        if there_is_brac == 'no'  :
            return got_str
        if there_is_brac == 'yes':  #if there is brackets present we need to use the brackets functions again
            got_str = brackets(got_str,1,txt)
            return got_str

    if no_open == 0 and flag == 1: #when no bracket is present we need to send this to operations function
        return got_str

def operations(got_str,flag,txt):
    oper_block = 0
    negative_list = list()

    if flag == 1:
        got_str = div(got_str,txt)
        got_str = multi(got_str,txt)
        got_str = add(got_str,txt)
        got_str = sub(got_str,txt)

        for i in range(0,len(got_str)): #to check any operators present
            operator = got_str[i] == '+' or got_str[i] == '*' or got_str[i] == '/'
            if operator :
                oper_block = 1
                break
            if got_str[i] == '-':
                negative_list.append(i)

        if len(negative_list) >= 1  :   #when there are more than one negative sign in got_str
           oper_block = 1
        if len(negative_list) == 1 and negative_list[0] == 0:
           oper_block = 0              #if negative sign comes on the start and only one such sign is present


         #still there is operator so we need to do the operations
        if oper_block == 0:
             return got_str
        else :
             got_str = operations(got_str,1,txt)
             return got_str

#defining operation functions
def div(got_str,txt):
    got_str = any_oper_taker(got_str,'/',txt)
    return got_str
def multi(got_str,txt):
    got_str = any_oper_taker(got_str,'*',txt)
    return got_str
def add(got_str,txt):
    got_str = any_oper_taker(got_str,'+',txt)
    return got_str
def sub(got_str,txt):
    got_str =any_oper_taker(got_str,'-',txt)
    return got_str

#function which takes any operators
def any_oper_taker(got_str,oper,txt):
    base_operator = 0
    left_operator_found = 0
    right_operator_found = 0
    left_operator_pos = 0
    right_operator_pos = 0
    value = 0
    oper_seeker = 0
    left_part = 0
    right_part = 0
    left_number = 0
    right_number = 0
    new_str = 0

    for i in range(0,len(got_str)):     #to find the first operators from left to right
        if got_str[i] == oper and i != 0 :      #when i = 0 then we will get base_operator as 0,which maybe -ve which is not desired
            base_operator = i
            break

    #taking left number
    #first we need to check any operator in left side from base_operator in reverse order
    for i in range(base_operator-1,-1,-1):
        if got_str[i] == '+' or got_str[i] == '*' or got_str[i] == '-' or got_str[i] == '/'  :
            oper_seeker = 1
            break

    if  oper_seeker == 1 and base_operator != 0:
        left_operator_found = 1                             #if oper_seeker is 1 then there is operator
        left_operator_pos = i                               #if base_operator is 0 then that oper is not present

    if left_operator_found == 1 and base_operator != 0:
        left_part = got_str[:left_operator_pos+1]               #when there is not '-' in left_operator_pos in got_str
        left_number = got_str[left_operator_pos+1:base_operator]

    if left_operator_found == 1 and base_operator != 0 and got_str[left_operator_pos] == '-':  #here inorder to take -ve value from left (i.e '-4-3' from it to take -4)
        left_part  = got_str[:left_operator_pos]
        left_number = got_str[left_operator_pos:base_operator]    #to take -ve values

    if left_operator_found == 0 and base_operator != 0:
        left_number = got_str[:base_operator]

    oper_seeker = 0
    #taking right number
    for i in range(base_operator+1,len(got_str)): #to the right from base_operator to last
        if got_str[i] == '+' or got_str[i] == '*' or got_str[i] == '-'  or got_str[i] == '/'  :
            if i > base_operator+1:  #otherwise i.e '-4*-8' it will take right-operator as '-' in 8 ,in that case we won't get -8 as right_number
                oper_seeker = 1
                break

    if oper_seeker == 1 and base_operator != 0:
        right_operator_found = 1
        right_operator_pos = i

    if right_operator_found == 1 and base_operator != 0:
        right_part = got_str[right_operator_pos:]               #when got_str[base_operator] is not '-'
        right_number = got_str[base_operator+1:right_operator_pos]

    if right_operator_found == 1 and base_operator != 0 and got_str[base_operator] == '-':  #here base_operator will have to be taken to right number
        right_number = got_str[base_operator:right_operator_pos]                            # if it is a -ve value

    if right_operator_found == 0 and base_operator != 0:
        right_number = got_str[base_operator+1:]

    if right_operator_found == 0 and base_operator != 0 and got_str[base_operator] == '-' :
        right_number = got_str[base_operator:]


#now for arithmetic operation
    if  oper == '+' and base_operator != 0:
        value = float(left_number)+float(right_number)
    if oper == '-' and base_operator != 0:
        value = float(left_number)+float(right_number) #Since 4-3 can be done as 4+-3
    if oper == '*' and base_operator != 0:
        value = float(left_number)*float(right_number)
    if oper == '/' and right_number == '0.0' and base_operator != 0:
        txt.delete('1.0','end')
        messagebox.showerror('showerror','cannot be divided by zero')
    if oper == '/' and right_number != '0.0' and base_operator != 0:
        value = float(left_number)/float(right_number)

#now to join the left and right part to create new string 'new_str'
    if right_operator_found == 0 and left_operator_found == 0 and base_operator != 0:
        new_str = str(value)

    if right_operator_found == 1 and left_operator_found == 0 and base_operator != 0:
        new_str = str(value) + right_part

    if right_operator_found == 0 and left_operator_found == 1 and base_operator != 0:
        new_str = left_part + str(value)

    if right_operator_found == 1 and left_operator_found == 1 and base_operator != 0:
        new_str = left_part + str(value) + right_part

#Now to return the new_str or got_str corresponding to the situation
    if base_operator !=0:
        return new_str

    if base_operator == 0: # since base_operator is zero then new_str will be zero to avoid that
        return got_str

#To avoid situations like 1+2+,(1. etc
def last_nonnum(got_str):
    T_indexval = len(got_str)-1
    operators = got_str[T_indexval] == '+' or got_str[T_indexval] == '-' or got_str[T_indexval] == '*' or got_str[T_indexval] == '/'

    if got_str[T_indexval] == '(' or got_str[T_indexval] == '.' or operators :
        pass
    else :
        return 1
