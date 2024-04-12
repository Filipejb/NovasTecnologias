grid = [['10', '11','12'], ['13', '14', '15'],['16','17','18']]

for i, linha in enumerate(grid):
    for j ,colna in enumerate(grid[i]):
        print(grid[i][j], end=" ")
    print("")


venceu = False:


   while not venceu:

     jogada = input("ecolhs x ou O")
    linha = int(input("em qual linha"))
    coluna = int(input("em qual coluna"))

    grid[linha][coluna]= jogada

    for i, linha in enumerate(grid):
       for j ,colna in enumerate(grid[i]):
          print(grid[i][j], end=" ")
      print("")

    if(grid[0][0]==grid[1][1]=grid[2][2]):
        venceu = True
    for i in range(0, len(grid))
    
    
if venceu is True:
            print("""
                     voce ganhou
        """)
