n = int(input("Enter number: "))

if n % 3 == 0:
    print("Number is divisible by 3")

if n % 5 == 0:
    print("Number is divisible by 5")

if n % 9 == 0:
    print("Number is divisible by 9")

if n % 3 != 0 and n % 5 != 0 and n % 9 != 0:
    print("Number is not divisible by 3, 5, or 9")