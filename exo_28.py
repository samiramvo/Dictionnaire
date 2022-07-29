liste={"a":[2,0,3],
    "b":[9,5,4],
    "c":[1,0,4]
}

def list_sort(liste):
    liste1=[]
    for key in liste.keys():
        var=key,sorted(liste[key])
        liste1.append(var)
    return dict(liste1)

print(list_sort(liste))