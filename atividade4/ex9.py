def comparar_listas_versoes(lista_inicial, lista_modificada):
 
  inicial_set = set(lista_inicial)
  modificada_set = set(lista_modificada)

  
  nao_mudaram = inicial_set.intersection(modificada_set)

  
  novos = modificada_set.difference(inicial_set)

  
  removidos = inicial_set.difference(modificada_set)

  return nao_mudaram, novos, removidos


lista_inicial = [1, 2, 3, 4, 5]

lista_modificada = [2, 3, 6, 7]


nao_mudaram, novos, removidos = comparar_listas_versoes(lista_inicial, lista_modificada)


print("Elementos que não mudaram:", nao_mudaram)
print("Novos elementos:", novos)
print("Elementos removidos:", removidos)


