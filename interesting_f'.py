colors = ['balck','pink','white']
sizes =['S','M','L','XL']
for t_shirt in (f'{c} {s}' for c in colors for s in sizes):
    print(t_shirt)