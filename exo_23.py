from collections import Counter
liste=[{'a':'b','amount':500},{'a':'b','amount':600}]
result=Counter
for c in liste:
    result[c['a']]+=c['amount']
print(result)