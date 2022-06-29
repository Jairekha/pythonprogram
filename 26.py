# Python program to print even length words in a string
n="welcome to python program"
s=n.split(" ")
for i in s:
  if len(i)%2==0:
    print(i)