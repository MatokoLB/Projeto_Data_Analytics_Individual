### O SISTEMA TEM QUE CRIA/EXCLUIR(TALVEZ UM CRUD) O candidato
### O SISTEMA TEM QUE ARMAZENAR DADOS DAS 5 ENTREVISTA PARA CADA candidato (DICIONARIO)
### O SISTEMA TEM QUE BUSCAR OS candidatoS QUE TEM A NOTA IQUAL OU MAIOR PARA VAGA NOTA PARA VAGA PESQUESADA.
### MENU DE ESCOLHA

# lista que ira receber os candidatos
listaDeCandidatos = [["ana",[0,0,0,0]],["jaoo",[0,0,0,0]]] #[]
nomesTestes = ["entrevista","teste teórico","teste prático","soft skills"]

def addCandidato():
    resultado = []

    nome = input(f"""
                 
        Digite o nome do Candidato em: 
                 
                  """).lower()
    #validaçao de entradas nome sem esta na lista

    for x in nomesTestes:
        
        nota = int(input(f"""
                         

        Digite a nota em {x}: """))

        ### validaçao de entradas de 0 A 10
        if nota != int or nota < 0 or nota > 10:
            print("ERRO !!! insira um Valor valido numero entre: 0-10")

        resultado.append(nota)
    candidato = [nome] + [resultado]
    listaDeCandidatos.append(candidato)


def excluirCandidato():
    ## verifica se lista esta vazia 

    nome = input("Digite o nome do candidato a ser excluido :").lower()
    ## valida entrada vazia

    for candidato in listaDeCandidatos:
        if nome in candidato:
            indece = candidato.index(nome)
            candidato.pop(indece)  # Removendo o nome
            if len(candidato) == 1:  # Se a lista de notas está vazia
                listaDeCandidatos.remove(candidato)
            break
        else:
            print(f"""Candidato não Encontrado""")



def pesquisarCandidatoIdeal():
    #veificar se lista esta vazia


    Aprovados = []
    notasPesquisa = []

    for nota in nomesTestes:
        nota = int(input(f"insira de {nota}: "))
        notasPesquisa.append(nota)

    for canditato in listaDeCandidatos:
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


def verLista():
    print(listaDeCandidatos)
pass

while True:
    opcoes = input (F"""
    ####################################### S I S T E M A ###########################################      
                                    bem-vindo ao #COMPATIBILITY#                  
                                        SELECIONE UMA OPÇÃO
    #################################################################################################                
                                        
                    
        [1]- ADICIONAR CANDIDATO    [2]- EXCLUIR CANDIDATO      [3]- APLICAR VAGA A CANDIDATO
                    
        
        [4]- VER LISTA              [5]- OPÇÕES AUTOMAÇÃO       [6]- CRÉDITOS        
                                                                                                  
                                                                                           
                                                                                           [7]-SAIR
    #################################################################################################  
                    """)
    
    if opcoes == "1":
        addCandidato()
        pass
    elif opcoes == "2":
        excluirCandidato()
        pass
    elif opcoes == "3":
        pesquisarCandidatoIdeal()
    elif opcoes == "4":
        verLista()
    elif opcoes == "5":
       pass
    elif opcoes == "6":
        pass
    elif opcoes == "7":
        print(f"""
              
    #################################################################################################                

              


                            *FINALIZANDO OPERAÇÂO* - OBRIGADO, VOLTE SEMPRE.


             
              
    ################################################################################################# 
                  """)
        exit()
    else:
        pass