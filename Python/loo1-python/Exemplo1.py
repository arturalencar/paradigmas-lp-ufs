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
        print("Excecao capturada:", e)
    print("-" * 50)

if __name__ == "__main__":
    # int valor = 1;
    dec_valor = DeclaracaoVariavel(Id("valor"), ValorInteiro(1))

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
    dec_c = DecVariavelObjeto(TipoClasse(Id("Contador")), Id("c"), Id("Contador"))

    # c.inc();
    c_inc = ChamadaMetodo(Id("c"), Id("inc"), ListaExpressao())

    # c.print();
    c_print = ChamadaMetodo(Id("c"), Id("print"), ListaExpressao())

    # c.inc(); c.print();
    inc_e_print = SequenciaComando(c_inc, c_print)

    # { Contador c := new Contador; c.inc(); c.print(); }
    com_declaracao = ComandoDeclaracao(dec_c, inc_e_print)

    # Programa
    prog = Programa(dec_classe, com_declaracao)

    # Executar
    executar_exemplo(prog, "Contador c := new Contador; c.inc(); c.print();", ContextoExecucaoOO1())
