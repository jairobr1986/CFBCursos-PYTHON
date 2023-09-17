# l_carros=["HRV","Golf","Argo"]
t_carros=("HRV","Golf","Argo")
l_carros=list(t_carros)
l_carros[2]="Focus"
t_carros=tuple(l_carros)
# print(t_carros[2])

for x in t_carros:
    print(x)