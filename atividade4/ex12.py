
animal1 = {'nome': 'Max', 'tipo': 'Cachorro', 'dono': 'Maria'}
animal2 = {'nome': 'Mittens', 'tipo': 'Gato', 'dono': 'João'}
animal3 = {'nome': 'Bella', 'tipo': 'Cachorro', 'dono': 'Ana'}
animal4 = {'nome': 'Whiskers', 'tipo': 'Coelho', 'dono': 'Pedro'}


pets = [animal1, animal2, animal3, animal4]


for pet in pets:
    print(f"Nome: {pet['nome']}")
    print(f"Tipo: {pet['tipo']}")
    print(f"Dono: {pet['dono']}")
    print() 

