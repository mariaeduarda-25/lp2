numero=int(input('Informe o n-ésimo termo da sequência: '))
f1=0
f2=1
i=0
while i < numero:
  x= f1+ f2
  f1= f2
  f2=x
  i= i+1
print('O n-ésimo do numero informado é: ', f1)
