def main():

  num = input("Digite um número: ")


  if not num.isdigit():
      print("Por favor, insira um número válido.")
      return

  for d in num:
      print(d, end="   ")

if __name__ == "__main__":
  main()

