import traceback
from util.tipo_primitivo import TipoPrimitivo
from expression.exp_equals import ExpEquals
from expression.exp_not import ExpNot
from expression.exp_sub import ExpSub
from expression.id import Id
from expression.valor_inteiro import ValorInteiro
from expression.valor_string import ValorString
from command.atribuicao import Atribuicao
from command.comando_declaracao import ComandoDeclaracao
from command.if_then_else import IfThenElse
from command.sequencia_comando import SequenciaComando
from command.skip import Skip
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
    id_b = Id("b")
    id_a = Id("a")
    id_x = Id("x")
    id_escreve_recursivo = Id("escreveRecursivo")

    decl_b = DeclaracaoVariavel(id_b, ValorInteiro(3))
    param_a = DeclaracaoParametro(id_a, TipoPrimitivo.inteiro())
    lista_param_a = ListaDeclaracaoParametro(param_a)

    condicao = ExpNot(ExpEquals(id_a, ValorInteiro(0)))
    decl_x = DeclaracaoVariavel(id_x, ValorInteiro(0))
    atrib_x = Atribuicao(id_x, ExpSub(id_a, ValorInteiro(1)))
    write_ola = Write(ValorString("Ola"))
    chamada_recursiva = ChamadaProcedimento(id_escreve_recursivo, ListaExpressao(id_x))

    seq_then = SequenciaComando(atrib_x, SequenciaComando(write_ola, chamada_recursiva))
    bloco_then = ComandoDeclaracao(decl_x, seq_then)

    if_cmd = IfThenElse(condicao, bloco_then, Skip())
    def_escreve_recursivo = DefProcedimento(lista_param_a, if_cmd)
    decl_escreve_recursivo = DeclaracaoProcedimento(id_escreve_recursivo, def_escreve_recursivo)

    declaracoes = DeclaracaoComposta(decl_b, decl_escreve_recursivo)
    chamada_inicial = ChamadaProcedimento(id_escreve_recursivo, ListaExpressao(id_b))
    bloco_completo = ComandoDeclaracao(declaracoes, chamada_inicial)

    ambiente = ContextoExecucaoImperativa2(ListaValor())
    prog = Programa(bloco_completo)

    executar(
        "{ var b = 3,\n" +
        "  proc escreveRecursivo (int a) {\n" +
        "    if (not (a == 0)) then {\n" +
        "      var x = 0; x := a - 1;\n" +
        "      write(\"Ola\");\n" +
        "      call escreveRecursivo(x)\n" +
        "    } else skip\n" +
        "  };\n" +
        "  call escreveRecursivo(b) }",
        prog,
        ambiente
    )
