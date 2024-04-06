def main():

  num = int(input("Digite um número de cinco dígitos: "))

  if not (10000 <= num <= 99999):
      print("Por favor, insira um número de cinco dígitos.")
      return


  digito_5 = num % 10
  digito_4 = (num // 10) % 10
  digito_3 = (num // 100) % 10
  digito_2 = (num // 1000) % 10
  digito_1 = (num // 10000) % 10


  print(digito_1, digito_2, digito_3, digito_4, digito_5)

if __name__ == "__main__":
  main()

