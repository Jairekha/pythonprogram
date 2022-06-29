#Write a function called show_stars(rows). If rows are 5
n=int(input("\nEnter the number of rows:"))
for i in range(1,n+1):
    for j in range(0,i):
        print("*",end="  ")
    print("\r")
