def e_primo(num):

  if num <= 1:
      return False

 
  if num == 2 or num == 3:
      return True
  if num % 2 == 0 or num% 3 == 0:
      return False

 
  i = 5
  while i * i <= num:
      if num % i == 0 or num % (i + 2) == 0:
          return False
      i += 6

  return True

def imprimir__primos(n):
 
  primo = []

 
  num = 2
  while len(primo) < n:
      if e_primo(num):
          primo.append(num)
      num += 1

 
  print(f"Os {n} primeiros números primos são:")
  print(primo)

def main():
  
  n = int(input("Digite a quantidade de números : "))

  
  imprimir__primos(n)

if __name__ == "__main__":
  main()

