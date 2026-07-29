try:
    a = int(input("Enter a number: "))
    print(a+6)
except Exception as e:
    print(e)
    print("Invalid input")