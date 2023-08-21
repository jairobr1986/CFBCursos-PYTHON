carros = ["HRV", "Golf", "Argo", "Focus"]
carros[2] = "Jairo"
carros.append("Fit")
carros.append("Fusion")
carros.append("Polo")

carros.remove("Jairo")

# .pop remove o último elemento da lista
carros.pop()

# remove o item selecionado
del carros[1]

# limpa toda a lista
# carros.clear()

carros2 = ["Fusca", "147","Brasilia", "Celta"]

carros3 = carros+carros2

print(str(len(carros3)) + " carros na lista")

print(carros3)