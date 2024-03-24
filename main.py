### O SISTEMA TEM QUE CRIA/EXCLUIR(TALVEZ UM CRUD) O candidato
### O SISTEMA TEM QUE ARMAZENAR DADOS DAS 5 ENTREVISTA PARA CADA candidato (DICIONARIO)
### O SISTEMA TEM QUE BUSCAR OS candidatoS QUE TEM A NOTA IQUAL OU MAIOR PARA VAGA NOTA PARA VAGA PESQUESADA.
### MENU DE ESCOLHA

# lista que ira receber os candidatos
listaDeCandidatos = [{'nome': 'ana', 'resultado': {'e': 10, 't': 10, 'p': 10, 's': 10}}, {'nome': 'joao', 'resultado': {'e': 2, 't': 5, 'p': 10, 's': 0}}, {'nome': 'jana', 'resultado': {'e': 0, 't': 0, 'p': 0, 's': 10}}] #[]


def addCandidato():
    candidato = {"nome" : "","resultado":{}}
# loop entre chaves e valores, usando o método:items()
    for x,y in candidato.items():
            if x == "nome":
                # pega nome do candidato 
                candidato[x] = input(f" {x} :").lower()
                # chave resultado acresentada automaticamente
                candidato["resultado"] = {"e": 0,"t": 0,"p": 0,"s": 0}

                # talvez add def verificar nome ja exitente:
            else:
                for z in y:
                    candidato[x][z] =  int(input(f" {z} :")) 
                # talvez add def verificar valores intevalo de 0 a 10:       
            pass
    listaDeCandidatos.append(candidato)
    print("Candidato adicionado")        
pass



def excluirCandidato():
    global listaDeCandidatos

    nome = input("digite o nome do candidato a ser excluido :").lower()

    for candidatos in listaDeCandidatos:
        if candidatos["nome"] == nome: 
        # criacao de nova lista interando sobre a antiga sem o nome do usuario removido
            listaDeCandidatos = [candidato for candidato in listaDeCandidatos if candidato["nome"] != nome]
            print("O Canditato foi excluido.")
            break
        else:
            print("nao ha canditado com esse nome")
            break 
    pass

def pesquisarCandidato():
    pass

def verLista():
    pass

print(listaDeCandidatos)