liste={'1':['a','b'],'2':['c','d']}

for values in liste.values():
    print(dict(zip(*values)))