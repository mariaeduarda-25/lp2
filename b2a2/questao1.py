file = open("notassurfistas.csv", "r")
file.seek(0,0)
d = []
auxiliar = file.readlines()
file.seek(0,0)
contador = len(file.read().split())
file.seek(0,0)
str_file = file.read()
file.seek(0,0)
t = []
vetor = []
j = 0
auxiliar_medias = []
somatorio= []
for i in range(0, contador, 6):
    vetor.append(file.read().split()[i])
    file.seek(0,0)
    m = "".join(vetor[j])
    str_file = str_file.replace(m, "")
    file.seek(0,0)
    j = j+1
for i in range(0, j):
    auxiliar_mxmn = auxiliar[i].replace(vetor[i], "").replace(",","").split()
    máximo = max(auxiliar_mxmn)
    mínimo = min(auxiliar_mxmn)
    d.append(auxiliar[i].replace(máximo, "").replace(mínimo, ""))
vetor_auxiliar = vetor
vetor = sorted(set(vetor))
for i in range(0, len(vetor)):
    for j in range(0, len(d)):
        if vetor[i] in d[j]:
            t.append(d[j])
auxiliar_medias = "".join(t)
for i in range(0, len(vetor)):
    auxiliar_medias = auxiliar_medias.replace(vetor[i],"")
split_auxiliar = auxiliar_medias.replace(",","").split()
for i in range(0, len(split_auxiliar), 3):
    somador = 0
    for j in range(i, i+3):
        somador = float(split_auxiliar[j]) + somador
    somatorio.append(round(somador/3, 2))
vet_aux = sorted(vetor_auxiliar)
teste = []
var_media = []
assistente = []
for i in range(0, len(vetor_auxiliar)):
    testando = vetor_auxiliar[i], somatorio[i]
    teste.append(testando)
teste = list(teste)
for i in range(0, len(vetor)):
    for j in range(0, len(teste)):
        if vetor[i] in teste[j]:
            var_media.append(teste[j][1])
        if j == len(teste)-1:
            var_media.append("\n")
for i in range(0, len(var_media)):
    lista = [str(i) for i in var_media]
var_media = " ".join(lista).split("\n")
f= 0
n = 0
teste.clear()
for i in range(0, len(var_media)-1):
    var_media[i] = sorted(var_media[i].split())[len(var_media[i].split())-2:len(var_media[i].split())]
    f = 0
    for j in range(0,2):
        f = float(var_media[i][j]) + f
    if i != len(var_media)-1:
        print("".join(vetor[n]).replace(",", " -"), round(f, 2))
    n = n+1