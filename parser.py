#Inicializo variables
x,y=1,1

#0 norte, #1 oriente, #2 occidente (izquierda), #3 sur
direction=0

def giro():
    direction+=1
    direction%=4
    
def put():
    return True

def move_Forward():
    if direction==1 and x-1>0: #no se sale de los bordes
        x+=1
    elif direction ==2:#TODO hay un limite??
        x-=1
        
    elif direction==3: #TODO hay un limite??
        y+=1
        
    elif direction==0 and y-1>0: #no se sale de los bordes
        y-=1
