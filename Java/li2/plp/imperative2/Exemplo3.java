package li2.plp.imperative2;

import li2.plp.expressions1.util.TipoPrimitivo;
import li2.plp.expressions2.expression.ExpEquals;
import li2.plp.expressions2.expression.ExpNot;
import li2.plp.expressions2.expression.ExpSub;
import li2.plp.expressions2.expression.Id;
import li2.plp.expressions2.expression.ValorInteiro;
import li2.plp.expressions2.expression.ValorString;
import li2.plp.imperative1.command.Atribuicao;
import li2.plp.imperative1.command.ComandoDeclaracao;
import li2.plp.imperative1.command.IfThenElse;
import li2.plp.imperative1.command.SequenciaComando;
import li2.plp.imperative1.command.Skip;
import li2.plp.imperative1.command.Write;
import li2.plp.imperative1.declaration.DeclaracaoComposta;
import li2.plp.imperative1.declaration.DeclaracaoVariavel;
import li2.plp.imperative1.memory.ContextoCompilacaoImperativa;
import li2.plp.imperative1.memory.ListaValor;
import li2.plp.imperative2.command.ChamadaProcedimento;
import li2.plp.imperative2.command.ListaExpressao;
import li2.plp.imperative2.declaration.DeclaracaoParametro;
import li2.plp.imperative2.declaration.DeclaracaoProcedimento;
import li2.plp.imperative2.declaration.DefProcedimento;
import li2.plp.imperative2.declaration.ListaDeclaracaoParametro;
import li2.plp.imperative2.memory.ContextoExecucaoImperativa2;

/**
 * Exemplo3 - Executa o seguinte programa na linguagem li2:
 *
 * { var b = 3,
 *   proc escreveRecursivo (int a) {
 *     if (not (a == 0)) then {
 *       var x = 0; x := a - 1;
 *       write("Ola");
 *       call escreveRecursivo(x)
 *     }
 *     else skip
 *   };
 *   call escreveRecursivo(b)
 * }
 *
 * Resultado esperado: escreve "Ola" 3 vezes (b=3, 2, 1) e para quando a==0
 */
public class Exemplo3 {

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
        System.out.println("Programa: \n" + descricao + "\n");
        try {
            boolean bemTipado = prog.checaTipo(new ContextoCompilacaoImperativa(new ListaValor()));
            System.out.println("Bem tipado: " + bemTipado);
            if (bemTipado) {
                ListaValor saida = prog.executar(ambiente);
                System.out.print("Saida: ");
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
        Id idB = new Id("b");
        Id idA = new Id("a");
        Id idX = new Id("x");
        Id idEscreveRecursivo = new Id("escreveRecursivo");

        // Declaracao de variavel do bloco externo: var b = 3
        DeclaracaoVariavel declB = new DeclaracaoVariavel(idB, new ValorInteiro(3));

        // Parametro formal do procedimento: int a
        DeclaracaoParametro paramA = new DeclaracaoParametro(idA, TipoPrimitivo.INTEIRO);
        ListaDeclaracaoParametro listaParamA = new ListaDeclaracaoParametro(paramA);

        // Condicao do if: not (a == 0)
        ExpNot condicao = new ExpNot(new ExpEquals(idA, new ValorInteiro(0)));

        // Corpo do bloco then:
        //   var x = 0; x := a - 1; write("Ola"); call escreveRecursivo(x)

        // Declaracao local: var x = 0
        DeclaracaoVariavel declX = new DeclaracaoVariavel(idX, new ValorInteiro(0));

        // Atribuicao: x := a - 1
        Atribuicao atribX = new Atribuicao(idX, new ExpSub(idA, new ValorInteiro(1)));

        // write("Ola")
        Write writeOla = new Write(new ValorString("Ola"));

        // call escreveRecursivo(x)  — parametro real: x
        ChamadaProcedimento chamadaRecursiva = new ChamadaProcedimento(
                idEscreveRecursivo, new ListaExpressao(idX));

        // Sequencia dentro do then: x := a-1; write("Ola"); call escreveRecursivo(x)
        SequenciaComando seqThen = new SequenciaComando(
                atribX,
                new SequenciaComando(writeOla, chamadaRecursiva)
        );

        // Bloco then completo: { var x = 0; x := a-1; write("Ola"); call escreveRecursivo(x) }
        ComandoDeclaracao blocoThen = new ComandoDeclaracao(declX, seqThen);

        // if (not (a == 0)) then { ... } else skip
        IfThenElse ifCmd = new IfThenElse(condicao, blocoThen, new Skip());

        // Definicao do procedimento escreveRecursivo (int a) { if ... }
        DefProcedimento defEscreveRecursivo = new DefProcedimento(listaParamA, ifCmd);

        // Declaracao do procedimento: proc escreveRecursivo (int a) { ... }
        DeclaracaoProcedimento declEscreveRecursivo =
                new DeclaracaoProcedimento(idEscreveRecursivo, defEscreveRecursivo);

        // Declaracao composta do bloco externo: var b = 3, proc escreveRecursivo (int a) { ... }
        DeclaracaoComposta declaracoes = new DeclaracaoComposta(declB, declEscreveRecursivo);

        // Comando principal: call escreveRecursivo(b)
        ChamadaProcedimento chamadaInicial = new ChamadaProcedimento(
                idEscreveRecursivo, new ListaExpressao(idB));

        // Bloco completo:
        // { var b = 3, proc escreveRecursivo (int a) { ... }; call escreveRecursivo(b) }
        ComandoDeclaracao blocoCompleto = new ComandoDeclaracao(declaracoes, chamadaInicial);

        // Ambiente de execucao
        ContextoExecucaoImperativa2 ambiente =
                new ContextoExecucaoImperativa2(new ListaValor());

        // Programa
        Programa prog = new Programa(blocoCompleto);

        // Executa
        executar(
            "{ var b = 3,\n" +
            "  proc escreveRecursivo (int a) {\n" +
            "    if (not (a == 0)) then {\n" +
            "      var x = 0; x := a - 1;\n" +
            "      write(\"Ola\");\n" +
            "      call escreveRecursivo(x)\n" +
            "    } else skip\n" +
            "  };\n" +
            "  call escreveRecursivo(b) }",
            prog,
            ambiente
        );
    }
}
