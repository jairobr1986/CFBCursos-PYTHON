import os
carros=[]
carro=input("Digite o nome do novo carro: ")
while carro !="-1":
    carros.append(carro)
    carro=input("Digite o nome do novo carro: ")
os.system("cls")
for x in carros:
    print(x)
print("\nFim do Loop")