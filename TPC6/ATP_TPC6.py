import csv
import matplotlib.pyplot as plt 

def lerObras():
    file=open("obras.csv",encoding="UTF8")
    file.readline()
    csv_file= csv.reader(file,delimiter=";")
    lista=[]
    for linha in csv_file:
        lista.append(tuple(linha))
    file.close()
    return lista

def contarObras(obras):
    return len(obras)

def imprimeObras(obras):
    for obra in obras:
        nome, desc, ano, periodo, compositor, duracao, id =obra
        print(f"| {nome[:10] :^20}   |   {desc[:30] :^10}   |   {ano[:10]:^10}    | {compositor[:15]:^10}")
    return  

def ordenaTitle(obras):
    lista= []
    for obra in obras :
        nome, desc, ano, periodo, comp, duracao, id = obra
        lista.append((nome, ano))
    lista.sort(key= lambda x: x[0])
    return lista

def ordenaYear(obras):
    lista= []
    for obra in obras :
        nome, desc, ano, periodo, comp, duracao, id = obra
        lista.append((nome, ano))
    lista.sort(key= lambda x: x[1])
    return lista

def ordenaComp(obras):
    lista= []
    for obra in obras :
        nome, desc, ano, periodo, comp, duracao, id = obra
        if comp not in lista: 
            lista.append((comp))
    lista.sort()

def distribPeriodo(obras):
    distrib={}
    for obra in obras :
        nome, desc, ano, periodo, comp, duracao, id = obra
        
        if periodo in distrib.keys():
            distrib[periodo] += 1
        else:
            distrib[periodo] = 1
    return distrib

def distribAno(obras):
    distrib = {}
    for obra in obras:
        nome, desc, ano, periodo, comp, duracao, id = obra
        if ano in distrib.keys():
            distrib[ano] += 1
        else:
            distrib[ano] = 1
    return distrib

def distribComp(obras):
    distrib = {}
    for obra in obras:
        nome, desc, ano, periodo, comp, duracao, id = obra
        if comp in distrib.keys():
            distrib[comp] += 1
        else:
            distrib[comp] = 1
    return distrib

def graph(distrib):
    fig1 = plt.figure(figsize = (30, 15))
    plt.bar(distrib.keys(), distrib.values(), color= "pink", width= 0.5)
    plt.xticks([x for x in range(0, len(distrib.keys()))], distrib.keys(), rotation='vertical')
    plt.show()
    return

def prob(obras):
    res= []
    listaComp= []
    for obra in obras:
        nome, desc, ano, periodo, comp, duracao, id = obra
        if comp not in listaComp:
            listaComp.append(comp)
    for compositor in listaComp:
        listaObras= []
        for obra in obras:
            nome, desc, ano, periodo, comp, duracao, id = obra
            if  comp == compositor:
                listaObras.append(nome)
        res.append((compositor, listaObras))
    return res

def lerProb(lista):
    for tuplo in lista:
        autor, obras = tuplo
        i = 1
        branco = ""
        print(f"\n{autor:<30}|{obras[0]:<20}")
        while i != len(obras):
            print(f"{branco:<30}|{obras[i]:<20}")
            i += 1
    return