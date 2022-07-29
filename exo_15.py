dico={
    "Banane":2000,
    "Cerise":5000,
    "Ananas":1000
}
max_key=max(dico.keys(),lambda x:dico[x])
min_key=min(dico.keys(),lambda x:dico[x])
print(dico(max_key))
print(dico(min_key))