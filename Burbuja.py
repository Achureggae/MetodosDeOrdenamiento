

lista = [10,5,8,4,9,3,1,2,3,4,8,9,1,5]
n=0
print(lista)

for _ in lista:
    n+=1
    
for x in range(n-1):
    for y in range(n-x-1):
        if lista[y] > lista[y+1] :
            lista[y] , lista[y+1] = lista[y+1],lista[y]
            
print(lista)            



