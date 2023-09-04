
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
    
    
    

while linea != "":
    
    lista=elementos_linea(linea)
    
    print(lista)
    #sí hay una variable
    if "defVar" in linea:
        pass
        #print(elemento_despues_espacio(linea))
        #print(elemento_despues_espacio(linea[len("defVar"):]))
        
    
    linea = text_file.readline()