acum = 0
matriz = [[1,1,1],[2,2,3],[4,3,4]]
for x in range(0,3):
    suma = sum(matriz[x])
    acum = acum + suma
    for y in range(0,3):
        print((matriz[x][y]), end='')
    print(" =  ",suma)
    print("")
    
print("La suma de los elementos es : ",acum)
    