try:
    x= int(input('Entre com o primeiro número: '))
    y= int(input('Entre com segundo número: '))
    print( x,'/', y, '=', x/y)
except ValueError:
    print('Erro! Informe números inteiros')
    x= int(input('Entre com o primeiro número: '))
    y= int(input('Entre com o segundo número: '))
    print( x,'/', y, '=', x/y)
except ZeroDivisionError:
    print('Não foipossível realizar divisão por 0!!! Informe outro número ')
    x= int(input('Entre com o primeiro número: '))
    y= int(input('Entre com o segundo número: '))
    print( x,'/', y, '=', x/y)