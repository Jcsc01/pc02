numeros=[]
for i in range(5):
    numeros.append(int(input("Ingrese un numero: ")))
print(numeros)


def menor_en_arreglo(list):
    menor=list[0]
    for i in list:
        if i<menor:
            menor=i
    return menor

print(menor_en_arreglo(numeros))
