from datetime import date


dates_list = [
    {"name":"alberto", "age": 39},
    {"name":"maria", "age": 25},
    {"name":"gissel", "age": 22}
]

dates_dict = {
    "name" : ['alberto', 'gissel', 'maria'],
    "cargos" : ['programer', 'reception', 'lawyer'],
    "salario" : ['$8.000.000', '$2.500.000', '$3.400.000'],
    "ciudad" : ['magangue', 'cartagena', 'caracas' ]
}


list_person = list(filter(lambda persona : persona, dates_list))
# print(list_person)

# list(map(lambda persona : print('Persona: ', persona['name'], persona['age']) if persona['age'] < 25 else 0, list_person ))


for key, value in dates_dict.items():
    list(map(lambda key : print(value[0]) if key == 'name' else 'none', dates_dict)) 
        

    


    
    
