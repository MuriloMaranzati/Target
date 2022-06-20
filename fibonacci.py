# Resolução pergunta 2:

num = int(input('Insira um número: '))

def fib(n):
    if n > 1:
        return fib(n-1) + fib(n-2)
    return n

for i in range(num):
    print(fib(i))