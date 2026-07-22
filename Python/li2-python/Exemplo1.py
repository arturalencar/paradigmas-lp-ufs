import traceback
from expression.exp_soma import ExpSoma
from expression.id import Id
from expression.valor_inteiro import ValorInteiro
from command.atribuicao import Atribuicao
from command.comando_declaracao import ComandoDeclaracao
from command.sequencia_comando import SequenciaComando
from command.write import Write
from declaration.declaracao_composta import DeclaracaoComposta
from declaration.declaracao_variavel import DeclaracaoVariavel
from memory.contexto_compilacao_imperativa import ContextoCompilacaoImperativa
from memory.lista_valor import ListaValor
from command.chamada_procedimento import ChamadaProcedimento
from command.lista_expressao import ListaExpressao
from declaration.declaracao_procedimento import DeclaracaoProcedimento
from declaration.def_procedimento import DefProcedimento
from declaration.lista_declaracao_parametro import ListaDeclaracaoParametro
from memory.contexto_execucao_imperativa2 import ContextoExecucaoImperativa2
from Programa import Programa

def executar(descricao, prog, ambiente):
    print("-" * 50)
    print("Programa  : \n" + descricao + "\n")
    try:
        bem_tipado = prog.checaTipo(ContextoCompilacaoImperativa(ListaValor()))
        print("Bem tipado:", bem_tipado)
        if bem_tipado:
            saida = prog.executar(ambiente)
            print("Saida: ", end="")
            while saida is not None and saida.length() > 0:
                print(saida.getHead(), end=" ")
                saida = saida.getTail()
            print()
        else:
            print("Erro de tipo: execucao abortada.")
    except Exception as e:
        print("Excecao capturada:", e)
        traceback.print_exc()
    print("-" * 50)

if __name__ == "__main__":
    id_a = Id("a")
    id_inc_a = Id("incA")

    decl_a = DeclaracaoVariavel(id_a, ValorInteiro(0))
    corpo_inc_a = Atribuicao(id_a, ExpSoma(id_a, ValorInteiro(1)))
    def_inc_a = DefProcedimento(ListaDeclaracaoParametro(), corpo_inc_a)
    decl_inc_a = DeclaracaoProcedimento(id_inc_a, def_inc_a)
    declaracoes = DeclaracaoComposta(decl_a, decl_inc_a)

    chamada1 = ChamadaProcedimento(id_inc_a, ListaExpressao())
    chamada2 = ChamadaProcedimento(id_inc_a, ListaExpressao())
    write_a = Write(id_a)
    seq = SequenciaComando(chamada1, SequenciaComando(chamada2, write_a))

    bloco = ComandoDeclaracao(declaracoes, seq)
    ambiente = ContextoExecucaoImperativa2(ListaValor())
    prog = Programa(bloco)

    executar(
        "{ var a = 0, proc incA () { a := a + 1 };\n" +
        "  call incA(); call incA(); write(a) }",
        prog,
        ambiente
    )
