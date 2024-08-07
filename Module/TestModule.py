a = int(input("Enter The First Number:"))
b = int(input("Enter The Second Number:"))


def math_operations(x=a, y=b):
    sum = x + y
    print("Addition of two given number is:", sum)
    mult = x * y
    print("Multiplication of two given number is:", mult)
    divi = x / y
    print("Division of two given number is:", divi)
    Subs = x - y
    print("Substaction of two given number is:", Subs)

    return sum, mult, divi, Subs

#math_operations()
