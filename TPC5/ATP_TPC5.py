# Lê a informação do ficheiro para um modelo 
# Especifique um programa que ao executar apresenta as tabelas correspondentes às distribuições pedidas

#idade,sexo,tensão,colesterol,batimento,temDoença

def lerinf(fnome):
    f=open(str(fnome),"r")
    modelo=[]

    for line in f:     
        paciente=line[:-1].split(",")
        modelo.append(paciente)
    f.close
    return modelo

lerinf("myheart.csv")

# Calcula a distribuição da doença p/sexo
def doencapsexo(list):
    m=0
    f=0
    for p in list:
        if p[-1]=="1":
            if p[1]=="M":
                m+=1
            if p[1]=="F":
                f+=1
    distrib=[("M",m),("F",f)]
    return distrib

doencapsexo(lerinf("myheart.csv"))

# Calcula a distribuição da doença por escalões etários: [30-40], [35-39], [40-45],...
def disteta(list):
    distrib=[]
    e=30
    while e<85:
        escalão=[e,e+5]
        n=0
        for p in list:
            if p[-1]=="1" and escalão[0]<=int(p[0])<escalão[1]:
                n+=1
        distrib.append((escalão,n))
        e+=5
    return distrib
disteta(lerinf("myheart.csv"))

# Calcula a distribuição da doença por níveis de colesterol. Intervalo de 10 unidades.
def colesterol(modelo):
    c=0
    coles=[]
    while c<=540:
        escalão=[c,c+10]
        n=0
        for i in modelo:
            if i[-1]=="1" and escalão[0] <=int(i[3])<escalão[1]:
                n=n+1
            coles.append(escalão,n)
            c=c+10
    return coles 

def tabela(dados,critério):
    if critério==doencapsexo:
        print(" Sexo   | nº de pessoas doentes")
    if critério==disteta:
        print("Distribuição etária   | nº de pessoas doentes")
    if critério==colesterol:
        print("Colestrol   | nº de doentes")
    for i in critério(dados):
        print(i[0], "|", i[1], end="")

dados = lerinf("myheart.cvs")
tabela(dados,doencapsexo)
tabela(dados,disteta)
tabela(dados,colesterol)