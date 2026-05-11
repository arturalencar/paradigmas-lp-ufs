from expression.exp_soma import ExpSoma
from expression.exp_sub import ExpSub
from expression.exp_menos import ExpMenos
from expression.exp_length import ExpLength
from expression.exp_and import ExpAnd
from expression.exp_concat import ExpConcat
from expression.valor_inteiro import ValorInteiro
from expression.valor_string import ValorString
from expression.valor_booleano import ValorBooleano
from Programa import Programa

class Exemplos:
    @staticmethod
    def executar(descricao: str, prog: Programa):
        """Método estático para padronizar a execução dos testes."""
        print("-" * 50)
        print(f"Expressão : {descricao}")

        # Chamada ao método de checagem definido na classe Programa
        bem_tipada = prog.checa_tipo()
        print(f"Bem tipada: {bem_tipada}")

        if bem_tipada:
            prog.executar()
        else:
            print("Erro de tipo: expressão mal tipada, avaliação abortada.")

    @staticmethod
    def main():
        # 1) -4 + 12 - 3
        exp1 = ExpSub(
            ExpSoma(ExpMenos(ValorInteiro(4)), ValorInteiro(12)),
            ValorInteiro(3)
        )
        Exemplos.executar("-4 + 12 - 3", Programa(exp1))

        # 2) length("abc") + 3
        exp2 = ExpSoma(ExpLength(ValorString("abc")), ValorInteiro(3))
        Exemplos.executar('length("abc") + 3', Programa(exp2))

        # 3) true and false
        exp3 = ExpAnd(ValorBooleano(True), ValorBooleano(False))
        Exemplos.executar("true and false", Programa(exp3))

        # 4) "curso" ++ " de " ++ " paradigmas"
        exp4 = ExpConcat(
            ExpConcat(ValorString("curso"), ValorString(" de ")),
            ValorString(" paradigmas")
        )
        Exemplos.executar('"curso" ++ " de " ++ " paradigmas"', Programa(exp4))

        # 5) 1 + true (Erro de tipo esperado)
        exp5 = ExpSoma(ValorInteiro(1), ValorBooleano(True))
        Exemplos.executar("1 + true", Programa(exp5))

        print("-" * 50)

if __name__ == '__main__':
    Exemplos.main()

    