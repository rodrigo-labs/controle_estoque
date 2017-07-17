import sys

from controle_de_estoque.exceptions.exceptions import ProdutoError
from controle_de_estoque.models.daos import ProdutoCsvDAO
from controle_de_estoque.views.views import Principal, Cadastro, Movimentacao, ReajusteDePreco, Relatorios


# todo refatorar esse modulo usando dicionario no lugar de if/else
def principal_controle():
    principal = Principal()

    while True:
        opcao = principal.menu()

        if opcao == '1':
            cadastro_controle()
        elif opcao == '2':
            movimentacao_controle()
        elif opcao == '3':
            reajuste_controle()
        elif opcao == '4':
            relatorios_controle()
        elif opcao == '0':
            sys.exit(0)
        else:
            print("OPÇÃO INVALIDA", end="\n\n")


def cadastro_controle():
    # todo criar um metodo que cria um produto e um outro que cria um cadastro(idea)
    cadastro = Cadastro()
    produto_dao = ProdutoCsvDAO()

    while True:
        opcao = cadastro.menu()

        if opcao == '1':
            try:
                produto = cadastro.inserir()
                produto_dao.inserir(produto)
            except ProdutoError as ex:
                print(ex.mensagem)
        elif opcao == '2':
            try:
                nome = cadastro.consultar()
                produto = produto_dao.consultar_por_nome(nome)

                produto_dao.alterar(cadastro.alterar(produto))
            except ProdutoError as ex:
                print(ex.mensagem)
        elif opcao == '3':
            try:
                nome = cadastro.consultar()
                produto = produto_dao.consultar_por_nome(nome)

                produto_dao.excluir(cadastro.excluir(produto))
            except ProdutoError as ex:
                print(ex.mensagem)
        elif opcao == '4':
            try:
                nome = cadastro.consultar()
                produto = produto_dao.consultar_por_nome(nome)

                cadastro.resultado_da_consulta(produto)
            except ProdutoError as ex:
                print(ex.mensagem)
        elif opcao == '0':
            return
        else:
            print("OPÇÃO INVALIDA", end="\n\n")


def movimentacao_controle():
    movimentacao = Movimentacao()
    produto_dao = ProdutoCsvDAO()

    while True:
        opcao = movimentacao.menu()

        if opcao == '1':
            try:
                nome = movimentacao.consultar()
                produto = produto_dao.consultar_por_nome(nome)
                movimentacao.adicionar_quantidade(produto)

                produto_dao.alterar(produto)
            except ProdutoError as ex:
                print(ex.mensagem)
        elif opcao == '2':
            try:
                nome = movimentacao.consultar()
                produto = produto_dao.consultar_por_nome(nome)
                movimentacao.subtrair_quantidade(produto)

                produto_dao.alterar(produto)
            except ProdutoError as ex:
                print(ex.mensagem)
        elif opcao == '0':
            return
        else:
            print("OPÇÃO INVALIDA", end="\n\n")


def reajuste_controle():
    reajuste = ReajusteDePreco()
    produto_dao = ProdutoCsvDAO()

    while True:
        opcao = reajuste.menu()

        if opcao == '1':
            try:
                nome = reajuste.consultar()
                produto = produto_dao.consultar_por_nome(nome)
                reajuste.reajustar_preco(produto)

                produto_dao.alterar(produto)
            except ProdutoError as ex:
                print(ex.mensagem)
        elif opcao == '0':
            return
        else:
            print("OPÇÃO INVALIDA", end="\n\n")


def relatorios_controle():
    relatorios = Relatorios()
    produto_dao = ProdutoCsvDAO()

    while True:
        opcao = relatorios.menu()

        if opcao == '1':
            relatorios.lista_de_precos(produto_dao.obter_lista())
        elif opcao == '2':
            relatorios.balanco(produto_dao.obter_lista())
        elif opcao == '0':
            return
        else:
            print("OPÇÃO INVALIDA", end="\n\n")
