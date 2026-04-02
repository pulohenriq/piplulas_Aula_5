def ehPrimo(n):
    if n < 2:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

#main
n = int(input('Número: '))
if ehPrimo(n):
    print(f'{n} é primo')
else: 
    print(f'{n} não é primo')