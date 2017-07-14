class ProdutoError(Exception):
    def __init__(self, mensagem):
        self.mensagem = mensagem


class ProdutoNaoEncontradoError(ProdutoError):
    def __init__(self, mensagem):
        super().__init__(mensagem)


class ConfirmaError(ProdutoError):
    def __init__(self, mensagem):
        super().__init__(mensagem)


class MenorQueZeroError(ProdutoError):
    def __init__(self, mensagem):
        super().__init__(mensagem)
