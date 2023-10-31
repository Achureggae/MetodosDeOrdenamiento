

lista = [10,5,8,4,9,3,1,2,3,4,8,9,1,5]
n=0
print(lista)

for _ in lista:
    n += 1
    
for x in range(n):
    actual = x
    for y in range(x+1,n):
        if lista[actual] > lista[y]:
            actual = y
    lista[x],lista[actual] = lista[actual],lista[x]

print(lista)
    
            