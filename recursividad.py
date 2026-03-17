def sumatoria (n):
    if n==1:
        return 1
    return n+sumatoria(n-1)

print("La sumatoria", sumatoria(5))

def factorial (n):
    if n==0:
        return 1
    return n * factorial(n-1);

print("El factorial" , factorial(5)) 

def fibonacci(n):
    if n<=1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print("Serie fibonacci", fibonacci(5))

for i in range(7):
    print(fibonacci(i))