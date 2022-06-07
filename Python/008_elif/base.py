x = input("Please enter a number: ")
y = input("Please enter an operation: ")
z = input("Please enter another number: ")
if y == "+":
    print((int(x)+int(z)))
elif y == "-":
    a = (int(x)-int(z))
    print(a)
elif y == "*":
    b = (int(x)*int(z))
    print(b)
elif y == "/":
    c = (int(x)/int(z))
    print(c)
else:
    print("Nothing works")