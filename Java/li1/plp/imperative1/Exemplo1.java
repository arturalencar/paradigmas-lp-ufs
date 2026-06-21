package li1.plp.imperative1;

import li1.plp.expressions2.expression.Id;
import li1.plp.expressions2.expression.ValorInteiro;
import li1.plp.imperative1.command.Comando;
import li1.plp.imperative1.command.ComandoDeclaracao;
import li1.plp.imperative1.command.Write;
import li1.plp.imperative1.declaration.DeclaracaoVariavel;
import li1.plp.imperative1.memory.ContextoCompilacaoImperativa;
import li1.plp.imperative1.memory.ContextoExecucaoImperativa;
import li1.plp.imperative1.memory.ListaValor;
import li1.plp.expressions2.memory.IdentificadorJaDeclaradoException;
import li1.plp.expressions2.memory.IdentificadorNaoDeclaradoException;
import li1.plp.imperative1.memory.EntradaVaziaException;
import li1.plp.imperative1.memory.ErroTipoEntradaException;


public class Exemplo1 {

    public static void main(String[] args) {
        Id idA = new Id("a");

        // var a = 3
        DeclaracaoVariavel decVarA = new DeclaracaoVariavel(idA, new ValorInteiro(3));

        // write(a)
        Comando writeA = new Write(idA);

        // { var a = 3; write(a) }
        Comando blocoDeclaracao = new ComandoDeclaracao(decVarA, writeA);

        Programa programa = new Programa(blocoDeclaracao);

        try {
            ContextoCompilacaoImperativa ambComp = new ContextoCompilacaoImperativa(new ListaValor());
            if (programa.checaTipo(ambComp)) {
                ContextoExecucaoImperativa ambExec = new ContextoExecucaoImperativa(new ListaValor());
                System.out.println("Saida do Exemplo 1: " + programa.executar(ambExec));
            } else {
                System.out.println("Erro de tipo no Exemplo 1!");
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