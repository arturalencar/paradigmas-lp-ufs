from exp_binaria import ExpBinaria
from valor_booleano import ValorBooleano
from util.tipo import Tipo


class ExpEquals(ExpBinaria):

    def __init__(self, esq, dir):
        # Passa as sub-expressões e o operador conceitual para a classe pai
        super().__init__(esq, dir, "==")

    def avaliar(self, amb):
        # Avalia a sub-expressão da esquerda e a da direita no ambiente atual
        valor_concreto_esq = self.esq.avaliar(amb)
        valor_concreto_dir = self.dir.avaliar(amb)

        # Assume-se que as instâncias de ValorConcreto possuem o método is_equals (ou correspondente)
        resultado_igualdade = valor_concreto_esq.is_equals(valor_concreto_dir)

        return ValorBooleano(resultado_igualdade)

    def _checa_tipo_elemento_terminal(self, ambiente) -> bool:
        tipo_esq = self.esq.get_tipo(ambiente)
        tipo_dir = self.dir.get_tipo(ambiente)

        # O operador 'not' inverte o booleano retornado por e_void()
        return not tipo_esq.intersecao(tipo_dir).e_void()

    def get_tipo(self, ambiente) -> Tipo:
        return Tipo.TIPO_BOOLEANO
