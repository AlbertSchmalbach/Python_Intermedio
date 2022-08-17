# dir()

mi_lista = [1, 2, 3]
dir(mi_lista)
# Salida: ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__',
# '__delslice__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
# '__getitem__', '__getslice__', '__gt__', '__hash__', '__iadd__', '__imul__',
# '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__',
# '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__',
# '__setattr__', '__setitem__', '__setslice__', '__sizeof__', '__str__',
# '__subclasshook__', 'append', 'count', 'extend', 'index', 'insert', 'pop',
# 'remove', 'reverse', 'sort']

# type e id

print(type(''))
# Salida: <type 'str'>

print(type([]))
# Salida: <type 'list'>

print(type({}))
# Salida: <type 'dict'>

print(type(dict))
# Salida: <type 'type'>

print(type(3))
# Salida: <type 'int'>

nombre = "Pelayo"
print(id(nombre))
# Salida: 139972439030304

# Módulo inspect
import inspect
# print(inspect.getmembers(str))
# Salida: [('__add__', <slot wrapper '__add__' of ... ...