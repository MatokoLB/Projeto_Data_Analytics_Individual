### O SISTEMA TEM QUE CRIA/EXCLUIR(TALVEZ UM CRUD) O candidato
### O SISTEMA TEM QUE ARMAZENAR DADOS DAS 5 ENTREVISTA PARA CADA candidato (DICIONARIO)
### O SISTEMA TEM QUE BUSCAR OS candidatoS QUE TEM A NOTA IQUAL OU MAIOR PARA VAGA NOTA PARA VAGA PESQUESADA.
### MENU DE ESCOLHA

# lista que ira receber os candidatos
listaDeCandidatos = [] #[]


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
        # criacao de nova lista interando sobre a antiga, sem o nome do usuario removido.
            listaDeCandidatos = [candidato for candidato in listaDeCandidatos if candidato["nome"] != nome]
            print("O Canditato foi excluido.")
            break
        else:
            print("nao ha canditado com esse nome")
            break 
    pass



def pesquisarCandidatoIdeal():
    listaDeAprovados = []
    # print(listaDeCandidatos)
    notas = [0,1,2,3] ### talves coloca um dicionario seja a melhor opcao(a lista muda de valor imposbilitando a chama a def novamente...)
    # print(notas[3])
    for nota in notas:
        notas[nota] = int(input(f"insira a notas: "))
        # print(notas)
    pass
      

    for candidatos in listaDeCandidatos:
        # print(type(candidatos["resultado"]["e"]))
        # print(notas)
        condicao = candidatos["resultado"]["e"] >= notas[0] and candidatos["resultado"]["t"] >= notas[1] and candidatos["resultado"]["p"] >= notas[2] and candidatos["resultado"]["s"] >= notas[3]

        if condicao:
            print("aprovado")
            print(candidatos)
            listaDeAprovados.append(candidatos)

        else:
            print("nao")


    # for candidatos in listaDeCandidatos:
    #     # print(candidatos["resultado"])
    #     condicao = candidatos["resultado"]["e"] and >= candidatos["resultado"]["t"] >= and candidatos["resultado"]["p"] >= and candidatos["resultado"]["s"]:
    #  for x in listaDeCandidatos:
    #         if x == "resultado":
    #               for z in y:
    #                  if x[x]["e"] >= 5 and x[x]["t"] >= 5 and x[x]["p"] >= 5 and x[x]["s"] >= 5 :
    #                     print("aprovado")
    #                     print(x)
    #                  else:
    #                     print("nao")
    #                     print(x)
    #                  break
pass
        

def verLista():
    print(listaDeCandidatos)
pass


verLista()

addCandidato()
addCandidato()


excluirCandidato()
pesquisarCandidatoIdeal()
