liste={"a  800":[2,0,3],
    "b 5000":[9,5,4],
    "c   100":[1,0,4]
}
print(liste)
new_dict={x.translate({32:None}):y for x,y in liste.items()}
print("Nouveau dictionnaire:",new_dict)
