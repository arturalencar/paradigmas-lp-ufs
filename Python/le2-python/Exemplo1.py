from Programa import Programa
from declaration.dec_variavel import DecVariavel
from expression.exp_declaracao import ExpDeclaracao
from expression.exp_soma import ExpSoma
from expression.id import Id
from expression.valor_inteiro import ValorInteiro


def executar(descricao: str, prog: Programa) -> None:
    print("--------------------------------------------------")
    print("Expressao : " + descricao)
    try:
        bem_tipada: bool = prog.checa_tipo()
        print("Bem tipada: " + str(bem_tipada).lower())
        if bem_tipada:
            print("Resultado: " + str(prog.executar()))
        else:
            print("Erro de tipo: avaliacao abortada.")
    except Exception as e:
        print("Excecao capturada: " + str(e))
        import traceback

        traceback.print_exc()

def main():
    # DecVariavel("x", 1)
    dec_x = DecVariavel(Id("x"), ValorInteiro(1))
    decs = [dec_x]

    # corpo: x + 1   |   let: let var x = 1 in corpo
    corpo = ExpSoma(Id("x"), ValorInteiro(1))
    let = ExpDeclaracao(decs, corpo)
    prog = Programa(let)

    executar("let var x = 1 in x + 1", prog)

    print("--------------------------------------------------")



if __name__ == "__main__":
    main()