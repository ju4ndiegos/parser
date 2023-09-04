
archivo = "prueba.txt"

text_file=open(archivo)

linea = text_file.readline()


variables = {}

def elementos_linea(string:str):
    """Entran strings como por ejemplo "defVar nom 0" o " defVar ..." y me devuelve defVar
    """
    string=string.replace("\n","")
    lista=[]
    elemento=""
    
    for i in string:
        if i!=" ":
            elemento+=i
        if i==" " or i==string[-1]:
            if elemento!="":
                lista.append(elemento)
                elemento=""
    
    return lista
    
    
    
lista_grande=[]
while linea != "":
    
    lista=elementos_linea(linea)
    lista_grande+=lista
    for i in range(lista_grande):
        elemento=lista_grande[i]
        #sí hay una variable
        if "defVar" ==elemento:
            nom_variable = lista_grande[i+1]
            valor= lista_grande[i+2]
            variables[nom_variable]=valor
        #print(elemen   ,   to_despues_espacio(linea))
        #print(elemento_despues_espacio(linea[len("defVar"):]))
        
    
    
    
    linea = text_file.readline()