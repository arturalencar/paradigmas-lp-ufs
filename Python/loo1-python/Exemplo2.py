import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from Programa import Programa
from command.atribuicao import Atribuicao
from command.chamada_metodo import ChamadaMetodo
from command.comando_declaracao import ComandoDeclaracao
from command.new import New
from command.sequencia_comando import SequenciaComando
from command.write import Write
from declaration.dec_classe_simples import DecClasseSimples
from declaration.dec_procedimento_composta import DecProcedimentoComposta
from declaration.dec_procedimento_simples import DecProcedimentoSimples
from declaration.dec_variavel_objeto import DecVariavelObjeto
from declaration.declaracao_variavel import DeclaracaoVariavel
from declaration.declaracao_composta import DeclaracaoComposta
from declaration.lista_declaracao_parametro import ListaDeclaracaoParametro
from expression.acesso_atributo_this import AcessoAtributoThis
from expression.exp_soma import ExpSoma
from expression.id import Id
from expression.this_expressao import This
from expression.valor_inteiro import ValorInteiro
from memory.contexto_compilacao_oo1 import ContextoCompilacaoOO1
from memory.contexto_execucao_oo1 import ContextoExecucaoOO1
from memory.lista_valor import ListaValor
from util.tipo_classe import TipoClasse
from util.tipo_primitivo import TipoPrimitivo
from expression.lista_expressao import ListaExpressao

def executar_exemplo(prog, descricao, ambiente):
    print("-" * 50)
    print("Programa: \n" + descricao + "\n")
    try:
        bem_tipado = prog.checaTipo(ContextoCompilacaoOO1(ListaValor()))
        print("Bem tipado:", bem_tipado)
        if bem_tipado:
            saida = prog.executar(ambiente)
            print("Saida:", end=" ")
            while saida is not None and saida.length() > 0:
                print(saida.getHead(), end=" ")
                saida = saida.getTail()
            print()
        else:
            print("Erro de tipo: execucao abortada.")
    except Exception as e:
        import traceback
        print("Excecao capturada: " + str(e))
        traceback.print_exc()
    print("-" * 50)

if __name__ == "__main__":
    # int valor = 1;
    dec_valor = DeclaracaoVariavel(TipoPrimitivo.INTEIRO, Id("valor"), ValorInteiro(1))

    # proc print() { write(this.valor) }
    write_valor = Write(AcessoAtributoThis(This(), Id("valor")))
    proc_print = DecProcedimentoSimples(Id("print"), ListaDeclaracaoParametro(), write_valor)

    # proc inc() { this.valor := this.valor + 1 }
    inc_valor = Atribuicao(
        AcessoAtributoThis(This(), Id("valor")), 
        ExpSoma(AcessoAtributoThis(This(), Id("valor")), ValorInteiro(1))
    )
    proc_inc = DecProcedimentoSimples(Id("inc"), ListaDeclaracaoParametro(), inc_valor)

    # proc print(), proc inc()
    dec_procedimentos = DecProcedimentoComposta(proc_print, proc_inc)

    # classe Contador { ... }
    dec_classe = DecClasseSimples(Id("Contador"), dec_valor, dec_procedimentos)

    # Contador c := new Contador;
    dec_c1 = DecVariavelObjeto(TipoClasse(Id("Contador")), Id("c"), Id("Contador"))
    # Contador c2 := new Contador;
    dec_c2 = DecVariavelObjeto(TipoClasse(Id("Contador")), Id("c2"), Id("Contador"))

    dec_composta = DeclaracaoComposta(dec_c1, dec_c2)

    # c.inc();
    c_inc = ChamadaMetodo(Id("c"), Id("inc"), ListaExpressao())
    # c2.inc();
    c2_inc1 = ChamadaMetodo(Id("c2"), Id("inc"), ListaExpressao())
    # c2.inc();
    c2_inc2 = ChamadaMetodo(Id("c2"), Id("inc"), ListaExpressao())
    # c.print();
    c_print = ChamadaMetodo(Id("c"), Id("print"), ListaExpressao())
    # c2.print();
    c2_print = ChamadaMetodo(Id("c2"), Id("print"), ListaExpressao())

    seq1 = SequenciaComando(c_inc, c2_inc1)
    seq2 = SequenciaComando(seq1, c2_inc2)
    seq3 = SequenciaComando(seq2, c_print)
    seq4 = SequenciaComando(seq3, c2_print)

    com_declaracao = ComandoDeclaracao(dec_composta, seq4)

    prog = Programa(dec_classe, com_declaracao)
    executar_exemplo(prog, "Contador c := new Contador, Contador c2 := new Contador;\nc.inc();\nc2.inc();\nc2.inc();\nc.print();\nc2.print()", ContextoExecucaoOO1())
