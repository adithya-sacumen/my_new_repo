# taking int input from user
num=int(input("Enter any number:"))

# # assigning initial values to a and b
a=0
b=1

# # looping num to print fibonaci series
for var in range(num):
    print(a,end=" ")
    a,b=b,a+b



# prime number program 
num1 =int(input("Enter number:"))
count=0
for val in range(2,num1//2+1):
    if num1%2==0:
        count+=1
if count==0:
    print("Prime number")
else:
    print("Not a prime number")