from expression.valor_inteiro import ValorInteiro
from expression.exp_soma import ExpSoma
from expression.exp_sub import ExpSub
from Programa import Programa

class Exemplos1():
    
    @staticmethod
    def main():
        v4 = ValorInteiro(4)
        v12 = ValorInteiro(12)
        v3 = ValorInteiro(3)

        soma = ExpSoma(v4, v12)
        sub = ExpSub(soma, v3)

        programa = Programa(sub)
        print("Expressão: 4 + 12 - 3")
        print("Bem tipada: ", programa.checa_tipo())
        programa.executar()
    
if __name__ == "__main__":
    Exemplos1.main()



