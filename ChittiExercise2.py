# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 21:42:39 2020

@author: AG14546
"""
import math
def percent(expression):
    if "%" in expression:
        expression = expression.replace("%","/100")
    return eval(expression)

a= int (input('Total No of Months')) #no of Months to Pay
ChittiAmount = int(input('ChittiAmount'))
if a ==0:
    raise Exception ("No of months Cannot be less than 1")   
b= int (input('total No of Persons'))  #no of Persons
#x = int (input()) #the no of months after which the amount lifted
mp = percent("5*ChittiAmount%") #mp stands for montly pay if amount not lifted
mp2 = percent("6*ChittiAmount%") #mp2 stands for montly pay if amount  lifted
list = input("Enter Months separated by space for the People who have lifted the amount ")
y  = list.split()
 #print(y)
pay = 0
received = 0
count = 0
for z in y:
    x = int(z)
    if x <= 0 or x > 20:
        raise Exception ("No of months Specified is out of Range")
    else:
        received+= ((a-x) * mp2) + (x * mp)  #Total amount received after 2months 
        pay+=  94000 + (x * (1000))
        count+= 1
if count == b:
    print ('All Customers have lifted the amount before 20months')
elif count > b:
    raise Exception ("No of Customers Specified is out of Range")
else:
    x = int(input('Give Month Value for Rest Of Customers '))
    if x <= 0 or x > 20:
        raise Exception ("No of months Specified is out of Range")
    while count  != b:
        received+= ((a-x) * mp2) + (x * mp)  #Total amount received after 2months 
        pay+=  94000 + (x * (1000))
        count+= 1
        
print ('You have Paid  customers:',pay)
print ('The amount you recievd:',received)
    #ref = x * 5000 #amount the person has paid till he lifted the amount
    
if pay < received :
    print ('You have received Profit of:',(received-pay))
else:
    print ('You have Encountered Loss of:',(pay-received))


    

    



