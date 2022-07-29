liste={"a":[2,0,3]}

def list_sum(liste):
    for key in liste.keys():
        som=sum(liste[key])
       
    return som

print(list_sum(liste))