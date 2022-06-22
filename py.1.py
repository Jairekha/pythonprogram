# Display “Hello World” in your output screen.
print("Hello World")
# Get the input from the user and perform addition of two numbers
a=int(input("Enter the number 1 = "))
b=int(input("Enter the number 2 = "))
c=a+b
print(c)
# swap two variables without temp variable
a=50
b=30
a=a+b
b=a-b
a=a-b
print(a)
print(b)
# convert the entered kilometres (Conversion Factor= 0.621371)
k=int(input("Enter the number"))
m=k*0.621371
print("Conversation is ")
print(m)
# check whether the given number is positive, negative or 0
a=int(input("Enter the nuumber = "))
if(a==0):
 print("The number is zero")
elif(a>0):
 print("The number is positive")
else:
 print("The number is negative")
print(a)    
# verify that the given year is a leap year
b=int(input("ENer the year"))
if(b%4==0):
 print("This is a Leap Year")
else:
 print("This is not a Leap Year")  
print(b)
# display the prime numbers within the given interval
l =int(input("Enter the starting number = "))
u =int(input("Enter the ending number = "))
print("Prime numbers between", l, "and", u, "are:")
for n in range(l,u+1):
   if n > 1:
       for i in range(2, n):
           if (n % i) == 0:
               break
       else:
           print(n)
# display the Fibonacci sequence up to n-th term
nterms = int(input("How many terms? "))
n1=1
n2=0
count=0
if nterms<=0:
   print("Please enter a positive integer")
elif nterms==1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1           
 # check if the number is an Armstrong number or not
 num=int(input("Enter a number: "))
sum=0
temp=num
while temp>0:
   digit=temp%10
   sum+=digit**3
   temp//=10
if num==sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number") 
# Find the Sum of natural numbers up to n-th term
num =int(input("Enter a number = "))
if num < 0:
   print("Please enter a positive number")
else:
   sum = 0
   while(num > 0):
       sum += num
       num -= 1
   print("The sum is", sum)         