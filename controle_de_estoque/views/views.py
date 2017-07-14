from controle_de_estoque.exceptions.exceptions import ProdutoNaoEncontradoError, ConfirmaError, MenorQueZeroError
from controle_de_estoque.models.entities import Produto


class Principal(object):

    def menu(self):
        print("XYZ COMERCIO DE PRODUTOS LTDA.")
        print("SISTEMA DE CONTROLE DE ESTOQUE", end="\n\n")
        print("MENU PRINCIPAL")
        print("1 - CADASTRO DE PRODUTOS")
        print("2 - MOVIMENTAÇÃO")
        print("3 - REAJUSTE DE PREÇOS")
        print("4 - RELATÓRIOS")
        print("0 - FINALIZA", end="\n\n")

        return input("OPÇÂO: ")

    def consultar(self):
        print("XYZ COMERCIO DE PRODUTOS LTDA.")
        print("SISTEMA DE CONTROLE DE ESTOQUE", end="\n\n")
        print("CONSULTA DE PRODUTOS")

        nome_do_produto = input("NOME DO PRODUTO: ")

        return nome_do_produto

    def resultado_da_consulta(self, produto):
        print("XYZ COMERCIO DE PRODUTOS LTDA.")
        print("SISTEMA DE CONTROLE DE ESTOQUE", end="\n\n")
        print("CONSULTA DE PRODUTOS")

        if not produto:
            raise ProdutoNaoEncontradoError("PRODUTO NÃO ENCONTRADO")

        self._exibir(produto)

    def _confirmar(self, texto_da_pergunta):
        opcao = input(texto_da_pergunta)

        if opcao.upper() == "S":
            return True
        elif opcao.upper() == "N":
            return False
        else:
            print("ERRO: OPÇÔES VALIDAS - S s N n", end="\n\n")
            self._confirmar(texto_da_pergunta)

    def _exibir(self, produto):
        print("CÓDIGO:", produto.codigo)
        print("NOME:", produto.nome)
        print("PREÇO: R${:.2f}".format(float(produto.preco)))
        print("UNIDADE:", produto.unidade)
        print("QUANTIDADE:", produto.quantidade)


class Cadastro(Principal):

    def menu(self):
        print("XYZ COMERCIO DE PRODUTOS LTDA.")
        print("SISTEMA DE CONTROLE DE ESTOQUE", end="\n\n")
        print("CADASTRO DE PRODUTOS")
        print("1 - INCLUSÃO")
        print("2 - ALTERAÇÃO")
        print("3 - EXCLUSÃO")
        print("4 - CONSULTA")
        print("0 - RETORNA", end="\n\n")

        return input("OPÇÂO: ")

    def inserir(self):
        produto = Produto()

        print("XYZ COMERCIO DE PRODUTOS LTDA.")
        print("SISTEMA DE CONTROLE DE ESTOQUE", end="\n\n")
        print("INCLUSÃO DE PRODUTOS")
        produto.nome = input("NOME: ")
        produto.preco = input("PREÇO: ")
        produto.unidade = input("UNIDADE: ")
        produto.quantidade = input("QUANTIDADE: ")

        confirma = self._confirmar("CONFIRMA INCLUSÃO (S/N)? ")
        if not confirma:
            raise ConfirmaError("INCLUSÃO CANCELADA PELO USUÁRIO")

        print("INCLUSÂO CONCLUIDA COM SUCESSO")
        return produto

    def alterar(self, produto):
        novo_produto = Produto()

        print("XYZ COMERCIO DE PRODUTOS LTDA.")
        print("SISTEMA DE CONTROLE DE ESTOQUE", end="\n\n")
        print("ALTERAÇÂO DE PRODUTOS")
        self._exibir(produto)
        novo_produto.codigo = produto.codigo
        novo_produto.nome = input("NOME: ")
        novo_produto.preco = input("PREÇO: ")
        novo_produto.unidade = input("UNIDADE: ")
        novo_produto.quantidade = input("QUANTIDADE: ")

        confirma = self._confirmar("CONFIRMA ALTERAÇÂO (S/N)? ")
        if not confirma:
            raise ConfirmaError("ALTERAÇÃO CANCELADA PELO USUÁRIO")

        print("ALTERAÇÃO CONCLUIDA COM SUCESSO")
        return novo_produto

    def excluir(self, produto):
        print("XYZ COMERCIO DE PRODUTOS LTDA.")
        print("SISTEMA DE CONTROLE DE ESTOQUE", end="\n\n")
        print("EXCLUSÂO DE PRODUTOS")
        self._exibir(produto)

        confirma = self._confirmar("CONFIRMA EXCLUSÃO (S/N)? ")
        if not confirma:
            raise ConfirmaError("EXCLUSÃO CANCELADA PELO USUÁRIO")

        print("EXCLUSÃO CONCLUIDA COM SUCESSO")
        return produto


