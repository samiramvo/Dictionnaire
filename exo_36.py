from collections import defaultdict
liste=["a","b","c","d"]
liste1=[1,5,8,6]
temp=defaultdict(set)

for c,i in zip(liste,liste1):
    temp[c].add(i)
print(temp)