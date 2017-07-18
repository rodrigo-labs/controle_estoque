class DAO(object):

    def inserir(self, objeto):
        raise NotImplementedError()

    def alterar(self, objeto):
        raise NotImplementedError()

    def excluir(self, objeto):
        raise NotImplementedError()

    def obter_lista(self):
        raise NotImplementedError()

    def consultar(self, valor):
        raise NotImplementedError()


class ProdutoDAO(DAO):

    def inserir(self, produto):
        pass

    def alterar(self, produto):
        pass

    def excluir(self, produto):
        pass

    def consultar(self, nome):
        pass

    def obter_lista(self):
        pass


class UnidadeDAO(DAO):

    def inserir(self, unidade):
        pass

    def alterar(self, unidade):
        pass

    def excluir(self, unidade):
        pass

    def consultar(self, codigo):
        pass

    def obter_lista(self):
        pass
