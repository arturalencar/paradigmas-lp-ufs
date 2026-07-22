from expression.exp_equals import ExpEquals
from expression.id import Id
from expression.valor_inteiro import ValorInteiro
from expression.valor_string import ValorString
from command.atribuicao import Atribuicao
from command.comando_declaracao import ComandoDeclaracao
from command.if_then_else import IfThenElse
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
    idN = Id("n")
    idM = Id("m")

    # var n = 0, var m = 0
    decN0 = DeclaracaoVariavel(idN, ValorInteiro(0))
    decM0 = DeclaracaoVariavel(idM, ValorInteiro(0))
    decComposta = DeclaracaoComposta(decN0, decM0)

    # n := 2
    atribN2 = Atribuicao(idN, ValorInteiro(2))

    # m := 3
    atribM3 = Atribuicao(idM, ValorInteiro(3))

    # if (m == n) then write(...) else write(...)
    condicaoIf = ExpEquals(idM, idN)
    thenBranch = Write(ValorString("valores de entrada iguais"))
    elseBranch = Write(ValorString("valores de entrada diferentes"))
    condicionalIf = IfThenElse(condicaoIf, thenBranch, elseBranch)

    # Juntando os comandos em sequência: n := 2; m := 3; condicionalIf
    seqComandos2 = SequenciaComando(atribM3, condicionalIf)
    sequenciaCompleta = SequenciaComando(atribN2, seqComandos2)

    # Bloco do comando declaração completo
    blocoDeclaracao = ComandoDeclaracao(decComposta, sequenciaCompleta)

    programa = Programa(blocoDeclaracao)

    try:
        ambComp = ContextoCompilacaoImperativa(ListaValor())
        if programa.checaTipo(ambComp):
            ambExec = ContextoExecucaoImperativa(ListaValor())
            print("Saida do Exemplo 4:", programa.executar(ambExec))
        else:
            print("Erro de tipo no Exemplo 4!")
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
