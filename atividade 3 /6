lugares_vagos = [10, 2, 1, 3, 0]

def disponibilidade(sala, qtd_lugar):
    if sala < 1 or sala > len(lugares_vagos):
        print("Sala inválida.")
        return False
    elif lugares_vagos[sala - 1] >= qtd_lugar:
        lugares_vagos[sala - 1] -= qtd_lugar
        print(f"{qtd_lugar} lugar(es) vendido(s) na sala {sala}.")
        return True
    else:
        print(f"Não há lugares suficientes na sala {sala}.")
        return False

while True:
    sala = int(input("Digite o número da sala (ou 0 para sair): "))
    if sala == 0:
        break
    qtd_lugar = int(input("Digite a quantidade de lugares solicitados: "))
    disponibilidade(sala, qtd_lugar)

print("Programa encerrado.")

