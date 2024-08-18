a=int(input("Enter first number: "))
o=input("Enter operation: ")
b=int(input("Enter second number: "))

print("Answer = ",end=' ')
if o=='+':
    print(a+b)
elif o=='-':
    print(a-b)
elif o=='*':
    print(a*b)
elif o=='/':
    print(a/b)
else:
    print("Operation is not valid.")
