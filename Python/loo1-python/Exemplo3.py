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
from command.skip import Skip
from command.if_then_else import IfThenElse
from declaration.dec_classe_simples import DecClasseSimples
from declaration.dec_procedimento_composta import DecProcedimentoComposta
from declaration.dec_procedimento_simples import DecProcedimentoSimples
from declaration.dec_variavel_objeto import DecVariavelObjeto
from declaration.declaracao_variavel import DeclaracaoVariavel
from declaration.declaracao_composta import DeclaracaoComposta
from declaration.lista_declaracao_parametro import ListaDeclaracaoParametro
from declaration.dec_parametro import DecParametro
from expression.acesso_atributo_this import AcessoAtributoThis
from expression.exp_equals import ExpEquals
from expression.exp_not import ExpNot
from expression.id import Id
from expression.this_expressao import This
from expression.valor_inteiro import ValorInteiro
from expression.valor_null import ValorNull
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
    idLValor = Id("LValor")
    tipoLValor = TipoClasse(idLValor)

    decValor = DeclaracaoVariavel(TipoPrimitivo.INTEIRO, Id("valor"), ValorInteiro(-100))
    decProx = DeclaracaoVariavel(tipoLValor, Id("prox"), ValorNull())
    decVariaveis = DeclaracaoComposta(decValor, decProx)

    idV = Id("v")
    paramV = ListaDeclaracaoParametro(DecParametro(idV, TipoPrimitivo.INTEIRO))

    condInsere = ExpEquals(AcessoAtributoThis(This(), Id("valor")), ValorInteiro(-100))
    thisValorV = Atribuicao(AcessoAtributoThis(This(), Id("valor")), idV)
    thisProxNew = New(AcessoAtributoThis(This(), Id("prox")), idLValor)
    thenInsere = SequenciaComando(thisValorV, thisProxNew)

    argV = ListaExpressao(idV)
    elseInsere = ChamadaMetodo(AcessoAtributoThis(This(), Id("prox")), Id("insere"), argV)

    ifInsere = IfThenElse(condInsere, thenInsere, elseInsere)
    procInsere = DecProcedimentoSimples(Id("insere"), paramV, ifInsere)

    writeValor = Write(AcessoAtributoThis(This(), Id("valor")))
    proxNull = ExpEquals(AcessoAtributoThis(This(), Id("prox")), ValorNull())
    condPrint = ExpNot(proxNull)

    thenPrint = ChamadaMetodo(AcessoAtributoThis(This(), Id("prox")), Id("print"), ListaExpressao())
    elsePrint = Skip()

    ifPrint = IfThenElse(condPrint, thenPrint, elsePrint)
    corpoPrint = SequenciaComando(writeValor, ifPrint)

    procPrint = DecProcedimentoSimples(Id("print"), ListaDeclaracaoParametro(), corpoPrint)
    decProcedimentos = DecProcedimentoComposta(procInsere, procPrint)

    decClasse = DecClasseSimples(idLValor, decVariaveis, decProcedimentos)

    decLv = DecVariavelObjeto(tipoLValor, Id("lv"), idLValor)

    arg3 = ListaExpressao(ValorInteiro(3))
    lvInsere3 = ChamadaMetodo(Id("lv"), Id("insere"), arg3)

    arg4 = ListaExpressao(ValorInteiro(4))
    lvInsere4 = ChamadaMetodo(Id("lv"), Id("insere"), arg4)

    lvPrint = ChamadaMetodo(Id("lv"), Id("print"), ListaExpressao())

    seqPrin1 = SequenciaComando(lvInsere3, lvInsere4)
    seqPrin2 = SequenciaComando(seqPrin1, lvPrint)

    comDeclaracao = ComandoDeclaracao(decLv, seqPrin2)
    prog = Programa(decClasse, comDeclaracao)

    executar_exemplo(prog, "LValor lv := new LValor;\nlv.insere(3);\nlv.insere(4);\nlv.print()", ContextoExecucaoOO1())
