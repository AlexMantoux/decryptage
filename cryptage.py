def finalTask(L):
    abc = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for j in range(len(L)):
        for i in range(len(abc)):
            if L[j]==i:
                L[j]=abc[i]
    print(L)



def replaceValue(L,a,b):
    cry=[]
    for i in range(len(L)):
        x=L[i]
        y = a*x+b
        y = y%26
        cry.append(y)
    return cry

def cryptage(L):
    abc = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for j in range(len(L)):
        for i in range(len(abc)):
            if L[j]==abc[i]:
                L[j]=i
    return L


def makeAlist(word):
    liste = []
    for letters in range(len(word)):
        liste.append(word[letters])
    return liste

finalTask(replaceValue(cryptage(makeAlist("zoubi")), 5,2))