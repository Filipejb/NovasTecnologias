
agenda ={}
lisat_dados=["nome"," telefone", "email", "data de nscimento"]


while = 1:

    ope = int(input("""




                 agenda pessoal
                 1-salvar contato
                 2-alterar contato
                 3-buscar contato
                 4-listar contato
                 5-excluir contato
                 pressione 0 para sair
                 



     """))

    if ope == 1:
        
        contato = []
        contato.append(input("nome:"))
        contato.append( input("email:"))
        contato.appendinput(input("telefone:"))
        contato.appendinput(input("data de nascimento:"))
        agenda[nome]= contato,

        if nome == nome:
            pritn("nome ja adicionado")
        else:
        print("contato salvo com sucesso")
    elif ope == 2:
        print("alterar contato")
        nome = input("qual nome")
        print(agenda[nome])
        campo = input("qual dado")
        print(f"voce quer alterar{ agenda[nome][lista_dados.index(campo)]}?")
        novo_dado = input("qual nova informacao")
        agenda[nome][lista_dados.index(campo)]= novo_dado
        print(f"contato alterado {agenda[nome]}")
                     
        
    elif ope == 3:
        print("buscar contato")
        nome = input("qual contato:")
        print(agenda[nome])
    elif ope == 4:
        print("listar contato")
        for contato in agenda.values():
            print(contato)
    elif ope == 5:
        print("excluir contato")
        nome = input("qual contato")
        contato=agenda[nome]
       if contato == agenda.pop(nome)
        print("contato apagado")
    elif ope == 0:
        break
    else:
        print("opcao invalida")

