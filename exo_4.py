dico={
    "Bananes":4000,
    "Cerises":6755,
    "Ananas":9054
}
key1=input("Entrez la clé")

for key in dico.keys():
    if key1 in dico.keys():
        print("True")
    else:
        print("False")