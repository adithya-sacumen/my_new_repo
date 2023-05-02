# taking int input from user
num=int(input("Enter any number:"))

# assigning initial values to a and b
a=0
b=1

# looping num to print fibonaci series
for var in range(num):
    print(a,end=" ")
    a,b=b,a+b
