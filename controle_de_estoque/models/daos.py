import csv

from controle_de_estoque.exceptions.exceptions import ProdutoNaoEncontradoError
from controle_de_estoque.models.entities import Produto


class ProdutoDAO(object):

    def inserir(self, produto):
        raise NotImplementedError()

    def alterar(self, produto):
        raise NotImplementedError()

    def excluir(self, produto):
        raise NotImplementedError()

    def obter_lista(self):
        raise NotImplementedError()

    def consultar_por_nome(self, nome):
        raise NotImplementedError()


class ProdutoCsvDAO(ProdutoDAO):
    _caminho = "database/produtos.csv"

    def inserir(self, produto):
        produto.codigo = self._gerar_codigo()

        with open(self._caminho, "a") as arquivo:
            nome_dos_campos = ["codigo", "nome", "preco", "unidade", "quantidade"]
            escritor = csv.DictWriter(arquivo, nome_dos_campos)

            if produto.codigo == 1:
                escritor.writeheader()

            escritor.writerow({"codigo": produto.codigo, "nome": produto.nome, "preco": produto.preco,
                               "unidade": produto.unidade, "quantidade": produto.quantidade})

    def alterar(self, produto):
        lista = self.obter_lista()
        indice = self._obter_indice(produto.codigo)
        lista[indice] = produto

        self._persistir_lista(lista)

    def excluir(self, produto):
        lista = self.obter_lista()
        lista.remove(produto)

        self._persistir_lista(lista)

    def obter_lista(self):
        lista = []

        with open(self._caminho, "r") as arquivo:
            leitor = csv.DictReader(arquivo)

            for linha in leitor:
                produto = Produto(linha["codigo"], linha["nome"], linha["preco"], linha["unidade"], linha["quantidade"])
                lista.append(produto)

        return lista

    def consultar_por_nome(self, nome):
        with open(self._caminho, "r") as arquivo:
            leitor = csv.DictReader(arquivo)

            for linha in leitor:
                if linha["nome"] == nome:
                    produto = Produto(linha["codigo"], linha["nome"], linha["preco"], linha["unidade"],
                                      linha["quantidade"])
                    return produto

            raise ProdutoNaoEncontradoError("PRODUTO NÃO ENCONTRADO")

    def _obter_indice(self, codigo):
        lista = self.obter_lista()

        for produto in lista:
            if codigo == produto.codigo:
                return lista.index(produto)

        raise ProdutoNaoEncontradoError("PRODUTO NÃO ENCONTRADO")

    def _persistir_lista(self, lista):
        with open(self._caminho, "w") as arquivo:
            nome_dos_campos = ["codigo", "nome", "preco", "unidade", "quantidade"]
            escritor = csv.DictWriter(arquivo, nome_dos_campos)
            escritor.writeheader()

            for produto in lista:
                escritor.writerow({"codigo": produto.codigo, "nome": produto.nome, "preco": produto.preco,
                                   "unidade": produto.unidade, "quantidade": produto.quantidade})

    def _gerar_codigo(self):
        lista = self.obter_lista()

        if lista:
            return int(lista[-1].codigo) + 1

        return 1
