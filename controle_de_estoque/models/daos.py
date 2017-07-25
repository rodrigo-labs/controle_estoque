import sqlite3

from controle_de_estoque.exceptions.exceptions import ProdutoNaoEncontradoError
from controle_de_estoque.models.entities import Produto


class Conexao(object):
    _path = "database/controle_de_estoque.bd"

    def __init__(self) -> None:
        self._db = sqlite3.connect(self._path)

    def get_conexao(self):
        return self._db

    def __del__(self):
        self._db.close()


class DAO(object):
    def inserir(self, objeto):
        raise NotImplementedError()

    def alterar(self, objeto):
        raise NotImplementedError()

    def excluir(self, objeto):
        raise NotImplementedError()

    def consultar(self, valor):
        raise NotImplementedError()

    def listar(self):
        raise NotImplementedError()


class ProdutoDAO(DAO):
    _path = "database/controle_de_estoque.db"

    def inserir(self, produto):
        sql = """INSERT INTO produtos (nome, preco, unidade, quantidade) VALUES (?, ?, ?, ?)"""

        with sqlite3.connect(self._path) as conexao:
            cursor = conexao.cursor()
            cursor.execute(sql, (produto.nome, produto.preco, produto.unidade, produto.quantidade))

    def alterar(self, produto):
        sql = """UPDATE produtos SET nome = ?, preco = ?, unidade = ?, quantidade = ? WHERE id = ?"""

        with sqlite3.connect(self._path) as conexao:
            cursor = conexao.cursor()
            cursor.execute(sql, (produto.nome, produto.preco, produto.unidade, produto.quantidade, produto.codigo))

    def excluir(self, produto):
        sql = """DELETE FROM produtos WHERE id = ?"""

        with sqlite3.connect(self._path) as conexao:
            cursor = conexao.cursor()
            cursor.execute(sql, (produto.codigo,))

    def consultar(self, nome):
        sql = """SELECT * FROM produtos WHERE nome = ?"""

        with sqlite3.connect(self._path) as conexao:
            cursor = conexao.cursor()
            cursor.execute(sql, (nome,))
            linha = cursor.fetchone()

            if not linha:
                raise ProdutoNaoEncontradoError("PRODUTO NÃO ENCONTRADO")

            produto = self._fabrica_de_produto(linha)
            return produto

    def listar(self):
        sql = """SELECT * FROM produtos"""

        with sqlite3.connect(self._path) as conexao:
            cursor = conexao.cursor()
            cursor.execute(sql)
            linhas = cursor.fetchall()

            if not linhas:
                raise ProdutoNaoEncontradoError("NENHUM PRODUTO FOI ENCONTRADO")

            produtos = self._fabrica_de_produtos(linhas)
            return produtos

    def _fabrica_de_produto(self, linha):
        return Produto(*linha)

    def _fabrica_de_produtos(self, linhas):
        produtos = []

        for linha in linhas:
            produto = self._fabrica_de_produto(linha)
            produtos.append(produto)

        return produtos


class UnidadeDAO(DAO):
    def inserir(self, unidade):
        pass

    def alterar(self, unidade):
        pass

    def excluir(self, unidade):
        pass

    def consultar(self, codigo):
        pass

    def listar(self):
        pass
