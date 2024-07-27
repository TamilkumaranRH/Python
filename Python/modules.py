'''
import module
print(module.add(5,5))

from module import get
get("hi!")

import math as m
print("this is",m.pi)
'''
'''
from add import *

try:
  print("select number is")
  print("1.Addition \n"
      "2.Subtraction \n"
      "3.Multiply \n"
      "4.division \n")
  select=int(input("enter a number 1/2/3/4:"))
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")


n1=int(input("enter a number:"))
n2=int(input("enter a number:"))

if select == 1:
    print(n1, "+", n2, "=",add(n1, n2))
 
elif select == 2:
    print(n1, "-", n2, "=",subtraction(n1, n2))
 
elif select == 3:
    print(n1, "*", n2, "=",multiply(n1, n2))
 
elif select == 4:
    print(n1, "/", n2, "=", division(n1, n2))
else:
    print("Invalid input")

'''
'''
import calendar
from datetime import date,timedelta
today=date.today()
tomorrow=today+timedelta(days=1)
yesterday=today-timedelta(days=1)
print("today:",calendar.day_name[today.weekday()],today.strftime('%d-%m-%y'))
print("tomorrow:",calendar.day_name[tomorrow.weekday()],tomorrow.strftime('%d-%m-%y'))
print("yesterday:",calendar.day_name[yesterday.weekday()],yesterday.strftime('%d-%m-%y'))
'''

from python import ifstatement
print(ifstatement.num)
