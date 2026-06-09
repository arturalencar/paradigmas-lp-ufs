"""
Atividade 5 - le2

let var x = 3 in
  let var x = x + 1 in
    let var y = x in
      x + y

Rastreamento (declaracao COLATERAL):
  Escopo 1: x = 3
  Escopo 2: x = x_externo + 1 = 3 + 1 = 4
            (colateral: a expressao "x+1" é avaliada ANTES de x ser redeclarado,
             portanto usa x=3 do escopo externo)
  Escopo 3: y = x = 4   (usa x=4 do escopo 2)
  Corpo:    x + y = 4 + 4 = 8

Resultado esperado: 8
"""

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
    # Bloco mais interno: let var y = x in x + y
    corpo_mais_interno = ExpSoma(Id("x"), Id("y"))
    decs3 = [DecVariavel(Id("y"), Id("x"))]
    let3 = ExpDeclaracao(decs3, corpo_mais_interno)

    # Bloco do meio: let var x = x + 1 in <let3>
    # A expressao "x + 1" e avaliada no ambiente ANTES de x ser redeclarado (colateral)
    decs2 = [DecVariavel(Id("x"), ExpSoma(Id("x"), ValorInteiro(1)))]
    let2 = ExpDeclaracao(decs2, let3)

    # Bloco externo: let var x = 3 in <let2>
    decs1 = [DecVariavel(Id("x"), ValorInteiro(3))]
    let1 = ExpDeclaracao(decs1, let2)

    prog = Programa(let1)

    executar("let var x = 3 in let var x = x+1 in let var y = x in x + y", prog)

    print("--------------------------------------------------")


if __name__ == "__main__":
    main()
