
#elif condition syntax

''' 
if (test expression):
    statement
elif (test expression):
    statement
.......
else:
    statement
statement'''

operand_1= int(input('Enter operand1: '))
operand_2= int(input('Enter operant: '))
Operator= input('Choose an operator: (+,-,*,/)')

if Operator == '+':
    print(operand_1+operand_2)
elif Operator == '-':
    print(operand_1-operand_2)
elif Operator == '*':
    print(operand_1*operand_2)
elif Operator == '/':
    print(operand_1/operand_2)
else:
    print('none')
print('Thank you !')