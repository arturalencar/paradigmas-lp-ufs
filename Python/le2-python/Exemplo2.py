"""
Atividade - Linguagem de Expressão 2 (le2)

Avalia a expressão:
  let var x = 1 in
      let var x = 2 in x + 1

Árvore de expressão:

        ExpDeclaracao (externa)
       /                      \\
  DecVariavel              ExpDeclaracao (interna)
  (x = 1)                 /                     \\
                     DecVariavel              ExpSoma
                     (x = 2)                 /        \\
                                          Id(x)    ValorInteiro(1)

Observação: o x interno (= 2) sombreia o x externo (= 1).
            Logo, a soma x + 1 calcula 2 + 1.

Resultado esperado: 3
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
    # --- Escopo externo: var x = 1 ---
    x_externo = Id("x")
    v1 = ValorInteiro(1)
    dec_x_externo = DecVariavel(x_externo, v1)

    declaracoes_externas = [dec_x_externo]

    # --- Escopo interno: var x = 2 ---
    x_interno = Id("x")
    v2 = ValorInteiro(2)
    dec_x_interno = DecVariavel(x_interno, v2)

    declaracoes_internas = [dec_x_interno]

    # --- Corpo do escopo interno: x + 1  (soma) ---
    # O x resolvido aqui será o do escopo interno, cujo valor é 2.
    soma = ExpSoma(Id("x"), ValorInteiro(1))

    # --- ExpDeclaracao interna: let var x = 2 in x + 1 ---
    exp_interna = ExpDeclaracao(declaracoes_internas, soma)

    # --- ExpDeclaracao externa: let var x = 1 in <exp_interna> ---
    exp_externa = ExpDeclaracao(declaracoes_externas, exp_interna)

    # Programa é a expressão raiz
    programa = Programa(exp_externa)

    executar("let var x = 1 in let var x = 2 in x + 1", programa)

    print("--------------------------------------------------")


if __name__ == "__main__":
    main()
