import math

def calcula_raiz(a, b, c):
   
    discriminante = b**2 - 4*a*c

 
    if discriminante > 0:
        raiz1 = (-b + math.sqrt(discriminante)) / (2*a)
        raiz2 = (-b - math.sqrt(discriminante)) / (2*a)
        return raiz1, raiz2
    elif discriminante == 0:
        raiz = -b / (2*a)
        return raiz, raiz
    else:
        parte_real = -b / (2*a)
        parte_imaginaria = math.sqrt(abs(discriminante)) / (2*a)
        raiz1 = complex(parte_real, parte_imaginaria)
        raiz2 = complex(parte_real, -parte_imaginaria)
        return raiz1, raiz2

def main():
  
    a = float(input("Digite o coeficiente 'a': "))
    b = float(input("Digite o coeficiente 'b': "))
    c = float(input("Digite o coeficiente 'c': "))

    
    raiz1, raiz2 = calcula_raiz(a, b, c)

   
    print("As raízes   são:")
    print("x' =", raiz1)
    print("x'' =", raiz2)

if __name__ == "__main__":
    main()

