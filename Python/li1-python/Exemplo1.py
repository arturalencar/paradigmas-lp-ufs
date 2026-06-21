from expression.id import Id
from expression.valor_inteiro import ValorInteiro
from command.comando_declaracao import ComandoDeclaracao
from command.write import Write
from declaration.declaracao_variavel import DeclaracaoVariavel
from memory.contexto_compilacao_imperativa import ContextoCompilacaoImperativa
from memory.contexto_execucao_imperativa import ContextoExecucaoImperativa
from memory.lista_valor import ListaValor
from Programa import Programa
from memory.identificador_ja_declarado_exception import IdentificadorJaDeclaradoException
from memory.identificador_nao_declarado_exception import IdentificadorNaoDeclaradoException
from memory.entrada_vazia_exception import EntradaVaziaException
from memory.erro_tipo_entrada_exception import ErroTipoEntradaException

def main():
    idA = Id("a")

    # var a = 3
    decVarA = DeclaracaoVariavel(idA, ValorInteiro(3))

    # write(a)
    writeA = Write(idA)

    # { var a = 3; write(a) }
    blocoDeclaracao = ComandoDeclaracao(decVarA, writeA)

    programa = Programa(blocoDeclaracao)

    try:
        ambComp = ContextoCompilacaoImperativa(ListaValor())
        if programa.checaTipo(ambComp):
            ambExec = ContextoExecucaoImperativa(ListaValor())
            print("Saida do Exemplo 1:", programa.executar(ambExec))
        else:
            print("Erro de tipo no Exemplo 1!")
            
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
