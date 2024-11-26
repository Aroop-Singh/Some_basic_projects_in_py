#20 banking pro

import re

def is_number(string):
    pattern = r'^[+-]?(\d+(\.\d*)?|\.\d+)$'  # chaaaaaaaat gpt
    return bool(re.match(pattern, string))

def show_balance():
        print('\n')
        print(f"YOUR BALANCE IS : {x}")

def deposit():
    m=False
    while m == False:
        y = input("Enter amount to deposit : ")
        m = is_number(y)
    y = float(y)

    if y<0:
         print('\n')
         print("Amount cannot be less than 0")
         return 0
    else:
         print('\n')
         print(f"you have deposited {y}")
         return y         

def withdraw():
    m=False
    while m == False:
        z = input("Enter amount to withdraw : ")
        m = is_number(z)
    z = float(z)

    if z<0:
         print('\n')
         print("Amount cannot be less than 0")
         return 0
    elif x<z:
         print('\n')
         print(f"Amount cannot be more than {x}")
         return 0
    else:
         print('\n')
         print(f"you have withdrawn {z}")
         return z

x=0
is_running = True

while is_running:
    print("Banking Program \n1. Show balance \n2. Deposit \n3. Withdraw \n4. Exit")
    a = input("Enter a your choice : ")

    if a=="1":
        show_balance()
        print('\n')
    elif a=="2":
        x = x+deposit()
        print('\n')
    elif a=="3":
        x = x-withdraw()
        print('\n')
    elif a=="4":
        break
