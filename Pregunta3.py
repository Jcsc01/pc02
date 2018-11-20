a=  [[1,2,3,4],
    [4,5,6.8],
    [7,8,9,1],
    [6,3,9,2]]

def sum_diagonal(matriz):
    suma=0
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if i==j:
                suma+=matriz[i][j]

    return suma

print(sum_diagonal(a))