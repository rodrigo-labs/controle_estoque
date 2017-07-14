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


class ProdutoTxtDAO(ProdutoDAO):
    _caminho = "database/produtos.txt"

    def inserir(self, produto):
        produto.codigo = self._gerar_codigo()

        with open(self._caminho, "a") as arquivo:
            arquivo.write(str(produto) + "\n")

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
        with open(self._caminho, "r") as arquivo:
            lista = []

            for linha in arquivo:
                colunas = linha.split(",")
                lista.append(Produto(*colunas))  # o '*colunas' é uma lista de parametros

        return lista

    def consultar_por_nome(self, nome):
        lista = self.obter_lista()

        for produto in lista:
            if nome == produto.nome:
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
            for produto in lista:
                produto_str = str(produto).strip()
                arquivo.write(produto_str + "\n")

    def _gerar_codigo(self):
        lista = self.obter_lista()

        if lista:
            return int(lista[-1].codigo) + 1

        return 1
