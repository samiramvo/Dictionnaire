from heapq import nlargest
dico={'a':567,'b':678,'c':56,'d':436,'e':5667}
trois=nlargest(3,dico,key=dico.get)
print(trois)