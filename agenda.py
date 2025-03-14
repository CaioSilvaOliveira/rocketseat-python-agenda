def adicionar_contato(contatos, nome_contato, telefone_contato, email_contato):
    contato = {"nome": nome_contato, "telefone": telefone_contato, "email": email_contato, "favorito": False}
    contatos.append(contato)
    print(f"Contato {nome_contato} foi adicionado com sucesso!")
    return

def ver_contatos(contatos):
    print("\nLista de contatos:")
    for indice, contato in enumerate(contatos, start=1):
        status = "✓" if contato["favorito"] else " "
        nome_contato = contato["nome"]
        telefone_contato = contato["telefone"]
        email_contato = contato["email"]
        print(f"{indice}. [{status}] {nome_contato} | {telefone_contato} | {email_contato}")
    return

def atualiza_contato(contatos, indice_contato_ajustado, novo_nome, novo_telefone, novo_email):
    contatos[indice_contato_ajustado]["nome"] = novo_nome
    contatos[indice_contato_ajustado]["telefone"] = novo_telefone
    contatos[indice_contato_ajustado]["email"] = novo_email
    print(f"Contato {novo_nome} foi atualizado com sucesso!")
    return

def favoritar_contato(contatos, indice_contato):
    indice_contato_ajustado = int(indice_contato) - 1
    if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
        contatos[indice_contato_ajustado]["favorito"] = not contatos[indice_contato_ajustado]["favorito"]
        status = "favoritado" if contatos[indice_contato_ajustado]["favorito"] else "desfavoritado"
        print(f"Contato {contatos[indice_contato_ajustado]['nome']} foi {status} com sucesso!")
    else:
        print("Contato não encontrado!")
    return

def visualiar_contatos_favoritos(contatos):
    print("\nLista de contatos favoritos:")
    for indice, contato in enumerate(contatos, start=1):
        if contato["favorito"]:
            status = "✓" if contato["favorito"] else " "
            nome_contato = contato["nome"]
            telefone_contato = contato["telefone"]
            email_contato = contato["email"]
            print(f"{indice}. [{status}] {nome_contato} | {telefone_contato} | {email_contato}")
    return

def apagar_contato(contatos, indice_contato):
    indice_contato_ajustado = int(indice_contato) - 1
    if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
        contatos.pop(indice_contato_ajustado)
        print("Contato foi apagado com sucesso!")
    else:
        print("Contato não encontrado!")
    return



contatos = []
while True:
    print("\nMenu do Gerenciador da Agenda:")
    print("1. Adicionar contato")
    print("2. Visualizar a lista de contatos")
    print("3. Editar um contato")
    print("4. Favoritar/Desfavoritar um contato")
    print("5. Visualizar contatos favoritos")
    print("6. Apagar um contato")
    print ("7. Sair")

    escolha = input ("Digite a sua escolha: ")

    if escolha == "1":
        nome_contato = input("Digite o nome do contato que deseja adicionar: ")
        telefone_contato = input("Digite o telefone do contato que deseja adicionar: ")
        email_contato = input("Digite o email do contato que deseja adicionar: ")
        adicionar_contato(contatos, nome_contato, telefone_contato, email_contato)
    
    elif escolha == "2":
        ver_contatos(contatos)

    elif escolha == "3":
        indice_contato = input("Digite o número do contato que deseja editar: ")
        indice_contato_ajustado = int(indice_contato) - 1
        if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
            novo_nome = input("Digite o novo nome do contato: ")
            novo_telefone = input("Digite o novo telefone do contato: ")
            novo_email = input("Digite o novo email do contato: ")
            atualiza_contato(contatos, indice_contato_ajustado, novo_nome, novo_telefone, novo_email)
        else:
            print("Contato não encontrado!")

    elif escolha == "4":
        indice_contato = input("Digite o número do contato que deseja favoritar/desfavoritar: ")
        favoritar_contato(contatos, indice_contato)

    elif escolha == "5":
        visualiar_contatos_favoritos(contatos)

    elif escolha == "6":
        indice_contato = input("Digite o número do contato que deseja apagar: ")
        apagar_contato(contatos, indice_contato)

    elif escolha == "7":
        break
        
    print("Programa finalizado")