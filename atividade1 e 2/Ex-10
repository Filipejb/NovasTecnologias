def e_primo(num):
  
  if num <= 1:
      return False

  
  for i in range(2, int(num**0.5) + 1):
      if num % i == 0:
          return False

  return True

def main():
  
  num = int(input("Digite um número inteiro positivo: "))

 
  if e_primo(num):
      print(num, "é um número primo.")
  else:
      print(num, "não é um número primo.")

if __name__ == "__main__":
  main()

