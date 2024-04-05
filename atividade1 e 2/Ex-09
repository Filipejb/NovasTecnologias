def adicao():
  print("Tabuada de Adição:")
  for i in range(1, 11):
      for j in range(1, 11):
          print(f"{i} + {j} = {i + j}")
      print()

def subtracao():
  print("Tabuada de Subtração:")
  for i in range(1, 11):
      for j in range(1, 11):
          print(f"{i} - {j} = {i - j}")
      print()

def multiplicacao():
  print("Tabuada de Multiplicação:")
  for i in range(1, 11):
      for j in range(1, 11):
          print(f"{i} * {j} = {i * j}")
      print()

def divisao():
    print("Tabuada de Divisão:")
    for i in range(1, 11):
        for j in range(1, 11):
            if j != 0:
                resultado = i / j
                print(f"{i} / {j} = {resultado:.2f}")
            else:
                print(f"{i} / {j} = Indefinido")
        print()


def main():
  while True:
      print("\nEscolha uma operação:")
      print("1. Adição")
      print("2. Subtração")
      print("3. Multiplicação")
      print("4. Divisão")
      print("5. Sair")

      opcao = input("Digite o número da operação : ")

      if opcao == '1':
          adicao()
      elif opcao == '2':
          subtracao()
      elif opcao == '3':
          multiplicacao()
      elif opcao == '4':
          divisao()
      elif opcao == '5':
          print("Programa encerrado")
          break
      else:
          print("Opção inválida.")

if __name__ == "__main__":
  main()

