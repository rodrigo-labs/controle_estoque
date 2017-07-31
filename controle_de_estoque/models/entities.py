class Produto(object):

    def __init__(self, codigo=0, nome="", preco=0.0, unidade="", quantidade=0):
        self.__codigo = codigo
        self.__nome = nome
        self.__preco = preco
        self.__unidade = unidade
        self.__quantidade = quantidade

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, value):
        self.__codigo = value

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, value):
        self.__nome = value

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, value):
        self.__preco = value

    @property
    def unidade(self):
        return self.__unidade

    @unidade.setter
    def unidade(self, value):
        self.__unidade = value

    @property
    def quantidade(self):
        return self.__quantidade

    @quantidade.setter
    def quantidade(self, value):
        self.__quantidade = value

    @property
    def valor_total(self):
        return self.__quantidade * self.__preco

    def __str__(self) -> str:
        return "{},{},{},{},{}".format(self.codigo, self.nome, self.preco, self.unidade, self.quantidade)

    def __eq__(self, outro: object) -> bool:
        if isinstance(outro, self.__class__):
            return self.__dict__ == outro.__dict__
        return False

    def __ne__(self, outro: object) -> bool:
        return not self.__eq__(outro)
