def contar_caracteres(frase):
  
  contagem = {}

 
  for caractere in frase:
     
      if caractere in contagem:
         
          contagem[caractere] += 1
      else:
         
          contagem[caractere] = 1

  return contagem


frase = input("Insira uma frase: ")


resultado = contar_caracteres(frase)


print(resultado)

