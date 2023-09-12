
    #A função my_map recebe como parametros uma lista e uma funcao#
def my_mapp(lista_a, f):
        #Dentro da funcao my_map ela ira chamar a funcao que ela recebeu por parametro, no caso a função quadrado
        # que foi passado na hora de chamar a função my_map#
    novalista = f(lista_a)
    print(novalista)
def quadrado(lista_b):
    novalista =[i ** 2 for i in lista_b]
    return novalista

lista_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

my_mapp(lista_num, quadrado)