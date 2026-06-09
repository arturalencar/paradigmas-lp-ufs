"""
Avalia a expressao aninhada:

  let var y = 3 in
    let fun f x = x + y in
      let var z = 'abc' in
        f 3

Resultado esperado: f 3  =>  x + y = 3 + 3 = 6
(z = 'abc' e declarada mas nao e usada na aplicacao f 3)
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
from expression.valor_string import ValorString


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
    # Nivel 1: let var y = 3 in <nivel2>
    dec_y = DecVariavel(Id("y"), ValorInteiro(3))

    # Nivel 2: let fun f x = x + y in <nivel3>
    params = [Id("x")]
    corpof = ExpSoma(Id("x"), Id("y"))
    vf = ValorFuncao(params, corpof)
    decf = DecFuncao(Id("f"), vf)

    # Nivel 3: let var z = 'abc' in f 3
    dec_z = DecVariavel(Id("z"), ValorString("abc"))
    aplicacao_f = Aplicacao(Id("f"), [ValorInteiro(3)])
    nivel3 = ExpDeclaracao([dec_z], aplicacao_f)

    # Monta nivel 2 com nivel 3 como corpo
    nivel2 = ExpDeclaracao([decf], nivel3)

    # Monta nivel 1 com nivel 2 como corpo
    nivel1 = ExpDeclaracao([dec_y], nivel2)

    # Executa o programa
    prog = Programa(nivel1)

    executar(
        "let var y = 3 in\n" +
        "  let fun f x = x + y in\n" +
        "    let var z = 'abc' in\n" +
        "      f 3",
        prog
    )


if __name__ == "__main__":
    main()
