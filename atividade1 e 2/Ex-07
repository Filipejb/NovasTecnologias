def converte_segundo(segundo):

  dia = segundo // (24 * 3600)
  segundo_restante = segundo % (24 * 3600)
  hora = segundo_restante // 3600
  segundo_restante %= 3600
  minuto = segundo_restante // 60
  segundo_restante %= 60
  segundo = segundo_restante

  return dia, hora, minuto, segundo

def main():

  segundo = int(input("Digite a quantidade de segundos: "))


  dia, hora, minuto, segundo = converte_segundo(segundo)

  # Imprime o resultado
  print("Dias:", dia)
  print("Horas:", hora)
  print("Minutos:", minuto)
  print("Segundos:", segundo)

if __name__ == "__main__":
  main()


