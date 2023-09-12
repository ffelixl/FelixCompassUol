
def quebra(sequencia):
    tupla = sequencia.split(',') #Quebrando a string atraves do metodo split#
    soma = 0
    for i in tupla:
        soma += int(i)
    return soma
    
string = "1,3,4,6,10,76"
soma = quebra(string)
print(soma)

