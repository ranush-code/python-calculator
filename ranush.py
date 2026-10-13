def add(a , b):
    return a + b
def subtract(a , b):
    return a - b
def multip(a , b):
    return a * b
def div(a , b):
    return a / b

num1 = float(input("enter first number:"))
num2 = float(input("enter second number:"))

print("choose the operation:")
print("1. add (+)")
print("2. subtract (-)")
print("3. multip (*)")
print("4. div (/)")

choice = input("choose a number of the operation (1/2/3/4) :")
if choice == '1':
    print("the result is :", add(num1, num2))
elif choice == '2':
    print("the result is:", subtract(num1, num2))
elif choice == '3':
    print("the result is:", multip(num1, num2))
elif choice == '4':
    print("the result is:", div(num1, num2))
else:
    print("invalid choice!")
