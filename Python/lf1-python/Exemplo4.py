"""
Avalia a expressao:

  let fun mult x y = if (x == 0) then (0) else (y + mult(x - 1, y)) in
    mult(3, 4)

Calculo:
  mult(3,4) = 4 + mult(2,4)
            = 4 + 4 + mult(1,4)
            = 4 + 4 + 4 + mult(0,4)
            = 4 + 4 + 4 + 0
Resultado esperado: 12
"""

from Programa import Programa
from declaration.dec_funcao import DecFuncao
from expression.exp_declaracao import ExpDeclaracao
from expression.aplicacao import Aplicacao
from expression.if_then_else import IfThenElse
from util.valor_funcao import ValorFuncao
from expression.exp_equals import ExpEquals
from expression.exp_soma import ExpSoma
from expression.exp_sub import ExpSub
from expression.id import Id
from expression.valor_inteiro import ValorInteiro


def executar(descricao: str, prog: Programa) -> None:
    print("--------------------------------------------------")
    print("Expressao :\n" + descricao)
    try:
        bem_tipada = prog.checa_tipo()
        print("Bem tipada: " + str(bem_tipada).lower())
        if bem_tipada:
            print("Resultado: " + str(prog.executar()))
        else:
            print("Erro de tipo: avaliacao abortada.")
    except Exception as e:
        print("Excecao capturada: " + str(e))
        import traceback
        traceback.print_exc()
    print("--------------------------------------------------")


def main():
    # Parametros formais de mult: x e y
    params = [Id("x"), Id("y")]

    # Corpo recursivo: y + mult(x - 1, y)
    args_rec = [ExpSub(Id("x"), ValorInteiro(1)), Id("y")]
    chamada_rec = Aplicacao(Id("mult"), args_rec)
    ramo_else = ExpSoma(Id("y"), chamada_rec)

    # Corpo completo de mult:
    #   if (x == 0) then (0) else (y + mult(x - 1, y))
    condicao = ExpEquals(Id("x"), ValorInteiro(0))
    ramo_then = ValorInteiro(0)
    corpo_mult = IfThenElse(condicao, ramo_then, ramo_else)

    # Declaracao: fun mult x y = <corpoMult>
    vf_mult = ValorFuncao(params, corpo_mult)
    dec_mult = DecFuncao(Id("mult"), vf_mult)

    # Corpo do let: mult(3, 4)
    args_main = [ValorInteiro(3), ValorInteiro(4)]
    aplicacao_mult = Aplicacao(Id("mult"), args_main)

    # Monta: let fun mult x y = ... in mult(3, 4)
    let_mult = ExpDeclaracao([dec_mult], aplicacao_mult)

    # Executa o programa
    prog = Programa(let_mult)

    executar(
        "let fun mult x y = if (x == 0) then (0) else (y + mult(x - 1, y)) in\n" +
        "  mult(3, 4)",
        prog
    )


if __name__ == "__main__":
    main()
