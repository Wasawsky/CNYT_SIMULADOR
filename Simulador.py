#SIMULACION CLASICO A LO CUANTICO
#MICHAEL BALLESTEROS
#2019-2

def multiplicarMatrizMatriz(m1,m2):
    """ Recibo 2 matrices Booleanas y las multiplico -> matriz Booleana
    """
    m3=[[0 for x in m2[0]] for x in m1]
    for j in range(len(m1)):
        for k in range(len(m2[0])):
            resultado=0
            for h in range(len(m2)):
                resultado+=m1[j][h]*m2[h][k]
            m3[j][k]=resultado
    return m3

def clikear(m,clickeo):
    """ Recibo una matriz Booleana y un entero, que representan la matriz dinamica
        y el numero de clikeo que se quiere hacer. -> matriz Booleana
    """
    while clickeo>0:
        m=multiplicarMatrizMatriz(m,m)
        clickeo-=1
    return m

def simulador(m,clikeo,estadoInicial):
    """ Recibo una matriz Booleana,un entero,un vector, que representan
        la matriz dinamica
        el numero de clikeo
        el estado del sistema           -> vector con el estado de sistema final
    """
    m=clikear(m,clikeo)
    estadoFinal=multiplicarMatrizMatriz(m,[estadoInicial])
    return estadoFinal

    
#############################################
"""""""""

"""""""""
m1=[]
for i in range(6):
    vf=[int(x) for x in (input().split(" "))]
    m1.append(vf)
v1=[int(x) for x in (input().split(","))]
c = int(input())
#############################################

print(simulador(m1,c,v1))

