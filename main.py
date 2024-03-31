### O SISTEMA TEM QUE CRIA/EXCLUIR(TALVEZ UM CRUD) 
### O SISTEMA TEM QUE ARMAZENAR DADOS DAS 4 ENTREVISTA PARA CADA candidato 
### O SISTEMA TEM QUE BUSCAR OS candidatoS QUE TEM A NOTA IQUAL OU MAIOR PARA VAGA NOTA PARA VAGA PESQUESADA.
### MENU DE ESCOLHA

# lista que ira receber os candidatos
listaDeCandidatos = [] #[]
# listas de tipos de de testes / essa lista define o numero de notas que canditado vai ter.
nomesTestes = ["entrevista","teste teórico","prático teste ","soft skills"]

def addCandidato():    
    nome = input(f"""
                  
        Digite o nome do Candidato: """).lower()
    
    #validaçao de entradas nome sem esta na lista

    if any(nome == candidato[0] for candidato in listaDeCandidatos):
        print(f""" 
                ERRO !!! CANDIDATO JÁ EXITE NA LISTA.""")
        return addCandidato()
    
    elif nome == "":
       print(f"""
               ERRO !!! CAMPO VAZIO.""")
       return addCandidato()
    else:
        print(f""" 
                    CHECK OK, PROSSEGUINDO NO CADASTRO.>>>>>>""" )
     
    notas= []    
    pegaNotas(notas)
     ## adicionar candidato a lista
     
    listaDeCandidatos.append([nome,notas])
    print(f""" 
                    CHECK OK, CANDIDATO {nome.upper()} CADRASTADO.>>>>>>""" )
   

def excluirCandidato():
    if not listaDeCandidatos:
       print(f"""
               ERRO !!! LISTA CANDIDATOS VAZIA""")
       return

    nome = input(f"""

                  
                Digite o nome do Candidato em: """).lower()
    
    #validaçao de entradas nome sem esta na lista
    if nome == "":
       print(f"""
               ERRO !!! CAMPO VAZIO.""")
       return excluirCandidato()

    for candidato in listaDeCandidatos:
        print(candidato)
        if nome in candidato:
                listaDeCandidatos.remove(candidato) 
                print(F"""
                        CHECK OK, CANDIDATO REMOVIDO""")
                break
    else:
        print(F"""
                CANDIDATO NÃO ENCONTRADO.""")
    

def pesquisarCandidatoIdeal():
    # Verificar se lista está vazia
    if not listaDeCandidatos:
        print("ERRO !!! LISTA DE CANDIDATOS VAZIA.")
        return

    notasPesquisa = []
    pegaNotas(notasPesquisa)

    Aprovados = []
    
    for candidato in listaDeCandidatos:
        notasCandidato = candidato[1]
        qualificado = True

        for notaCandidato, notaPesquisa in zip(notasCandidato, notasPesquisa):
            if notaCandidato < notaPesquisa:
                qualificado = False
                break

        if qualificado:
            Aprovados.append(candidato)

    if Aprovados:
        verLista(Aprovados,"APROVADO")
    else:
        print("NINGUÉM PASSOU NO TESTE :(")


def verLista(lista,texto):

    listaDeCandidatosFormatada = []
    if not lista:
        print(f"""
                ERRO !!! LISTA CANDIDATOS VAZIA""")
        return
    
    for canditato in lista:
        notasCandidatoStr = [str(x) for x in canditato[1]]
        # print(notasCandidatoStr)
            
        letraEmNomeTestes = [letra[0] for letra in nomesTestes]
        
        # print(letraEmNomeTestes)
        letraNota = zip(letraEmNomeTestes,notasCandidatoStr)
        listaLetraNotas = "_".join(letra + nota for letra,nota in letraNota)
     
        # print(F""" 
        #    {str(canditato[0])}___{listaLetraNotas}""")
        
        listaDeCandidatosFormatada.append([canditato[0],listaLetraNotas])
    
    print(listaDeCandidatosFormatada)
    while True:
        print(f''' 
        #########################################################################################################      
                   CANDIDATO  {texto if texto else ""}                  ████                 RESULTADO
        #########################################################################################################''')
        for canditado in listaDeCandidatosFormatada:
            print(f""" 
                  {canditado[0]}                                                {canditado[1]}
        ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░""")
        x = input(f"""                                                                                  [7]-SAIR """)
        if x == "7":
           break


def pegaNotas(notas):
    for x in nomesTestes:
        while True:
            try: # captura Erro nao deixando codigo quebra
                nota = int(input(f"""
                        
                    Digite a nota em {x}: """))
                
                if  nota < 0 or nota > 10:  ### validaçao de entradas de 0 A 10
                    print(f"""
                            ERRO !!! INSIRA UMA NOTA VÁLIDA (0-10).""")
                else:
                    notas.append(nota)
                    break
            except ValueError:
                print(f"""
                            ERRO !!! INSIRA UM VALOR NUMÉRICO""")
    return notas


