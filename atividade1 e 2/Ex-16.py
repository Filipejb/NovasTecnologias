def fibonacci(n):
  if n <= 0:
      return "Número inválido"
  elif n == 1 or n == 2:
      return 1

  
  termo_anterior = 1
  termo_atual = 1

  
  for _ in range(3, n + 1):
      proximo_termo = termo_anterior + termo_atual
      termo_anterior = termo_atual
      termo_atual = proximo_termo

  return termo_atual

def main():
  n = int(input("Digite o valor de n (n ≥ 3): "))
  resultado = fibonacci(n)
  print(f"O {n}-ésimo termo da série de Fibonacci é: {resultado}")

if __name__ == "__main__":
  main()


