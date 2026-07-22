from expression.exp_soma import ExpSoma
from expression.id import Id
from expression.valor_inteiro import ValorInteiro
from command.comando_declaracao import ComandoDeclaracao
from command.sequencia_comando import SequenciaComando
from command.write import Write
from declaration.declaracao_composta import DeclaracaoComposta
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
    idA = Id("a")
    idB = Id("b")

    # var a = 2, var b = 5
    decA2 = DeclaracaoVariavel(idA, ValorInteiro(2))
    decB5 = DeclaracaoVariavel(idB, ValorInteiro(5))
    decComposta = DeclaracaoComposta(decA2, decB5)

    # write(a); write(b+a)
    writeA_interno = Write(idA)
    writeBA_interno = Write(ExpSoma(idB, idA))
    seq_interno = SequenciaComando(writeA_interno, writeBA_interno)

    # Bloco interno completo: { var a = 2, var b = 5; write(a); write(b+a) }
    blocoInterno = ComandoDeclaracao(decComposta, seq_interno)

    # var a = 3
    decA3 = DeclaracaoVariavel(idA, ValorInteiro(3))

    # Sequência de comandos externos: write(a); [blocoInterno]; write(a)
    writeA_externo1 = Write(idA)
    writeA_externo2 = Write(idA)

    seq_externa2 = SequenciaComando(blocoInterno, writeA_externo2)
    sequenciaComandoCompleta = SequenciaComando(writeA_externo1, seq_externa2)

    # Bloco externo completo
    blocoExterno = ComandoDeclaracao(decA3, sequenciaComandoCompleta)

    programa = Programa(blocoExterno)

    try:
        ambComp = ContextoCompilacaoImperativa(ListaValor())
        if programa.checaTipo(ambComp):
            ambExec = ContextoExecucaoImperativa(ListaValor())
            print("Saida do Exemplo 2:", programa.executar(ambExec))
        else:
            print("Erro de tipo no Exemplo 2!")
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
