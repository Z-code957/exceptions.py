"""1.Value Error
Outline:
Write a program to understand how the value error exception works?"""
"""try:
    number=int(input("Enter a number: "))
    print(number)

except ValueError as name:
    print("The exception error is",name)"""

'''2.Multiple exceptions
Outline:
Write a program to check how the exceptions and finally statement works'''
"""try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter number 2: "))
    result=num1/num2
   # result2=num2/num1
   # print("Result is ",result2)
    print("Output is ",result)
except ZeroDivisionError:
    print("Division by 0 is not allowed.")
#except:
   # print("Some error occured.")
finally:
    print("i will execute no matter what happens.")"""

'''3.Bye Bye
Outline:
Write a program using nested while loop. If the value is divided by two, then it will run an infinite loop of the bye.'''
'''while True:
    try:
        num = int(input("Enter a number "))
        while num%2==0:
            print("bye")
    except:
        print("INVALID.")'''

#raise
try:
    age = int(input("Enter your age: "))
    if age<18:
        raise ValueError
    else:
        print("Age is VALID.")
except ValueError:
    print("Age is INVALID.")