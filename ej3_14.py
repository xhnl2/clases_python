texto = input("Ingrese un texto: ")

# calculamos cuanto hay de cada letra
resum = {}
for c in texto:
    resum[c] = resum.get(c, 0) + 1

# nos fijamos el valor mas largo, para mostrar prolijo
maslargo = len(str(max(resum.values())))

# ordenamos: DSU (decorate-sort-undecorate)
# (pista: esto se puede hacer mejor de otra manera...)
tmp = [(v, k) for k, v in resum.items()]
tmp.sort(reverse=True)
resum = [(k, v) for v, k in tmp]

# mostramos
for k, v in resum:
    print("{} {:{maslargo}d}".format(k, v, maslargo=maslargo))
