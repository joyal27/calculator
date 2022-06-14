#programs to control the possiblities of  buttons


#for all operator buttons
def put_operator(str,oper,txt):
    x = len(str)-1                                   #str is current string 
    if str[x].isnumeric() == True or str[x] == ')' : #oper is operator
        return txt.insert('end',oper)               #txt is to make a link with text widget so to insert in it


#for all numbers
def put_num(str,num,txt):
     flag = 1
     x = len(str)-1    #num is the corresponding number
     if len(str) == 0:  #if there is no value in the text widget we need to add without a condition
          txt.insert('end',num)
          flag = 0
     if flag == 1:
       conditions=str[x] =='+' or str[x] =='-' or str[x] =='*' or str[x] =='/'
       if str[x] == '(' or str[x] == '.' or str[x].isnumeric() == True or conditions:
          return txt.insert('end',num)           

