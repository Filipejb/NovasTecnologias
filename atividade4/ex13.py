
sandwich_orders = []


while True:
    pedido = input("Digite o nome do sanduíche que deseja (ou '1' para encerrar): ")
    if pedido.lower() == '1':
        break
    else:
        sandwich_orders.append(pedido)


finished_sandwiches = []


for pedido in sandwich_orders:
    print(f"Preparei seu sanduíche de {pedido}.")

    
    finished_sandwiches.append(pedido)


print("\nTodos os sanduíches foram preparados!\n")


print("Sanduíches preparados:")
for sanduiche in finished_sandwiches:
    print(sanduiche)

