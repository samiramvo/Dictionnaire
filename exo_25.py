dico={
    "a":[2,3],
    "b":"sam",
    "c":56
}

for row in zip(*([key]+(value) for key,value in sorted(dico.items()))):
    print(*row)