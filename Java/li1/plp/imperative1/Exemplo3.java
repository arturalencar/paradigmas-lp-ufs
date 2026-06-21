package li1.plp.imperative1;

import li1.plp.expressions2.expression.ExpEquals;
import li1.plp.expressions2.expression.ExpNot;
import li1.plp.expressions2.expression.ExpSoma;
import li1.plp.expressions2.expression.Id;
import li1.plp.expressions2.expression.ValorInteiro;
import li1.plp.expressions2.expression.ValorString;
import li1.plp.imperative1.command.Atribuicao;
import li1.plp.imperative1.command.Comando;
import li1.plp.imperative1.command.ComandoDeclaracao;
import li1.plp.imperative1.command.SequenciaComando;
import li1.plp.imperative1.command.While;
import li1.plp.imperative1.command.Write;
import li1.plp.imperative1.declaration.DeclaracaoVariavel;
import li1.plp.imperative1.memory.ContextoCompilacaoImperativa;
import li1.plp.imperative1.memory.ContextoExecucaoImperativa;
import li1.plp.imperative1.memory.ListaValor;
import li1.plp.expressions2.memory.IdentificadorJaDeclaradoException;
import li1.plp.expressions2.memory.IdentificadorNaoDeclaradoException;
import li1.plp.imperative1.memory.EntradaVaziaException;
import li1.plp.imperative1.memory.ErroTipoEntradaException;


public class Exemplo3 {

    public static void main(String[] args) {
        Id idI = new Id("i");

        // var i = 0
        DeclaracaoVariavel decVarI = new DeclaracaoVariavel(idI, new ValorInteiro(0));

        // not (i == 3)
        ExpNot condicaoWhile = new ExpNot(new ExpEquals(idI, new ValorInteiro(3)));

        // i := i + 1
        Comando atribuicaoI = new Atribuicao(idI, new ExpSoma(idI, new ValorInteiro(1)));

        // Corpo do loop: i := i + 1; write("Hello World")
        Comando writeHello = new Write(new ValorString("Hello World"));
        Comando corpoWhile = new SequenciaComando(atribuicaoI, writeHello);

        // while not (i == 3) do ...
        Comando loopWhile = new While(condicaoWhile, corpoWhile);

        // Bloco declarativo completo
        Comando blocoDeclaracao = new ComandoDeclaracao(decVarI, loopWhile);

        Programa programa = new Programa(blocoDeclaracao);

        try {
            ContextoCompilacaoImperativa ambComp = new ContextoCompilacaoImperativa(new ListaValor());
            if (programa.checaTipo(ambComp)) {
                ContextoExecucaoImperativa ambExec = new ContextoExecucaoImperativa(new ListaValor());
                System.out.println("Saida do Exemplo 3: " + programa.executar(ambExec));
            } else {
                System.out.println("Erro de tipo no Exemplo 3!");
            }
        } catch (IdentificadorJaDeclaradoException e) {
            System.err.println("Erro!! Identificador já declarado!");
            System.err.println("Detalhes: " + e.getMessage());
            
        } catch (IdentificadorNaoDeclaradoException e) {
            System.err.println("Erro!! Identificador não declarada!");
            System.err.println("Detalhes: " + e.getMessage());
            
        } catch (EntradaVaziaException e) {
            System.err.println("Erro! Nenhuma entrada foi fornecida!");
            System.err.println("Detalhes: " + e.getMessage());
            
        } catch (ErroTipoEntradaException e) {
            System.err.println("Erro! O tipo de dado na entrada nao corresponde!");
            System.err.println("Detalhes: " + e.getMessage());
        }

    }
}