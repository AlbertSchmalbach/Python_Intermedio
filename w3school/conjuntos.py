frutas = {'mango', 'piña', 'pera', 'manzana', 'mora'}
otras = {'maracuya', 'sandia'}


# add()

frutas.add('naranja')

# añadir mas de uno - update()

frutas.update(otras)


# remove() - discard()

frutas.discard('pera')

# union()
set3 = frutas.union(otras)

print(set3)
for fruta in frutas:
    print(fruta, '\n')
    
#intersection_update

a = {1,7, 9,15, 12}
b = {4, 7, 1 , 12, 18}

#a.intersection_update(b)

#intersection() une los conjuntos y elimina duplicados
#a.intersection(b)

#El symmetric_difference_update()método mantendrá solo los elementos que NO están presentes en ambos conjuntos

a.symmetric_difference_update(b)

print(a)
    
    
    
