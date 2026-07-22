from expression.exp_equals import ExpEquals
from expression.exp_not import ExpNot
from expression.exp_soma import ExpSoma
from expression.id import Id
from expression.valor_inteiro import ValorInteiro
from expression.valor_string import ValorString
from command.atribuicao import Atribuicao
from command.comando_declaracao import ComandoDeclaracao
from command.sequencia_comando import SequenciaComando
from command.while_comando import While
from command.write import Write
from declaration.declaracao_variavel import DeclaracaoVariavel
from memory.contexto_compilacao_imperativa import ContextoCompilacaoImperativa
from memory.contexto_execucao_imperativa import ContextoExecucaoImperativa
from memory.lista_valor import ListaValor
from Programa import Programa
from exception.identificador_ja_declarado_exception import IdentificadorJaDeclaradoException
from exception.identificador_nao_declarado_exception import IdentificadorNaoDeclaradoException
from exception.entrada_vazia_exception import EntradaVaziaException
from exception.erro_tipo_entrada_exception import ErroTipoEntradaException

def main():
    idI = Id("i")

    # var i = 0
    decVarI = DeclaracaoVariavel(idI, ValorInteiro(0))

    # not (i == 3)
    condicaoWhile = ExpNot(ExpEquals(idI, ValorInteiro(3)))

    # i := i + 1
    atribuicaoI = Atribuicao(idI, ExpSoma(idI, ValorInteiro(1)))

    # Corpo do loop: i := i + 1; write("Hello World")
    writeHello = Write(ValorString("Hello World"))
    corpoWhile = SequenciaComando(atribuicaoI, writeHello)

    # while not (i == 3) do ...
    loopWhile = While(condicaoWhile, corpoWhile)

    # Bloco declarativo completo
    blocoDeclaracao = ComandoDeclaracao(decVarI, loopWhile)

    programa = Programa(blocoDeclaracao)

    try:
        ambComp = ContextoCompilacaoImperativa(ListaValor())
        if programa.checaTipo(ambComp):
            ambExec = ContextoExecucaoImperativa(ListaValor())
            print("Saida do Exemplo 3:", programa.executar(ambExec))
        else:
            print("Erro de tipo no Exemplo 3!")
    except IdentificadorJaDeclaradoException as e:
        print("Erro!! Identificador já declarado!")
        print("Detalhes:", e)
    except IdentificadorNaoDeclaradoException as e:
        print("Erro!! Identificador não declarada!")
        print("Detalhes:", e)
    except EntradaVaziaException as e:
        print("Erro! Nenhuma entrada foi fornecida!")
        print("Detalhes:", e)
    except ErroTipoEntradaException as e:
        print("Erro! O tipo de dado na entrada nao corresponde!")
        print("Detalhes:", e)

if __name__ == '__main__':
    main()
