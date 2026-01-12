from model.model import Model

model = Model()

model.crea_grafo(1999, "triangle")

distanza, percorso = model.ricerca_percorso()

print(distanza, percorso)