import traceback
from util.tipo_primitivo import TipoPrimitivo
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
from declaration.declaracao_parametro import DeclaracaoParametro
from declaration.declaracao_procedimento import DeclaracaoProcedimento
from declaration.def_procedimento import DefProcedimento
from declaration.lista_declaracao_parametro import ListaDeclaracaoParametro
from memory.contexto_execucao_imperativa2 import ContextoExecucaoImperativa2
from Programa import Programa

def executar(descricao, prog, ambiente):
    print("-" * 50)
    print("Programa: \n" + descricao + "\n")
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
    id_x = Id("x")
    id_y = Id("y")
    id_p = Id("p")

    decl_x = DeclaracaoVariavel(id_x, ValorInteiro(0))
    param_y = DeclaracaoParametro(id_y, TipoPrimitivo.inteiro())
    lista_param_y = ListaDeclaracaoParametro(param_y)

    corpo_p = Atribuicao(id_x, ExpSoma(id_x, id_y))
    def_p = DefProcedimento(lista_param_y, corpo_p)
    decl_p = DeclaracaoProcedimento(id_p, def_p)
    decl_externo = DeclaracaoComposta(decl_x, decl_p)

    decl_x_interno = DeclaracaoVariavel(id_x, ValorInteiro(1))
    chamada_p3 = ChamadaProcedimento(id_p, ListaExpressao(ValorInteiro(3)))
    write_x_interno = Write(id_x)
    seq_interna = SequenciaComando(chamada_p3, write_x_interno)
    bloco_interno = ComandoDeclaracao(decl_x_interno, seq_interna)

    chamada_p4 = ChamadaProcedimento(id_p, ListaExpressao(ValorInteiro(4)))
    write_x_externo = Write(id_x)
    seq_externa = SequenciaComando(bloco_interno, SequenciaComando(chamada_p4, write_x_externo))

    bloco_completo = ComandoDeclaracao(decl_externo, seq_externa)
    ambiente = ContextoExecucaoImperativa2(ListaValor())
    prog = Programa(bloco_completo)

    executar(
        "{ var x = 0, proc p (int y) { x := x + y };\n" +
        "    { var x = 1; call p(3); write(x) };\n" +
        "call p(4); write(x) }",
        prog,
        ambiente
    )