class Movimentacao(Principal):

    def menu(self):
        print("XYZ COMERCIO DE PRODUTOS LTDA.")
        print("SISTEMA DE CONTROLE DE ESTOQUE", end="\n\n")
        print("MOVIMENTAÇÂO DE PRODUTOS")
        print("1 - ENTRADA")
        print("2 - SAÍDA")
        print("0 - RETORNA", end="\n\n")

        return input("OPÇÂO: ")

    def adicionar_quantidade(self, produto):
        print("XYZ COMERCIO DE PRODUTOS LTDA.")
        print("SISTEMA DE CONTROLE DE ESTOQUE", end="\n\n")
        print("ENTRADA DE PRODUTOS")
        self._exibir(produto)

        valor = int(input("ADICIONAR A QUANTIDADE: "))
        produto.quantidade = int(produto.quantidade) + valor
        print("QUANTIDADE FINAL:", produto.quantidade)

        confirma = self._confirmar("CONFIRMA ENTRADA (S/N)? ")
        if not confirma:
            raise ConfirmaError("ENTRADA CANCELADA PELO USUÁRIO")

        print("NOVA ENTRADA CONCLUIDA COM SUCESSO")
        return produto

    def subtrair_quantidade(self, produto):
        print("XYZ COMERCIO DE PRODUTOS LTDA.")
        print("SISTEMA DE CONTROLE DE ESTOQUE", end="\n\n")
        print("SAÍDA DE PRODUTOS")
        self._exibir(produto)

        valor = int(input("SUBTRAIR A QUANTIDADE: "))
        self._validar_quantidade(produto, valor)
        print("QUANTIDADE FINAL:", produto.quantidade)

        confirma = self._confirmar("CONFIRMA SAÍDA (S/N)? ")
        if not confirma:
            raise ConfirmaError("SAÍDA CANCELADA PELO USUÁRIO")

        print("NOVA SAíDA CONCLUIDA COM SUCESSO")
        return produto

    def _validar_quantidade(self, produto, valor):
        if int(valor) > int(produto.quantidade):
            raise MenorQueZeroError("A QUANTIDADE DE UM PRODUTO NÃO PODE SER MENOR QUE ZERO")
        else:
            produto.quantidade = int(produto.quantidade) - int(valor)


class ReajusteDePreco(Principal):

    def menu(self):
        print("XYZ COMERCIO DE PRODUTOS LTDA.")
        print("SISTEMA DE CONTROLE DE ESTOQUE", end="\n\n")
        print("REAJUSTE DE PREÇOS")
        print("1 - REAJUSTE")
        print("0 - RETORNA", end="\n\n")

        return input("OPÇÂO: ")

    def reajustar_preco(self, produto):
        print("XYZ COMERCIO DE PRODUTOS LTDA.")
        print("SISTEMA DE CONTROLE DE ESTOQUE", end="\n\n")
        print("REAJUSTE DE PREÇO")
        self._exibir(produto)

        valor = float(input("NOVO PREÇO: "))
        self._validar_preco(produto, valor)
        print("PREÇO FINAL: R${:.2f}".format(float(produto.preco)))

        confirma = self._confirmar("CONFIRMA SAÍDA (S/N)? ")
        if not confirma:
            raise ConfirmaError("REAJUSTE CANCELADO PELO USUÁRIO")

        print("REAJUSTE CONCLUIDO COM SUCESSO")
        return produto

    def _validar_preco(self, produto, valor):
        if float(valor) < 0:
            raise MenorQueZeroError("O VALOR DO PRODUTO NÂO PODE SER MENOR QUE ZERO")
        else:
            produto.preco = valor


class Relatorios(Principal):
    def menu(self):
        print("XYZ COMERCIO DE PRODUTOS LTDA.")
        print("SISTEMA DE CONTROLE DE ESTOQUE", end="\n\n")
        print("RELATÒRIOS")
        print("1 - LISTA DE PREÇOS")
        print("2 - BALANÇO FÍSICO/FINÂNCEIRO")
        print("0 - RETORNA", end="\n\n")

        return input("OPÇÂO: ")

    def lista_de_precos(self, produtos):
        print("XYZ COMERCIO DE PRODUTOS LTDA.")
        print("SISTEMA DE CONTROLE DE ESTOQUE", end="\n\n")
        print("LISTA DE PREÇOS")
        print("+----------+----------------------------+------------+------------+")
        print("|  Código  |         Produto            | Preço - R$ |   Unidade  |")
        print("+----------+----------------------------+------------+------------+")

        for produto in produtos:
            print("|{:^10d}|{:^28s}|{:^12.2f}|{:^12s}|".format(int(produto.codigo),
                                                               self._formata_string(produto.nome, 24),
                                                               float(produto.preco), produto.unidade))
        print("+----------+----------------------------+------------+------------+")

    def balanco(self, produtos):
        print("XYZ COMERCIO DE PRODUTOS LTDA.")
        print("SISTEMA DE CONTROLE DE ESTOQUE", end="\n\n")
        print("BALANÇO FÍSICO/FINÂNCEIRO", )
        print("+----------+----------------------------+------------+------------------+")
        print("|  Código  |         Produto            | Quantidade | Valor Total - R$ |")
        print("+----------+----------------------------+------------+------------------+")

        for produto in produtos:
            print("|{:^10d}|{:^28s}|{:^12d}|{:^18.2f}|".format(int(produto.codigo),
                                                               self._formata_string(produto.nome, 24),
                                                               int(produto.quantidade), produto.get_valor_total()))
        print("+----------+----------------------------+------------+------------------+")
        print("                                        | ESTOQUE EM R$:{:^16.2f}|".format(
            self._get_valor_total_estoque(produtos)))
        print("                                        +-------------------------------+")

    # TODO pensar em um jeito de tirar esse numero magico
    # formata a string justificado a esquerda com o tamanho passado como argumento
    def _formata_string(self, valor, tamanho):
        valor = str(valor)

        if len(valor) > tamanho:
            valor = valor[0:tamanho - 3] + "..."

        return valor.ljust(tamanho)

    def _get_valor_total_estoque(self, produtos):
        valor_total = 0

        for produto in produtos:
            valor_total += produto.get_valor_total()

        return valor_total
