"""
Atividade 1 - lf1

Avalia a expressão:
  let fun f x = x + 1 in f(2)

Árvore:
  ExpDeclaracao
    DecFuncao: fun f [x] = ExpSoma(Id("x"), ValorInteiro(1))
    corpo:     Aplicacao( Id("f"), [ValorInteiro(2)] )

Rastreamento:
  - Declara f com parâmetro x e corpo x+1
  - Aplica f(2): cria escopo com x=2, avalia x+1 = 3

Resultado esperado: 3
"""

from Programa import Programa
from declaration.dec_funcao import DecFuncao
from expression.exp_declaracao import ExpDeclaracao
from expression.aplicacao import Aplicacao
from util.valor_funcao import ValorFuncao
from expression.exp_soma import ExpSoma
from expression.id import Id
from expression.valor_inteiro import ValorInteiro


def executar(descricao: str, prog: Programa) -> None:
    print("--------------------------------------------------")
    print("Expressao : " + descricao)
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
    # ValorFuncao: parametros e corpo de f
    params = [Id("x")]
    corpo = ExpSoma(Id("x"), ValorInteiro(1))
    vf = ValorFuncao(params, corpo)

    # DecFuncao: fun f x = x + 1
    dec_f = DecFuncao(Id("f"), vf)

    # Corpo do let: f(2)
    arg_f = [ValorInteiro(2)]
    chamada_f = Aplicacao(Id("f"), arg_f)

    # Bloco: let fun f x = x+1 in f(2)
    decs = [dec_f]
    let = ExpDeclaracao(decs, chamada_f)

    # Instancia e executa o programa funcional
    prog = Programa(let)

    executar("let fun f x = x + 1 in f(2)", prog)


if __name__ == "__main__":
    main()
