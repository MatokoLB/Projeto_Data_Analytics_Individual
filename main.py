### O SISTEMA TEM QUE CRIA/EXCLUIR(TALVEZ UM CRUD) O candidato
### O SISTEMA TEM QUE ARMAZENAR DADOS DAS 5 ENTREVISTA PARA CADA candidato (DICIONARIO)
### O SISTEMA TEM QUE BUSCAR OS candidatoS QUE TEM A NOTA IQUAL OU MAIOR PARA VAGA NOTA PARA VAGA PESQUESADA.
### MENU DE ESCOLHA

# lista que ira receber os candidatos
listaDeCandidatos = [['ana',[10, 3, 8, 5]],['jana',[10, 10, 4, 5]],['gil',[10, 7, 4, 5]]] #[]

# listas de tipos de de testes
nomesTestes = ["entrevista","teste teórico","prático teste ","soft skills"]

def addCandidato():    
    nome = input(f"""
                  
        Digite o nome do Candidato: """).lower()
    
    #validaçao de entradas nome sem esta na lista
    if any(nome == candidato for candidato in listaDeCandidatos):
        print("ERRO !!! CANDIDATO JÁ EXITE NA LISTA.")
        return addCandidato()
    elif nome == "":
       print("ERRO !!! CAMPO VAZIO.")
       return addCandidato()
    else:
        print("CHECK OK, PROSSEGUINDO NO CADASTRO.>>>>>>")
     
    notas= []    
    pegaNotas(notas)

     ## adicionar candidato a lista
    listaDeCandidatos.append([nome,notas])
   

def excluirCandidato():
    # verifica se lista esta vazia 
    


    nome = input(f"""

                  
        Digite o nome do Candidato em: """).lower()
    
    #validaçao de entradas nome sem esta na lista
    if nome == "":
       print("ERRO !!! CAMPO VAZIO.")
       return excluirCandidato()

    for candidato in listaDeCandidatos:
        print(candidato)
        if nome in candidato:
                listaDeCandidatos.remove(candidato) 
                print("CHECK OK, CANDIDATO REMOVIDO")
                break
    else:
        print("CANDIDATO NAO ENCONTRADO")
    


def pesquisarCandidatoIdeal():
    #veificar se lista esta vazia
    if listaDeCandidatos == []:
       print("ERRO !!! LISTA CANDIDATOS VAZIA")
       return
    
    Aprovados = []

    notasPesquisa= []
    pegaNotas(notasPesquisa)

    for canditato in listaDeCandidatos:
        notasCandidato = canditato[1]
        qualificado = True            
            
    for notasCandidato,notasPesquisa in zip(notasCandidato,notasPesquisa):
        if notasCandidato < notasPesquisa:
            qualificado = False
            break

    if qualificado:
        Aprovados.append(canditato)  

    if Aprovados:
        print(f"candidatos aprovados")
        for candidatos in Aprovados:
            print(candidatos)
    else:
        print("ninguem passou :( ")


def verLista():

    if listaDeCandidatos == []:
        print("ERRO !!! LISTA CANDIDATOS VAZIA")
    
    for canditato in listaDeCandidatos:
        notasCandidatoStr = [str(x) for x in canditato[1]]
        # print(notasCandidatoStr)
            
        letraEmNomeTestes = [letra[0] for letra in nomesTestes]
    # print(letraEmNomeTestes)
    
        letraNota = zip(letraEmNomeTestes,notasCandidatoStr)
        listaLetraNotas = "_".join(letra + nota for letra,nota in letraNota)
     
        print(F""" 
           {str(canditato[0])}___{listaLetraNotas}""")
     
    
    return
    






pass



def pegaNotas(notas):
    for x in nomesTestes:
        while True:
            try: # captura Erro nao deixando codigo quebra
                nota = int(input(f"""
                        
                    Digite a nota em {x}: """))
                
                if  nota < 0 or nota > 10:  ### validaçao de entradas de 0 A 10
                    print("ERRO !!! INSIRA UMA NOTA VÁLIDA (0-10).")
                else:
                    notas.append(nota)
                    break
            except ValueError:
                print("ERRO !!! INSIRA UM VALOR NUMÉRICO")

    return notas


while True:
    opcoes = input (F"""
    ####################################### S I S T E M A ###########################################      
                                    bem-vindo ao #COMPATIBILITY#                  
                                        SELECIONE UMA OPÇÃO
    #################################################################################################                
                                        
                    
        [1]- ADICIONAR CANDIDATO  [2]- EXCLUIR CANDIDATO       [3]- APLICAR VAGA A CANDIDATO
                    
        
        [4]- VER LISTA            [5]- AUTOMAÇÃO DE CADRASTO   [6]- CRÉDITOS        
                                                                                                  
                                                                                           
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