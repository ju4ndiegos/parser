#parser.py

x,y=1,1

#0, norte, #1 oriente, #2 occidente, #3 sur
direction=0

def giro():
    direction+=1
    direction%=4
    
def put():
    return True

def move_Forward():
    if direction==1 and x-1>0:
        x-=1
    elif direction==3:
        x+=1
    elif 