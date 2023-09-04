
archivo = "prueba.txt"

text_file=open(archivo)

linea = text_file.readline()


variables = {}

def elemento_despues_espacio(string):
    """Entran strings como por ejemplo "defVar nom 0" o " defVar ..." y me devuelve defVar
    """
    
    elemento="";
    
    for i in string:
        if i!=" ":
            elemento+=i
        else:
            if elemento!="":
                return elemento
    
    
    

while linea != "":
    
    #sí hay una variable
    if "defVar" in linea:
        
        print(elemento_despues_espacio(linea))
        print(elemento_despues_espacio(linea[len("defVar"):]))
        ubicacion = linea.find("defVar")
        indice_nombre_variable = ubicacion+7
        
        despues_variable=linea[indice_nombre_variable:]
        espacio_despues_variable= despues_variable.find(" ")
        
        nombre_variable= despues_variable[:espacio_despues_variable]
        
    
    linea = text_file.readline()