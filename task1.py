def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n-1)

num=int(input("Enter a number to find the Factorial: "))
print("Factorial of",num, "is:",factorial(num))