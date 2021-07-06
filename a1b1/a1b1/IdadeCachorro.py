idade = int(input('Informe a idade do cachorro: '))
if idade <= 2:
   humano = idade * 10.5
else: 
    humano = (idade-2) * 4 + 21
print('A idade correspondente aos humanos é: ', humano)