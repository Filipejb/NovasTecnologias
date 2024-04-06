def calcula_digito_verificador(numero_conta):
 
  numero_conta_str = str(numero_conta)

 
  soma_digitos = sum(int(digito) for digito in numero_conta_str)

 
  resto_divisao = soma_digitos % 10


  digito_verificador = 10 - resto_divisao


  if digito_verificador == 10:
      digito_verificador = 0

  return digito_verificador

def main():

  numero_conta = input("Digite o número da conta (até 6 dígitos): ")

 
  if len(numero_conta) > 6 or not numero_conta.isdigit():
      print("Número de conta inválido.")
      return


  numero_conta = numero_conta.zfill(6)


  digito_verificador = calcula_digito_verificador(numero_conta)


  print(f"Número de conta completo: {numero_conta}-{digito_verificador}")

if __name__ == "__main__":
  main()

