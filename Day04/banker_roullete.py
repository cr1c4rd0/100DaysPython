import random
#tomar de una lista de jugadores quien va a empezar la partida de forma aleatoria
names_string = input("Give me everybody's names, separated by a comma. ")
#el metodo split permite agregar una coma para agregar diferentes items a una lista
names = names_string.split(", ")

print(f"Players: {names}")

#la función len() permite saber la cantidad de items en una lista
players = len(names)
roullete = names[random.randint(0, players - 1)]
print(f"{roullete} is going to buy the meal today!")

#con random.choice() me escoge un elemento random de una lista
person = random.choice(names)
print(f"{person} is going to buy the meal today!")
