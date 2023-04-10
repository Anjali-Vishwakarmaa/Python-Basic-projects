"""
Make a Scientific Calculator
"""

from operator import *
from math import *

while True:
    ch=input("""1.Enter "+" for addition,"
        2.Enter "-" for subtraction,
        3.Enter "*" for multiplication, 
        4.Enter "/" for division,
        5.Enter "fact" for factorial,
        6.Enter "log" for Log,
        7.Enter "sin" for sin,
        8.Enter "cos" for cos
        9.Enter "floor" for floor division
        10.Enter "pow" for power
        11.Enter "tan" for tan
        12.Enter "cosec" for cosec
        13.Enter "sec" for sec
        14.Enter "cot" for cot
        15.Enter "degree" for degree
        16.Enter "radian" for radian
        17.Enter "sqrt" for square root
        18.Enter "ceil" for ceil
        19.Enter "min" for min value
        20.Enter "max" for max value
        
        Enter your choice: """)
    a=int(input("Enter First Number: "))
    if ch=="sin":
        res=sin(a)
        print("Result: ",res)

    elif ch=="cos":
        res=cos(a)
        print("Result: ",res)

    elif ch=="tan":
        res=tan(a)
        print("Result: ",res)

    elif ch=="fact":
        res=factorial(a)
        print("Result: ",res)

    elif ch=="cosec":
        res=1/sin(a)
        print("Result: ",res)

    elif ch=="sec":
        res=1/cos(a)
        print("Result: ",res)

    elif ch=="cot":
        res=1/tan(a)
        print("Result: ",res)

    elif ch=="degree":
        res=degrees(a)
        print("Result: ",res)

    elif ch=="radian":
        res=radians(a)
        print("Result: ",res)

    elif ch=="sqrt":
        res=sqrt(a)
        print("Result: ",res)

    else:

        b=int(input("Enter Second Number:"))

        if(ch=="+"):
            res=add(a,b)
            print("Result is:",res)


        elif(ch=="-"):
            res=sub(a,b)
            print("Result is:",res)

        elif(ch=="*"):
            res=prod(a,b)
            print("Result is:",res)

        elif(ch=="/"):
            res=a/b
            print("Result is:",res)


        elif(ch=="log"):
            res=log(a,b)
            print("Result: ",res)

        elif(ch=="min"):
            res=min(a,b)
            print("Result: ",res)

        elif(ch=="mod"):
            res=a%b
            print("Result: ",res)

        elif(ch=="floor"):
            res=floordiv(a,b)
            print("Result: ",res)

        elif(ch=="ceil"):
            res=ceil(a/b)
            print("Result :",res)

        elif(ch=="pow"):
            res=a**b
            print("Result: ",res)

        elif(ch=="max"):
            res=max(a,b)
            print("Result: ",res)

        else:
            print("Incorrect choice")

    chYN=input("Do you want to continue,Y/N: ")
    if chYN=='n' or chYN=='N':
        print("Thanks for using Calculator")
        break

