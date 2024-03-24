### O SISTEMA TEM QUE CRIA/EXCLUIR(TALVEZ UM CRUD) O ENTREVISTADO
### O SISTEMA TEM QUE ARMAZENAR DADOS DAS 5 ENTREVISTA PARA CADA ENTREVISTADO (DICIONARIO)
### O SISTEMA TEM QUE BUSCAR OS ENTREVISTADOS QUE TEM A NOTA IQUAL OU MAIOR PARA VAGA NOTA PARA VAGA PESQUESADA.
### MENU DE ESCOLHA

listaDeEntrevistados = []


def addEntrevistado():
    entrevistado = {"nome" : "","resultado":{}}
# loop entre chaves e valores, usando o método:items()
    for x,y in entrevistado.items():
            if x == "nome":
                entrevistado[x] = "ana" #input(f" {x} :")
                entrevistado["resultado"] = {"e": 0,"t": 0,"p": 0,"s": 0}
            else:
                for z in y:
                    entrevistado[x][z] =  int(input(f" {z} :"))         
            pass
    listaDeEntrevistados.append(entrevistado)          
pass

def excluirEntrevistado():
    pass

def pesquisarEntrevistado():
    pass

def verLista():
    pass


addEntrevistado()
print(listaDeEntrevistados)

addEntrevistado()
print(listaDeEntrevistados)

addEntrevistado()
print(listaDeEntrevistados)
