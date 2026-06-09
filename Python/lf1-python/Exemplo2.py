"""
Avalia a expressao aninhada:

  let fun f x = x + 1 in
    let fun f y = y + x in
      let var x = 5 in
        f 1

Resultado esperado: f 1  =>  1 + 5 = 6
(f do nivel 2 usa y=1 e x=5 declarado no nivel 3)
"""

from Programa import Programa
from declaration.dec_funcao import DecFuncao
from declaration.dec_variavel import DecVariavel
from expression.exp_declaracao import ExpDeclaracao
from expression.aplicacao import Aplicacao
from util.valor_funcao import ValorFuncao
from expression.exp_soma import ExpSoma
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
    # Nivel 1: let fun f x = x + 1 in <nivel2>
    params1 = [Id("x")]
    corpof1 = ExpSoma(Id("x"), ValorInteiro(1))
    vf1 = ValorFuncao(params1, corpof1)
    decf1 = DecFuncao(Id("f"), vf1)

    # Nivel 2: let fun f y = y + x in <nivel3>
    params2 = [Id("y")]
    corpof2 = ExpSoma(Id("y"), Id("x"))
    vf2 = ValorFuncao(params2, corpof2)
    decf2 = DecFuncao(Id("f"), vf2)

    # Nivel 3: let var x = 5 in f 1
    dec_x = DecVariavel(Id("x"), ValorInteiro(5))
    aplicacao_f = Aplicacao(Id("f"), [ValorInteiro(1)])
    nivel3 = ExpDeclaracao([dec_x], aplicacao_f)

    # Monta nivel 2 com nivel 3 como corpo
    nivel2 = ExpDeclaracao([decf2], nivel3)

    # Monta nivel 1 com nivel 2 como corpo
    nivel1 = ExpDeclaracao([decf1], nivel2)

    # Executa o programa
    prog = Programa(nivel1)

    executar(
        "let fun f x = x + 1 in\n" +
        "  let fun f y = y + x in\n" +
        "    let var x = 5 in\n" +
        "      f 1",
        prog
    )


if __name__ == "__main__":
    main()
