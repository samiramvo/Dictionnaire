from collections import Counter


dico={
    "Math":81,
    "Physique":83,
    "Chimie":87
}
dico=Counter(dico)
print(dico.most_common())
