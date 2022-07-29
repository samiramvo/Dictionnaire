liste=[{"V":"S001"},{"V":"S002"},{"VI":"S001"},{"VI":"S005"},{"V":"S009"},{"VII":"S007"}]
valeur=set(val for dic in liste for val in dic.values())
print(valeur)