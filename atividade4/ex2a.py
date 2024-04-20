def valores_comuns(lista1, lista2):
 
  conjunto1 = set(lista1)
  conjunto2 = set(lista2)


  comuns = conjunto1.intersection(conjunto2)

  return comuns


lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]


valores_comuns = valores_comuns(lista1, lista2)


print("Valores comuns às duas listas:", valores_comuns)

