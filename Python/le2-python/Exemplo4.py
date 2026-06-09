"""
Atividade 4 - le2

let var x = 3 in
  let var y = x + 1 in
    let var x = 5 in
      y

Rastreamento:
  Escopo 1: x = 3
  Escopo 2: y = x + 1 = 4   (usa x=3)
  Escopo 3: x = 5            (shadowing, mas nao usado)
  Corpo:    y = 4            (y veio do escopo 2)

Resultado esperado: 4
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
    # Bloco mais interno: let var x = 5 in y
    decs3 = [DecVariavel(Id("x"), ValorInteiro(5))]
    let3 = ExpDeclaracao(decs3, Id("y"))

    # Bloco do meio: let var y = x + 1 in <let3>
    decs2 = [DecVariavel(Id("y"), ExpSoma(Id("x"), ValorInteiro(1)))]
    let2 = ExpDeclaracao(decs2, let3)

    # Bloco externo: let var x = 3 in <let2>
    decs1 = [DecVariavel(Id("x"), ValorInteiro(3))]
    let1 = ExpDeclaracao(decs1, let2)

    prog = Programa(let1)

    executar("let var x = 3 in let var y = x+1 in let var x = 5 in y", prog)

    print("--------------------------------------------------")


if __name__ == "__main__":
    main()
