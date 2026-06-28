# # # C) Conditionals:-

# Take age input and print if eligible to vote (>=18).

age=int(input("enter your age :-"))
if age>=18:
    print("congratulation! you are eligible to vote")
else:

    print("sorry! you are not eligible to vote")

# Take number and print if positive, negative, or zero.
numb1=int(input("enter any number"))
if(numb1>0):
    print("Number is positive.")
elif(numb1==0):
    print("Number is zero.")

else:
    print("Number is negative.")




# Take two numbers and print the larger one.

numb1=int(input("Enter first Number:-  "))
numb2=int(input("Enter second Number:-  "))
if(numb1>numb2):
    print("First Number is greater..  ")
elif(numb1<numb2):
    print("second Number is greater..  ")
else:
    print("both are equal..")


#Take three numbers and print the largest.

numb1=int(input("Enter first Number:-  "))
numb2=int(input("Enter second Number:-  "))
numb3=int(input("Enter third Number:-  "))
if(numb1>=numb2 and numb1>=numb3):
    print("First Number is greater..  ")
elif(numb2>=numb3 and numb2>=numb1):
    print("Second Number is greater.. ")
else:
    print("Third Number is greater.. ")

# Take two numbers and print if first is divisible by second. 

numb1=int(input("Enter first Number:-  "))
numb2=int(input("Enter second Number:-  "))
if (numb2==0):
    print("no  it is  not divisible by second number")
elif (numb1%numb2==0):
    print(" it is   divisible by second number")
else:
    print("not divisible")

#Check if a number is a leap year.

year=int(input("Enter year:-  "))

if (year%400==0):
    print("yes it is leap year")
elif (%100==0):
    print("yes it is  not leap year")
elif (numb1%4==0):
    print("yes it is leap year")   
else:
    print("not leap year")

#Check if a number is divisible by 3 and 5.

numb1=int(input("Enter first Number:-  "))

if (numb1%3==0)and numb1%5==0:
    print("yes it is divisible by second number")
else:
    print("not divisible")

# Check if a string length is even/odd.

text=input("enter a string :-")
if len(text)%2==0:
    print("string length is even")
else:
    print("string length is odd")

# Take marks and print grade:
# A: 90-100
# B: 80-89
# C: 70-79
# D: 60-69
# F: <60
student_marks=int(input("enter marks :-"))

if student_marks<0 or student_marks >100:
    print("invalid marks")
elif student_marks >= 90:
    print("A")
elif student_marks >=80:
    print("B")
elif student_marks>=70:
    print("C")
elif student_marks>=60:
    print("D")
else:
    print("f")

# Find largest among two using conditional operator style (ternary).

numb1=int(input("Enter first Number:-  "))
numb2=int(input("Enter second Number:-  "))

print("first number is gretear"if numb1>numb2 else 'second number is grater')

#  Given side lengths a,b,c check if triangle possible (a+b>c etc).

a=int(input("Enter first Number:-  "))
b=int(input("Enter second Number:-  "))
c=int(input("Enter third Number:-  "))
if(a+b>c)and(b+c>a)and(c+a>b):
    print("yes triangle possible")

else:
    print("not possible")


# Check if triangle is equilateral/isosceles/scalene.

a=int(input("Enter first Number:-  "))
b=int(input("Enter second Number:-  "))
c=int(input("Enter third Number:-  "))
if(a+b>c)and(b+c>a)and(c+a>b):
    
   if(a==b==c):
    print("trianle is equilateral")
   elif(a==b)or(b==c)or(c==a):
    print("trianle is isoceles")
   else:
    print("trianle is scalane")
else:
  print("triangle is not possible")

# Input month number (1-12) and print season (basic logic).

month=int(input(("enter month number(1-12) :-")))
if 3 <=month<=6:
    print("summer season")
elif 7<=month<=9:
    print("rainy season")
elif 10<=month<=11:
    print("autumn season")
elif month== 12 or 1<=month<=2:
     print("winter season")

else:
    print("eror")
# Input day number and print weekday name (1=Mon, etc).

