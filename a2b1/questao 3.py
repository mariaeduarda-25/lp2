def somaNum(a, b):
    if(a+b) > 100 :
        raise OverflowError
    else:
        return a + b
try:
    n1 = int(input('Informe o primeiro número: '))
    n2 = int(input('Informe o segundo número: '))
    print('A soma dos números informados é = ', somaNum(n1, n2))
except ValueError:
    print('Números inválidos! Informe apenas números inteiros')
    n1 = int(input('Informe o primeiro valor: '))
    n2 = int(input('Informe o segundo valor: '))
    print('A soma dos  números informados  é = ', somaNum(n1, n2))