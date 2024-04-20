def comparar_listas(lista1, lista2):
  
  conjunto1 = set(lista1)
  conjunto2 = set(lista2)

  
  comuns = conjunto1.intersection(conjunto2)
  print("Valores comuns às duas listas:", comuns)

  
  apenas_na_lista1 = conjunto1.difference(conjunto2)
  print("Valores que só existem na primeira lista:", apenas_na_lista1)

 
  apenas_na_lista2 = conjunto2.difference(conjunto1)
  print("Valores que só existem na segunda lista:", apenas_na_lista2)

 
  uniao = conjunto1.union(conjunto2)
  print("Lista com elementos não repetidos das duas listas:", list(uniao))

 
  lista_sem_repetidos_na_segunda = conjunto1.difference(comuns)
  print("Primeira lista sem os elementos repetidos na segunda:", list(lista_sem_repetidos_na_segunda))


lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]


comparar_listas(lista1, lista2)
