import logging
logging.basicConfig(filename="Assignmnet4.log",level= logging.DEBUG,format="%(levelname)s %(asctime)s %(name)s %(message)s")

class Assignmnet4:
    logging.info(" This  is Assignmnet4 funtion ")
    """1.Write a Python Program to Find the Factorial of a Number?"""
    def Factorial_of_a_Number(self):
        logging.info(" We are in Factorial_of_a_Number")
        try:
            num = int(input("Enter the number"))
            fact = 1
            logging.info("Enter number is %s ",num )
            for i in range(1,num+1):
                fact = fact * i
                logging.info("factorial of number is %s ",fact)
                print(fact)

        except Exception as  e:
            logging.exception(e)

    """2.	Write a Python Program to Display the multiplication Table?"""
    def multiplication_Table(self):
        logging.info(" Display multiplication Table")
        num =int(input("Enter the table which you want to print"))
        try:
            for i in  range(1,11):
                logging.info("Multiplication Table %s  %s %s %s %s" , num ,"*",i,"=",i*num)
                print(num ,"*",i,"=",i*num)

        except Exception as e:
            logging.exception(e)

    """3.	Write a Python Program to Print the Fibonacci sequence?"""
    def Fibonacci_sequence(self):
        logging.info("Fibonacci_sequence function")
        try:
            num = int(input("Enter the number"))
            logging.info("Enter  number is %s" ,num)
            a = 1
            b = 1
            print(a)
            print(b)
            for i in range(2,num):
                c = a+ b
                a=b
                b=c
                logging.info("Fibonacci_sequence is %s $s",c )
                print(c)
        except Exception as e:
            logging.exception(e)

    """4.	Write a Python Program to Check Armstrong Number?"""
    def Armstrong_Number(self):
        logging.info("Armstrong_Number function")
        try:
            a = input('Enter a number: ')
            sum = 0
            for i in range(len(a)):
                sum = sum + pow(int(a[i]),3)
            if sum == int(a):
                logging.info(f'{a} is a Armstrong Number')
                print(f'{a} is a Armstrong Number')
            else:
                logging.info(f'{a} is a Not Armstrong Number')
                print(f'{a} is a Not Armstrong Number')
        except Exception as e:
            logging.exception(e)

    """5.	Write a Python Program to Find Armstrong Number in an Interval?"""
    def Find_Armstrong_Number_Interval(self):
        logging.info("Find_Armstrong_Number_Interval")
        try:
            num1 = int(input("Enter the  strat number"))
            num2 = int(input("Enter the  end number"))
            for num in range(num1, num2):
                temp = num
                sum = 0
                while temp > 0:
                    digit = temp % 10
                    sum = sum + digit ** 3
                    temp = temp // 10
                    if sum == num:
                        logging.info("Armstrong_Number_Interval %s",num)
                        print("Armstrong_Number_Interval",num)
        except Exception as e:
            logging.exception(e)





    """6.	Write a Python Program to Find the Sum of Natural Numbers?"""
    def Sum_of_Natural_Numbers():
        logging.info("Sum_of_Natural_Numbers")
        num = int(input("Enter the number"))
        logging.info("Enter number is %s ",num)
        p = 0
        while num > 0:
            p = p + num
            num = num - 1
        logging.info("Sum_of_Natural_Numbers %s ",p)
        return p




A= Assignmnet4
#A.Factorial_of_a_Number
#print(A.Factorial_of_a_Number("fact"))
#print(A.multiplication_Table("num"))
#print(A.Fibonacci_sequence(""))
#print(A.Armstrong_Number(""))
print(A.Sum_of_Natural_Numbers())
print((A.Find_Armstrong_Number_Interval("")))
