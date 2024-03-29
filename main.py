### O SISTEMA TEM QUE CRIA/EXCLUIR(TALVEZ UM CRUD) O candidato
### O SISTEMA TEM QUE ARMAZENAR DADOS DAS 5 ENTREVISTA PARA CADA candidato (DICIONARIO)
### O SISTEMA TEM QUE BUSCAR OS candidatoS QUE TEM A NOTA IQUAL OU MAIOR PARA VAGA NOTA PARA VAGA PESQUESADA.
### MENU DE ESCOLHA

# lista que ira receber os candidatos
listaDeCandidatos = [[],['ana', [1, 10, 10, 10]]] #[]
nomesTestes = ["entrevista","teste teórico","teste prático","soft skills"]

def addCandidato():
    resultado = []
    nome = input(f"""Digite o nome do Candidato em: """).lower()
    for x in nomesTestes:
        nota = int(input(f"""Digite a nota em {x}: """))
        resultado.append(nota)
    candidato = [nome] + [resultado]
    listaDeCandidatos.append(candidato)


# addCandidato()
# print(listaDeCandidatos)

def excluirCandidato():
    nome = input("digite o nome do candidato a ser excluido :").lower()
    for candidato in listaDeCandidatos:
        if nome in candidato:
            indece = candidato.index(nome)
            candidato.pop(indece + 1)
            candidato.pop(indece)

# excluirCandidato()
# print(listaDeCandidatos)

def pesquisarCandidatoIdeal():
    Aprovados = []
    notasPesquisa = []

    for nota in nomesTestes:
        nota = int(input(f"insira de {nota}: "))
        notasPesquisa.append(nota)

    for canditato in listaDeCandidatos:
        if canditato != []:
            print(canditato)
            notasCandidato = canditato[1]
            print(canditato[1])
            qualificado = True
    
    for notasCandidato,notasPesquisa in zip(notasCandidato,notasPesquisa):
        if notasCandidato < notasPesquisa:
            qualificado = False
            print("off")
            break
    
    if qualificado:
        Aprovados.append(canditato)

    if Aprovados:
        print(f"candidatos aprovados")
        for candidatos in Aprovados:
            print(canditato)
    else:
        print("ninguem passou :( ")


        


pesquisarCandidatoIdeal()


pass
        

def verLista():
    print(listaDeCandidatos)
pass


