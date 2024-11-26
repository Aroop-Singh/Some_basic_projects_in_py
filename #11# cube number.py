#11 cube number
import math

# first number
x = input("Enter first number : ")
y = x.isdigit()

while y == False:
    x = input("Enter a integer for first number : ")
    y = x.isdigit()
x = int(x)

# second number
z = input("Enter second number : ")
y = z.isdigit()

while y == False:
    z = input("Enter a integer for number : ")
    y = z.isdigit()
z = int(z)

print(f"the number first you entered is {x}")
print(f"the number second you entered is {z}")

if x>z:
    for z in range (z,x+1):
        z= pow(z,3)
        print (z)
elif x<z:
    for x in range (x,z+1):
        x= pow(x,3)
        print (x)
else:
    x = pow(x,3)
    print (x)
