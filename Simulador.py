#SIMULACION CLASICO A LO CUANTICO
#MICHAEL BALLESTEROS
#2019-2
from Library.Calculadora import *

def transpuesta(m1):
    """Recibo una matriz y determino su transpuesta -> matriz
    """
    m2=[[(0,0) for x in m1] for x in m1[0]]
    for j in range(len(m1[0])):
        for k in range(len(m1)):
            m2[j][k]=m1[k][j]
    return m2
#############################################
# EXPERIMENTO MULTIPLE RENDIJA CUANTICO
def multiplicacionCuantico(p1,p2):
    """Recibo 2 complejos y los multiplica -> complejo
    """
    a1,b1,a2,b2=p1[0],p1[1],p2[0],p2[1]
    cal=Calculadora()
    res=cal.multiplicacion(a1,a2)
    return (res,b1*b2)
def sumaCuantico(p1,p2):
    """Recibo 2 complejos y los suma -> complejo
    """
    a1,b1,a2,b2=p1[0],p1[1],p2[0],p2[1]
    cal=Calculadora()
    res=cal.suma(a1,a2)
    return (res,b1+b2)
def multiplicarMatrizMatrizCuantico(m1,m2):
    """ Recibo 2 matrices complejas y las multiplico -> matriz Booleana
    """
    m3=[[0 for x in m2[0]] for x in m1]
    for j in range(len(m1)):
        for k in range(len(m2[0])):
            resultado=((0,0),1)
            for h in range(len(m2)):
                resultado=sumaCuantico(multiplicacionCuantico(m1[j][h],m2[h][k]),resultado)
            m3[j][k]=resultado
    return m3
def simuladorCuantico(m1,v):
    rec=multiplicarMatrizMatrizCuantico(m1,m1)
    return rec[v]

#############################################
# EXPERIMENTO MULTIPLE RENDIJA CLASICO
def multiplicacionClasico(d1,d2):
    """Recibo 2 fraccionarios y los multiplica -> complejo
    """
    a1,b1,a2,b2=d1[0],d1[1],d2[0],d2[1]
    resultado = (0,0)
    if (a1==0 or a2==0):
        resultado = (0,1)
    else:
        resultado = (a1*a2,b1*b2)
    return resultado
def sumaClasico(d1,d2):
    """Recibo 2 fraccionrios y los suma -> complejo
    """
    a1,b1,a2,b2=d1[0],d1[1],d2[0],d2[1]
    resultado=0
    if (b1==b2):
        resultado = (a1+a2,b1)
    else:
        resultado = (a1*b2+a2*b1,b1*b2)
    return resultado
def multiplicarMatrizMatrizClasico(m1,m2):
    """ Recibo 2 matrices Clasicas y las multiplico -> matriz Booleana
    """
    m3=[[0 for x in m2[0]] for x in m1]
    for j in range(len(m1)):
        for k in range(len(m2[0])):
            resultado=(0,1)
            for h in range(len(m2)):
                resultado=sumaClasico(multiplicacionClasico(m1[j][h],m2[h][k]),resultado)
            m3[j][k]=resultado
    return m3
def simuladorClasico(m,estadoInicial):
    """ Recibo una matriz de fraccionarios,un vector, que representan
        la matriz dinamica
        el estado del sistema           -> vector con el estado de probabilidad de sistema final
    """
    rem=multiplicarMatrizMatrizClasico(m,m)
    estadoFinal=multiplicarMatrizMatrizClasico(rem,transpuesta([estadoInicial]))
    return rem,estadoFinal
#############################################

#############################################
# EXPERIMENTOS CANICAS
def multiplicarMatrizMatrizBool(m1,m2):
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

def clikearBool(m,clickeo):
    """ Recibo una matriz Booleana y un entero, que representan la matriz dinamica
        y el numero de clikeo que se quiere hacer. -> matriz Booleana
    """
    while clickeo>1:
        m=multiplicarMatrizMatrizBool(m,m)
        clickeo-=1
    return m

def simuladorBool(m,clikeo,estadoInicial):
    """ Recibo una matriz Booleana,un entero,un vector, que representan
        la matriz dinamica
        el numero de clikeo
        el estado del sistema           -> vector con el estado de sistema final
    """
    m1=clikearBool(m,clikeo)
    estadoFinal=multiplicarMatrizMatrizBool(m1,transpuesta([estadoInicial]))
    return estadoFinal
#############################################
