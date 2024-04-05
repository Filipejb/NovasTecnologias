def calcula_fatoria(n):

  if n < 0:
      return "Número inválido"

  
  if n == 0:
      return 1

  # Calcula o fatorial
  fatorial = 1
  for i in range(1, n + 1):
      fatorial *= i
  return fatorial

def main():
  
  try:
      num = int(input("Digite um número inteiro  : "))
  except ValueError:
      print("Número não inteiro")
      return

  
  result = calcula_fatoria(num)
  print(f"O fatorial de {num} é: {result}")

if __name__ == "__main__":
  main()

