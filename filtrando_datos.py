from list_and_dicts import clearConsole

DATA = [
    {
        'name': 'Alberto',
        'age': 35,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

def run():
    #all_python_devs=[worker['name'] for worker in DATA if worker['language']=='python']
    #all_python_workes =[worker['name'] for worker in DATA if worker['organization'] == 'Platzi']

    all_python_devs = list(filter(lambda worker:worker['language']=='python', DATA))
    all_python_devs = list(map(lambda worker:worker['name'], all_python_devs))

    all_python_workes = list(filter(lambda worker:worker['organization']=='Platzi', DATA))
    all_python_workes = list(map(lambda worker:worker['name'], all_python_workes))


    adult = list(filter(lambda worker:worker['age']>18, DATA))
    adult = list(map(lambda worker: worker['name'], adult))
    old_people = list(map(lambda worker: worker | {'old':worker['age']>70}, DATA))
    clearConsole()

    """ for worker in all_python_devs:
        print(worker) """

    for worker in all_python_workes:
        print(worker)

if __name__=='__main__':
    run()