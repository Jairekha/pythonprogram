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