
archivo = "prueba.txt"

text_file=open(archivo)

linea = text_file.readline()


variables = {}
procedimientos ={}

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
    
def sacar_parametros(sublista:list):
    parametros=[]
    if "(" in sublista[0]:
        for i in sublista:
            parametros.append(i.replace("(","").replace(")",""))
            if ")"in i:
                if i==")":
                    parametros.pop(-1)
                break
    return parametros
            
    
    
lista_grande=[]
while linea != "":
    
    lista=elementos_linea(linea)
    lista_grande+=lista
    linea = text_file.readline()

simbolos_reservados=["while",";","defVar","defProc","="]

funcionando=True
Error=False

i=0
while funcionando and Error==False:
    elemento=lista_grande[i]
    
    #sí hay una variable
    if "defVar" == elemento:
        nom_variable = lista_grande[i+1]
        valor= lista_grande[i+2]
        if nom_variable not in simbolos_reservados  and valor not in simbolos_reservados:
            variables[nom_variable]=valor
        else:
            Error=True
        lista_grande.pop(i)
        lista_grande.pop(i)
        lista_grande.pop(i)
        
        i-=1
        
    if elemento=="defProc":
        nom_proc = lista_grande[i+1]
        parametros= sacar_parametros(lista_grande[i+2:])
        procedimientos[nom_proc]=parametros
        #print(parametros)
        
    
    #paso para recorrer la lista 
    i+=1
    
    if i == len(lista_grande):
        funcionando=False
    
    
    