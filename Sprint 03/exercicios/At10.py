
comparacao = []
def duplicados(lista):
    for i in lista:
        #comparacao para ver se os elementos da lista não estão presentes na lista nova#
        #Se não estiver ele adicionará atraves da função append#
        #Outra forma de se fazer seria utilizando 2 for e uma variavel auxiliar#
        if i not in comparacao: 
            comparacao.append(i)
    return comparacao
palavras = ['abc', 'abc', 'abc', '123', 'abc', '123', '123']
lista_sem_duplicacao = duplicados(palavras)
print(lista_sem_duplicacao)