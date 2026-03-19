satrudnik = {"pasha":1200,
         "masha":222,
         "sasha":250,
         "dasha":250,
         "dimon":120}
minimal = 1200
for i in satrudnik.values():
    if i < minimal:
        minimal = i
for d in satrudnik:
    if satrudnik[d] == minimal:
        print(d)
