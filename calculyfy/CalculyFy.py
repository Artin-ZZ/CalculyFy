from colorama import Fore, Style
    
def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0:
        return 1
    else:
        result = 1
    for i in range(1, n + 1):
        result *= i
    print(Fore.GREEN + Style.BRIGHT + f"Factroial of {n} is: {str(result)}")

def add(a,b):
    res = a + b
    print(Fore.GREEN + Style.BRIGHT + f"Result Of {a} plus {b} is : {str(res)}")

def subtract(a,b):
    res = a - b
    print(Fore.GREEN + Style.BRIGHT + f"Result Of {a} Minus {b} is : {str(res)}")

def multip(a,b):
    res = a * b
    print(Fore.GREEN + Style.BRIGHT + f"Result Of {a} Times {b} is : {str(res)}")

def devide(a,b):
    res = a / b
    print(Fore.GREEN + Style.BRIGHT + f"Result Of {a} Divided By {b} is : {str(res)}")

def md(a,b):
    res = a % b
    print(Fore.GREEN + Style.BRIGHT + f"The result of {a} modulo {b}: {str(res)}")

def power(a,b):
    res = a ** b
    print(Fore.GREEN + Style.BRIGHT + f"Result Of {a} To The Power Of {b} is : {str(res)}")
    
def power_of_two(a):
    res = a ** 2
    print(Fore.GREEN + Style.BRIGHT + f"Result Of {a} To The power Of 2 is: {str(res)}")
    
    
def square_root(num):
    if num < 0:
        raise ValueError("Square root is not defined for negative numbers.")
    else:
        res = num ** 0.5
        print(Fore.GREEN + Style.BRIGHT + f"The Result square root of {num} is : {str(res)}")