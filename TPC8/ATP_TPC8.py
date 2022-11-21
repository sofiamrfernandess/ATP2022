#1)a
def inicDiferente(s1, s2):
    res = 0
    s1=s1.lower()
    s2=s2.lower()
    for letra in s1 and letra not in s2:
        res=res+1
    return res

#1)b
def acimaMedia(n):
    res = 0
    lista = []
    soma = 0
    for num in range(n):
        x = int(input("Insira o "+ str(num+1) +" número."))
        lista.append(x)
        soma += x
    media = soma/n
    for num in lista:
        if num > media:
            res += 1
    return res

#1)c
def merge(l1, l2):
    res = l1
    for num in l2:
        if num not in res:
            res.append(num)

    for i in range(len(res)):
        for j in range(i + 1, len(res)):
            if res[i] > res[j]:
                res[i], res[j] = res[j], res[i]
    return res

#1)d
def figuais(f1, f2):
    file1 = open(f1)
    file2 = open(f2)
    for line in file1:
        if line in file2:
            res = True
        else:
            res = False
    file1.close()
    file2.close()
    return res
#2)a
def figuais(f1, f2):
    file1 = open(f1)
    file2 = open(f2)
    for line in file1:
        if line in file2:
            res = True
        else:
            res = False
    file1.close()
    file2.close()
    return res
#2)b
def listarPorGenero(cinemateca, genero):
    res=[]
    for filme in cinemateca:
        title, year, elenco, genres = filme
        for genre in genres:
            if genero == genre:
                res.append(title)
    res.sort()
    return res

#2)c
def maiorElenco(cinemateca):
    elencoTamanho = 0
    for filme in cinemateca:
        title, year, elenco, genres = filme
        if len(elenco) > elencoTamanho:
            maiorElenco = title
            elencoTamanho = len(elenco)
    return maiorElenco
#2)d
def filmePorGenero( cinemateca ):
    genresTotal = [] 
    for filme in cinemateca:
        title, year, elenco, genres = filme
        for genre in genres:
            if genre not in genresTotal:
                genresTotal.append(genre)
    distrib = {}.fromkeys(genresTotal, 0)
    
    for filme in cinemateca:
        title, year, elenco, genres = filme
        for genre in genres:
            if genre in distrib.keys():
                distrib[genre] += 1
            else:
                distrib[genre] = 1    
    return distrib
#2)e
import matplotlib.pyplot as plt

def graph(distrib):
    fig1 = plt.figure(figsize = (10, 5))
    plt.bar(distrib.keys(), distrib.values(), color= "purple", width= 0.3)
    plt.xticks([x for x in range(0, len(distrib.keys()))], distrib.keys())
    plt.title("Gráfico da distribuição")
    plt.ylabel("Num de Filmes")
    plt.show()
    return

