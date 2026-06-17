package li2.plp.imperative2;

import li2.plp.expressions2.expression.ExpSoma;
import li2.plp.expressions2.expression.Id;
import li2.plp.expressions2.expression.ValorInteiro;
import li2.plp.imperative1.command.Atribuicao;
import li2.plp.imperative1.command.ComandoDeclaracao;
import li2.plp.imperative1.command.SequenciaComando;
import li2.plp.imperative1.command.Write;
import li2.plp.imperative1.declaration.DeclaracaoComposta;
import li2.plp.imperative1.declaration.DeclaracaoVariavel;
import li2.plp.imperative1.memory.ContextoCompilacaoImperativa;
import li2.plp.imperative1.memory.ListaValor;
import li2.plp.imperative2.command.ChamadaProcedimento;
import li2.plp.imperative2.command.ListaExpressao;
import li2.plp.imperative2.declaration.DeclaracaoProcedimento;
import li2.plp.imperative2.declaration.DefProcedimento;
import li2.plp.imperative2.declaration.ListaDeclaracaoParametro;
import li2.plp.imperative2.memory.ContextoExecucaoImperativa2;

/**
 * Exemplo1 - Executa o seguinte programa na linguagem li2:
 *
 * { var a = 0, proc incA () { a := a + 1 };
 *   call incA(); call incA(); write(a)
 * }
 *
 * Resultado esperado: write imprime 2
 */
public class Exemplo1 {

    /**
     * Executa um programa li2, verificando tipos antes de rodar.
     * Imprime a saida produzida pelo write ou a excecao capturada.
     *
     * @param descricao texto descritivo do programa
     * @param prog      o programa a executar
     * @param ambiente  o ambiente de execucao (contexto imperativo2)
     */
    static void executar(String descricao, Programa prog,
                         ContextoExecucaoImperativa2 ambiente) {
        System.out.println("--------------------------------------------------");
        System.out.println("Programa  : " + descricao);
        try {
            boolean bemTipado = prog.checaTipo(new ContextoCompilacaoImperativa(new ListaValor()));
            System.out.println("Bem tipado: " + bemTipado);
            if (bemTipado) {
                ListaValor saida = prog.executar(ambiente);
                System.out.print("Saida     : ");
                while (saida.length() > 0) {
                    System.out.print(saida.getHead() + " ");
                    saida = (ListaValor) saida.getTail();
                }
                System.out.println();
            } else {
                System.out.println("Erro de tipo: execucao abortada.");
            }
        } catch (Exception e) {
            System.out.println("Excecao capturada: " + e.getMessage());
            e.printStackTrace();
        }
        System.out.println("--------------------------------------------------");
    }

    public static void main(String[] args) {

        // Identificadores
        Id idA    = new Id("a");
        Id idIncA = new Id("incA");

        // Declaracao de variavel: var a = 0
        DeclaracaoVariavel declA = new DeclaracaoVariavel(idA, new ValorInteiro(0));

        // Corpo do procedimento incA: a := a + 1
        Atribuicao corpoIncA = new Atribuicao(idA, new ExpSoma(idA, new ValorInteiro(1)));

        // Definicao do procedimento incA (sem parametros formais)
        DefProcedimento defIncA = new DefProcedimento(
                new ListaDeclaracaoParametro(),  // lista vazia de parametros
                corpoIncA
        );

        // Declaracao de procedimento: proc incA () { a := a + 1 }
        DeclaracaoProcedimento declIncA = new DeclaracaoProcedimento(idIncA, defIncA);

        // Declaracao composta: var a = 0, proc incA () { ... }
        DeclaracaoComposta declaracoes = new DeclaracaoComposta(declA, declIncA);

        // Sequencia de comandos: call incA(); call incA(); write(a)
        ChamadaProcedimento chamada1 = new ChamadaProcedimento(idIncA, new ListaExpressao());
        ChamadaProcedimento chamada2 = new ChamadaProcedimento(idIncA, new ListaExpressao());
        Write writeA = new Write(idA);

        SequenciaComando seq = new SequenciaComando(
                chamada1,
                new SequenciaComando(chamada2, writeA)
        );

        // Bloco completo: { var a = 0, proc incA () {...}; call incA(); call incA(); write(a) }
        ComandoDeclaracao bloco = new ComandoDeclaracao(declaracoes, seq);

        // Ambiente de execucao
        ContextoExecucaoImperativa2 ambiente =
                new ContextoExecucaoImperativa2(new ListaValor());

        // Programa
        Programa prog = new Programa(bloco);

        // Executa
        executar(
            "{ var a = 0, proc incA () { a := a + 1 };\n" +
            "  call incA(); call incA(); write(a) }",
            prog,
            ambiente
        );
    }
}
