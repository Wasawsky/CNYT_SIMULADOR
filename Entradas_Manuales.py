#############################################
"""""""""


m1=[]
for i in range(6):
    vf=[int(x) for x in (input().split(" "))]
    m1.append(vf)
v1=[int(x) for x in (input().split(","))]
c = int(input())
#############################################

#print(simuladorBool(m1,c,v1))
"""""""""
"""""""""
m1=[]
for i in range(3):
    vf=[tuple(map(int, x.split("/"))) for x in (input().split(" "))]
    m1.append(vf)
v1=[tuple(map(int, x.split("/"))) for x in (input().split(" "))]
print(simuladorClasico(m1,v1))
"""""""""
m1=[]
for i in range(8):
    vf=[x.split("/") for x in (input().split(" "))]
    vd=[]
    for k in vf:
        t=tuple(map(float, k[0].split(",")))
        p=float(k[1])
        tf=(t,p)
        vd.append(tf)
    m1.append(vd)   
v=int(input())
print(simuladorCuantico(m1,v))
