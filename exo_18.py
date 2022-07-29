def vide(dico):
    if dico=={}:
        return True
    else:
        return False

print(vide({}))
print(vide({1:4,3:7}))