def automacaoCadrasto():
    global listaDeCandidatos
    x =input (F"""
    ██████████████████████████████████████████████████████████████████████████████████████████████████████████              

         
                        ╔═══════════════════════════════╗  ╔═══════════════════════════════╗   
                        ║ [1]- PRENCHER LISTA           ║  ║ [2]- LIMPA LISTA              ║  
                        ╚═══════════════════════════════╝  ╚═══════════════════════════════╝ 
                                                           
                                                                                                  [7]-SAIR
                    
    ██████████████████████████████████████████████████████████████████████████████████████████████████████████
                    """)
    if x == "1":
        if listaDeCandidatos:
            print(f"""
                    LISTA NÃO ESTA VAZIA""")
        else:
            listaDeCandidatos = [['ana',[10, 10, 10, 10]],['jana',[5, 10, 4, 5]],
                                 ['gil',[10, 7, 4, 5]],['thales',[8, 2, 3, 1]],
                                 ['maria',[3, 6, 3, 6]],['jubirildo',[7, 7, 6, 3]],
                                 ['oliver',[8, 8, 9, 7]],['lucas',[1, 4, 8, 2]]]
            print(f"""
                    LISTA PRENCHIDA """)
    elif x == "2":
        if not listaDeCandidatos:
            print(f"""
                    LISTA JÁ ESTA VAZIA""")
        else:
            listaDeCandidatos.clear()
            print(f"""
                    LISTA LIMPA""")



while True:
    opcoes = input (F"""
    ████████████████████████████████████████████  S I S T E M A ██████████████████████████████████████████████    
                                        bem-vindo ao #COMPATIBILITY#                  
                                              SELECIONE UMA OPÇÃO
    ██████████████████████████████████████████████████████████████████████████████████████████████████████████              

         
       ╔═══════════════════════════════╗  ╔═══════════════════════════════╗  ╔═══════════════════════════════╗   
       ║ [1]- ADICIONAR CANDIDATO      ║  ║ [2]- EXCLUIR CANDIDATO        ║  ║ [3]- APLICAR VAGA A CANDIDATO ║
       ╚═══════════════════════════════╝  ╚═══════════════════════════════╝  ╚═══════════════════════════════╝
       
       ╔═══════════════════════════════╗  ╔═══════════════════════════════╗  ╔═══════════════════════════════╗   
       ║ [4]- VER LISTA                ║  ║ [5]- AUTOMAÇÃO DE CADRASTO    ║  ║ [6]- CRÉDITOS                 ║
       ╚═══════════════════════════════╝  ╚═══════════════════════════════╝  ╚═══════════════════════════════╝             
          
                                                           
                                                                                                  [7]-SAIR
                    
    ██████████████████████████████████████████████████████████████████████████████████████████████████████████
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
        verLista(listaDeCandidatos,None)
    elif opcoes == "5":
        automacaoCadrasto()
    elif opcoes == "6":
     x =  input(f"""
              
    ██████████████████████████████████████████████████████████████████████████████████████████████████████████            

           MMM.           .MMM
           MMMMMMMMMMMMMMMMMMM
           MMMMMMMMMMMMMMMMMMM               PROJETO DE DESENVOLVIDO POR @MATOKOLB:
          MMMMMMMMMMMMMMMMMMMMM                 https://github.com/MatokoLB?
        MMMMMMMMMMMMMMMMMMMMMMMM                 
         MMMMMMMMMMMMMMMMMMMMMMM     
        MMMM::- -:::::::- -::MMMM                 
         MM~:~ 00~:::::~ 00~:~MM
    .. MMMMM::.00:::+:::.00::MMMMM ..        PROGRAMADORES CARIOCAS e CNseg - DATA ANALITYS
          .MM::::: ._. :::::MM.                 SENAC/RESILIA
             MMMM;:::::;MMMM
      -MM        MMMMMMM                              
      ^  M+     MMMMMMMMM                    INSTRUTOR William Firmino:
          MMMMMMM MM MM MM                      https://github.com/williamfirmino92      
               MM MM MM MM                      https://www.linkedin.com/in/william-firmino-87a2ba80  
               MM MM MM MM                
            .~~MM~MM~MM~MM~~.
         ~~~~MM:~MM~~~MM~:MM~~~~
        ~~~~~~==~==~~~==~==~~~~~~
         ~~~~~~==~==~==~==~~~~~~
                                                                                                    [N]- SAIR
    ██████████████████████████████████████████████████████████████████████████████████████████████████████████
                  """)
    elif opcoes == "7":
        print(f"""
              
    ██████████████████████████████████████████████████████████████████████████████████████████████████████████            
 
              




                                *FINALIZANDO OPERAÇÃO* - OBRIGADO, VOLTE SEMPRE.





             
              
    ██████████████████████████████████████████████████████████████████████████████████████████████████████████
                  """)
        exit()
    else:
        pass