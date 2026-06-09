from exp_binaria import ExpBinaria
from valor_booleano import ValorBooleano
from util.tipo import Tipo


class ExpAnd(ExpBinaria):
    """
    Um objeto desta classe representa uma Expressao de Conjuncao logica (AND).
    """

    def __init__(self, esq, dir):
        # Passa as sub-expressões e o operador textual correspondente para a superclasse
        super().__init__(esq, dir, "and")

    def avaliar(self, amb):
        """
        Retorna o valor da Expressao de Conjuncao Logica avaliando as duas sub-expressões.
        """
        # Avalia a esquerda e a direita passando o ambiente de execução atual
        valor_esq = self.esq.avaliar(amb).valor
        valor_dir = self.dir.avaliar(amb).valor

        # Retorna uma nova instância de ValorBooleano com o resultado da conjunção
        return ValorBooleano(valor_esq and valor_dir)

    def _checa_tipo_elemento_terminal(self, ambiente) -> bool:
        """
        Realiza a verificacao de tipos para garantir que ambos os lados sejam booleanos.
        O prefixo '_' simula o método 'protected' do Java.
        """
        return self.esq.get_tipo(ambiente).e_booleano() and self.dir.get_tipo(ambiente).e_booleano()

    def get_tipo(self, ambiente) -> Tipo:
        """
        Retorna o tipo resultante desta expressão (sempre Booleano).
        """
        return Tipo.TIPO_BOOLEANO
