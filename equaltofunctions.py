from tkinter import messagebox
#different operation functions


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
    print('flag',flag)
    #to check if is there any opening brackets and closing brackets
    for i in range(0,len(got_str)):
        if got_str[i] == '(':
            open_brac.append(i)
            no_open = 1

        if got_str[i] == ')':
            close_brac.append(i)
    print('open_bracket_list',len(open_brac))
    print('close_bracket_list',close_brac)


    if len(open_brac) != 0 and  len(open_brac) == len(close_brac) and flag == 1:  #to check there is same number of close brackets for open brackets
        while open_brac[len(open_brac)-1] > close_brac[counter] :#for including ((1+2)*3) and (1+2)+(3+4) kind of situations
            counter +=1
        #now all set to the brackets main functions
        for_oper = got_str[open_brac[len(open_brac)-1]+1:close_brac[counter]]
        print(for_oper)
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
        print('from_oper',from_oper)

        print('no-open',no_open)




        #when there is no operators present and if there is left or right part then we must make new string
        if left_part == 0 and right_part == 0:
            got_str = from_oper
            there_is_brac = 'no'         #so that there is no bracket and only numbers or maybe operators
        if left_part != 0 and right_part == 0 :
            got_str = left_part + from_oper
            print('here')
        if left_part == 0 and right_part != 0 :
            got_str = from_oper + right_part
        if left_part !=0 and right_part != 0 :
            got_str = left_part + from_oper + right_part


        #to return the value when last single bracket is taken but there is a left or right part without bracket
        #in that case there_is_brac will not be 'no',if it is not 'no' then returning process will not work
        #we need to change there_is_brac = 'no' if only one bracket exist
        if len(open_brac) == 1:
            there_is_brac = 'no'



        #print('now',s)
        #if there is brackets present we need to use the brackets functions again
        if there_is_brac == 'no'  :
            print('returning')
            return got_str
        if there_is_brac == 'yes':
            got_str = brackets(got_str,1)
            return got_str


    if no_open == 0 and flag == 1: #when no bracket is present we need to send this to next function
        return got_str




#to calculate inside brackets





def operations(got_str,flag,txt):
    oper_block = 0
    negative_list = list()

    if flag == 1:
        got_str = div(got_str,txt)
        print('passed div')
        got_str = multi(got_str,txt)
        print('passed multi')
        got_str = add(got_str,txt)
        print('passed add')
        got_str = sub(got_str,txt)



        for i in got_str:
            operator = i == '+' or i == '*' or i == '/'
            if operator :
                oper_block = 1
                break
            if i == '-':
                negative_list.append(i)

       #
        if len(negative_list) == 1 and negative_list[0] == 0:
           oper_block = 0


         #still there is operator so we need to do the operations
        if oper_block == 0:
             print('working1')
             return got_str
        else :
             got_str = operations(got_str,1)
             return got_str









#fjfls
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



#sjf
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
        if got_str[i] == oper and i != 0 :      #when i = 0 then we will get base_operator as 0 when -ve value comes
            base_operator = i
            break

    print('base',base_operator)

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

    if left_operator_found == 1 and base_operator != 0 and got_str[left_operator_pos] == '-':  #here inorder to take -ve value from left i.e '-4-3' from it to take -4
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

#here base_operator will have to be taken to right number if it is a -ve value
    if right_operator_found == 1 and base_operator != 0:
        right_part = got_str[right_operator_pos:]               #when got_str[base_operator] is not '-'
        right_number = got_str[base_operator+1:right_operator_pos]

    if right_operator_found == 1 and base_operator != 0 and got_str[base_operator] == '-':

        right_number = got_str[base_operator:right_operator_pos]

    if right_operator_found == 0 and base_operator != 0:
        right_number = got_str[base_operator+1:]

    if right_operator_found == 0 and base_operator != 0 and got_str[base_operator] == '-' :
        right_number = got_str[base_operator:]

    print('left_number',left_number)
    print('right_number',right_number)
    print('leftpart',left_part)
    print('rightpart',right_part)
#now for arithmetic operation
    if  oper == '+' and base_operator != 0:
        value = float(left_number)+float(right_number)
    if oper == '-' and base_operator != 0:
        value = float(left_number)+float(right_number)
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
        print('leftside work')

    if right_operator_found == 1 and left_operator_found == 1 and base_operator != 0:
        new_str = left_part + str(value) + right_part

   #changing new_str to string
    new_str = str(new_str)
   # when we do -4-2 we get --6.0 ,likewise there are some cases to avoid it we need to do some changes on new_str
    if new_str[0] == '-' and new_str[1] == '-':
        new_str = new_str[1:]


    print('current str',new_str)


    if base_operator !=0:
        return new_str

    if base_operator == 0: # since base_operator is zero then new_str will be zero to avoid that
        return got_str








#different types of checking in equalto
 #to avoid situations like 1+2+,(1. etc
def last_nonnum(got_str):
    T_indexval = len(got_str)-1
    operators = got_str[T_indexval] == '+' or got_str[T_indexval] == '-' or got_str[T_indexval] == '*' or got_str[T_indexval] == '/'

    if got_str[T_indexval] == '(' or got_str[T_indexval] == '.' or operators :

        pass
    else :
        return 1
