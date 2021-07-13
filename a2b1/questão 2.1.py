v = [1,2,3,4,5]
try: 
   print (v[7])
except IndexError:
   print('Posição não encontrada')