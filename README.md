# Gerenciador de Agenda de Contatos

Este é um programa simples em Python que permite gerenciar uma lista de contatos. O programa oferece funcionalidades para adicionar, visualizar, editar, favoritar, visualizar favoritos e apagar contatos. Ele é executado em um loop contínuo até que o usuário escolha sair.

## Funcionalidades

O programa oferece as seguintes funcionalidades:

1. **Adicionar Contato**: Adiciona um novo contato à lista com nome, telefone e e-mail.
2. **Visualizar Contatos**: Exibe todos os contatos cadastrados, indicando quais estão favoritados.
3. **Editar Contato**: Permite editar as informações de um contato existente.
4. **Favoritar/Desfavoritar Contato**: Alterna o status de favorito de um contato.
5. **Visualizar Contatos Favoritos**: Exibe apenas os contatos marcados como favoritos.
6. **Apagar Contato**: Remove um contato da lista.
7. **Sair**: Encerra o programa.

## Como Usar

1. **Adicionar Contato**:
   - Escolha a opção `1` no menu.
   - Insira o nome, telefone e e-mail do contato.
   - O contato será adicionado à lista.

2. **Visualizar Contatos**:
   - Escolha a opção `2` no menu.
   - Todos os contatos serão exibidos, com um indicador `[✓]` para os favoritos.

3. **Editar Contato**:
   - Escolha a opção `3` no menu.
   - Insira o número do contato que deseja editar.
   - Forneça o novo nome, telefone e e-mail.

4. **Favoritar/Desfavoritar Contato**:
   - Escolha a opção `4` no menu.
   - Insira o número do contato que deseja favoritar ou desfavoritar.
   - O status do contato será alternado.

5. **Visualizar Contatos Favoritos**:
   - Escolha a opção `5` no menu.
   - Apenas os contatos favoritados serão exibidos.

6. **Apagar Contato**:
   - Escolha a opção `6` no menu.
   - Insira o número do contato que deseja apagar.
   - O contato será removido da lista.

7. **Sair**:
   - Escolha a opção `7` no menu.
   - O programa será encerrado.

## Estrutura do Código

O código é composto por funções que realizam as operações descritas acima. Abaixo está uma breve explicação de cada função:

- **`adicionar_contato(contatos, nome_contato, telefone_contato, email_contato)`**:
  - Adiciona um novo contato à lista de contatos.

- **`ver_contatos(contatos)`**:
  - Exibe todos os contatos cadastrados, com um indicador de favorito.

- **`atualiza_contato(contatos, indice_contato_ajustado, novo_nome, novo_telefone, novo_email)`**:
  - Atualiza as informações de um contato existente.

- **`favoritar_contato(contatos, indice_contato)`**:
  - Alterna o status de favorito de um contato.

- **`visualiar_contatos_favoritos(contatos)`**:
  - Exibe apenas os contatos favoritados.

- **`apagar_contato(contatos, indice_contato)`**:
  - Remove um contato da lista.
