#---leer el archivo----------
archivo = "prueba.txt"

text_file=open(archivo)
#-------------------------



#Estructuras contención
class Block:
    block=""
    def Block(self,block:str):
        self.block=block
variables = {}
procedimientos ={}
#-----------------------

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
    
def sacar_parametros(sublista:list,Error:bool):
    parametros=[]
    iteraciones=0
    if "(" in sublista[0]:
        for i in sublista:
            iteraciones+=1
            
            parametros.append(i.replace("(","").replace(")",""))
            if ")"in i:
                if i==")" or i=="(":
                    parametros.pop(-1)
                break
    else:
        Error=False
            
    return iteraciones,parametros

def sacar_bloques(sublista:list,Error:bool): 
    bloque=""
    
    
    i=0
    buscando=True
    dentro_bloque=False
    while buscando:
        if "{" in sublista[i]:
            dentro_bloque=True
        elif dentro_bloque:
            bloque+=sublista[i].replace("{","").replace("}","")
            if "}"in sublista[i]:
                dentro_bloque=False
                buscando=False
        i+=1
        if i == len(sublista)-1:
            buscando=False
            Error=True
    return i-1,bloque

#---------lectura archivo---------------
linea = text_file.readline()
lista_grande=[]
while linea != "":
    
    lista=elementos_linea(linea)
    lista_grande+=lista
    linea = text_file.readline()
#------------------------------------

simbolos_reservados=["while",";","defVar","defProc","="]


#----------------parser-----------
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
        i1,parametros= sacar_parametros(lista_grande[i+2:],Error)
        i2,block_commands=sacar_bloques(lista_grande[i+3:],Error)
        procedimientos[nom_proc]=[parametros,block_commands]
        for _ in range(i1+i2):
            print("elimino ->",lista_grande.pop(i))
        
        i-=1
            
    if elemento=="{":
        print(lista_grande[i:])
        input("->")
        
    
    #paso para recorrer la lista 
    i+=1
    
    if i == len(lista_grande):
        funcionando=False
    
#--------------------------------------

#pruebas----------------    
#print(procedimientos)
print("Hubo un error ->"+Error)

