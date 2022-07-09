import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

escolha = len(names)

escolhido = random.randint(0, escolha - 1)

VaiPagar = names[escolhido]

print(VaiPagar + " vai pagar a conta hoje.")



