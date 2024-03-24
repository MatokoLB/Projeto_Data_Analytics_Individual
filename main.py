### O SISTEMA TEM QUE CRIA/EXCLUIR(TALVEZ UM CRUD) O candidato
### O SISTEMA TEM QUE ARMAZENAR DADOS DAS 5 ENTREVISTA PARA CADA candidato (DICIONARIO)
### O SISTEMA TEM QUE BUSCAR OS candidatoS QUE TEM A NOTA IQUAL OU MAIOR PARA VAGA NOTA PARA VAGA PESQUESADA.
### MENU DE ESCOLHA

listaDeCandidatos = []


def addCandidato():
    candidato = {"nome" : "","resultado":{}}
# loop entre chaves e valores, usando o método:items()
    for x,y in candidato.items():
            if x == "nome":
                #pega nome do candidato 
                candidato[x] = input(f" {x} :")
                candidato["resultado"] = {"e": 0,"t": 0,"p": 0,"s": 0}
            else:
                for z in y:
                    candidato[x][z] =  int(input(f" {z} :"))         
            pass
    listaDeCandidatos.append(candidato)          
pass


def excluirCandidato():
    pass

def pesquisarCandidato():
    pass

def verLista():
    pass


addCandidato()
print(listaDeCandidatos)

