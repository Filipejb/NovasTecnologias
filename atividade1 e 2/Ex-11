def e_primo(num):
  
  if num <= 1:
      return False

 
  if num == 2 or num == 3:
      return True
  if num % 2 == 0 or num % 3 == 0:
      return False

  
  i = 5
  while i * i <= num:
      if num % i == 0 or num % (i + 2) == 0:
          return False
      i += 6

  return True

def main():
  
  num = int(input("Digite um número inteiro positivo: "))

 
  if e_primo(num):
      print(num, "é um número primo.")
  else:
      print(num, "não é um número primo.")

if __name__ == "__main__":
  main()

