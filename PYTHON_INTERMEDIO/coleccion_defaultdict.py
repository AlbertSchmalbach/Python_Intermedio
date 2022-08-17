from collections import defaultdict
import json

# colours = (
#     ('Asturias', 'Oviedo'),
#     ('Galicia', 'Ourense'),
#     ('Extremadura', 'Cáceres'),
#     ('Galicia', 'Pontevedra'),
#     ('Asturias', 'Gijón'),
#     ('Cataluña', 'Barcelona'),
# )

# # defaultdict
# ciudades = defaultdict(list)

# for name, colour in colours:
#     ciudades[name].append(colour)

# print(ciudades)

tree = lambda: defaultdict(tree)
some_dict = tree()
some_dict['region']['ciudad'] = "Oviedo"

print(json.dumps(some_dict))