num=["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
day=int(input("day number :-"))
if (1<=day<=7):
    print(num[day-1])
else:
    print("error")



# Check if a number is prime (use loop inside). 
num = int(input("Enter the number: "))

if num <= 1:
    print("Not Prime")
else:
    prime = True

    for i in range(2, num):
        if num % i == 0:
            prime = False
            break

    if prime:
        print("Prime Number")
    else:
        print("Not Prime")

# Check if a number is perfect square.

num = int(input("Enter the number: "))
is_perfect_square = False

for i in range(num + 1):
    if i * i == num:
        is_perfect_square = True
        print("perfect sq")
        break

if not is_perfect_square:
    print("not perfect square")

# Check if a number is perfect number (sum of divisors equals number).

num = int(input("Enter the number: "))
sum = 0

for i in range(1, num):
    if num % i == 0:
        sum = sum + i

if sum == num:
    print("Perfect Number")
else:
    print("Not Perfect Number")
    




# Take a string and check if it’s “Yes/No” ignoring case.


text=input("enter the string:-")
if text.lower()=="yes":
    print("yes")
elif text.lower()=="no":

    print("no")

else:
    print("invalid")


#Check if a character is vowel or consonant.

ch=input("enter a charachter :-")
if ch.lower()in("aeiou"):
    print("vowel")
else:
    print("not vowel")
 

# Check if number is between 10 and 20 (inclusive).

num=int(input("enter the number"))
if(10<=num<=20):
    print("number is betwwn them")
else:
    print("number not lies between them")


# Check if number is between -5 and 5.


num=int(input("enter the number"))
if (-5<=num<=5):
    print("number lies between them")
else:
    print("number not lies between them")

# Take marks and print “Pass” or “Fail” (>=35).

mark=int(input("enter the marks :-"))
if mark>=35:
    print("student is pass")
else:
    print("sudent is fail")



#Take temperature and print “Freezing” (<0), “Normal” (0-25), “Hot”(>25).

temp=int(input("ener the tempreture :-"))
if temp<0:
    print("freezing")
elif 0<=temp<=25:
    print("normal")

else:
    print("hot")



# Take three numbers and print if they can form arithmetic progression.

a=int(input("enter the first number:"))
b=int(input("enter the sec number:"))
c=int(input("enter the third number:"))

if a-b== b-c:
    print("arthmetic progrssion")
else:
    print("not arthmetic progrssion")


# Given x, print absolute value using conditional. 

x=int(input ("enter the value of x:-"))
if x<0:
    print(-x)

else:
    print(x)


#Given marks, print pass/fail and also “distinction” if >=75.

mark=int(input("enter the marks :-"))
if mark>=75:
    print("pass")
    print("distniction")
elif mark>=35:
    print("pass")
else:
    print("fail")


# Take year and print if it is century (divisible by 100).

year=int(input("enter the year:-"))
if year%100==0:
    print("century")
else:
    print("not century")

# Take number and print if divisible by both 2 and 4.

num=int(input("enter the first number :-"))
if num%2==0 and num%4==0:
    print("yes it is divisible")
else:
    print("not divisible")

# Take two strings and print if they are equal ignoring case.

a=input("enter the string1")
b=input("enter the string2")


# Take two integers and print if they are both positive.

num1=int(input("enter the first number:-"))
num2=int(input("enter the second number:-"))
if num1>=0 and num2>=0:
    print("both number is possitive")
else:
    print("number is not possitive")

# Take three integers and print if all are equal.

num1=int(input("enter the first number:-"))
num2=int(input("enter the second number:-"))
num3=int(input("enter the third number:-"))

if(num1==num2) and (num2==num3):
    print("three integer are equal")
else:
    print("integer not equal")

#Take string and print if it contains substring "python".

stro=input(" the word :-")
if "python" in stro.lower():
    print("it is substring")
else:
    print("not substring")

#Check if input character is digit using condition.

ch=input("enter the character :-")
if ch.isdigit():
    print("using digit")
else:
    print("not")

# Check if input character is uppercase using .isupper().

ch=input("enter the char :-")
if ch.isupper():
    print("using uppercase")
else:
    print("not using upper case")

# Check if input character is lowercase using .islower().
ch=input("enter the char :-")
if ch.islower():
    print("using lower case")
else:
    print("not using lower case")

# Check if password matches confirm password (two inputs).
password=input("enter the password :-")
confirm=input("enter the confirm password :-")
if password==confirm:
    print("password is matched")
else:
    print("password not matched")


# Take a number and print factorial using conditional base case.
num=int(input("enter the factorial"))
if num==0 or num==1:
    print("factorial is 1")
else:
    for i in range(1,num+1):
        fact*=i
        print("factorial is",fact)

# Implement simple calculator using conditionals (+,-,*,/).


num1=int(input("enter the first number:-"))
num2=int(input("enter the second number:-"))
op=input("+ - * % / ** //") 

if (op=="+"):
    print(num1+num2)
if (op=="-"):
    print(num1-num2)
elif (op=="*"):
    print(num1*num2)
elif (op=="/"):
    print(num1/num2)
elif (op=="//"):
    print(num1//num2)
elif (op=="**"):
    print(num1**num2)
elif (op=="%"):
    print(num1%num2)
else:
    print("not found")

#  Take two numbers and print quotient only if divisor not zero.
num1=int(input("enter the number you will divide :-"))
num2=int(input("enter the number you will give divide :-"))

if num2!=0:
    print("qutient",num1/num2)
else:
    print(" divisor not possible ")
