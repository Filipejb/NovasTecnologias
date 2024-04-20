
first_name = input("Digite o primeiro nome: ")
last_name = input("Digite o sobrenome: ")
age = int(input("Digite a idade: "))
city = input("Digite a cidade: ")


pessoa = {
    'first_name': first_name,
    'last_name': last_name,
    'age': age,
    'city': city
}


print("Primeiro nome:", pessoa['first_name'])
print("Sobrenome:", pessoa['last_name'])
print("Idade:", pessoa['age'])
print("Cidade:", pessoa['city'])

