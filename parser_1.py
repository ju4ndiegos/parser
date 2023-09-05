
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
    linea = text_file.readline()


funcionando=True
i=0
while funcionando:
    elemento=lista_grande[i]
    
    #sí hay una variable
    if "defVar" == elemento:
        nom_variable = lista_grande[i+1]
        valor= lista_grande[i+2]
        variables[nom_variable]=valor
            
        lista_grande.pop(i)
        lista_grande.pop(i)
        lista_grande.pop(i)
        
        i-=1
        
    if elemento=="defProc":
        nom_proc = lista_grande[i+1]
        parametros= lista_grande[i+2]#TODO revisar los parametros
        variables[nom_variable]=valor
        
    
    #paso para recorrer la lista 
    i+=1
    
    if i == len(lista_grande):
        funcionando=False
    
    
    