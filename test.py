listaDeEntrevistados = []


def addEntrevistado():
    entrevistado = {"nome" : "","resultado":{}}
# loop entre chaves e valores, usando o método:items()
    for x,y in entrevistado.items():
            if x == "nome":
                entrevistado["resultado"] = {"e": 0,"t": 0,"p": 0,"s": 0}
            else:
                for z in y:
                    entrevistado[x][z] =  int(input(f" {z} :"))         
            pass
    listaDeEntrevistados.append(entrevistado)          
pass


addEntrevistado()
print(listaDeEntrevistados)
