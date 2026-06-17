package li2.plp.imperative2;

import li2.plp.expressions1.util.TipoPrimitivo;
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
import li2.plp.imperative2.declaration.DeclaracaoParametro;
import li2.plp.imperative2.declaration.DeclaracaoProcedimento;
import li2.plp.imperative2.declaration.DefProcedimento;
import li2.plp.imperative2.declaration.ListaDeclaracaoParametro;
import li2.plp.imperative2.memory.ContextoExecucaoImperativa2;

/**
 * Exemplo2 - Executa o seguinte programa na linguagem li2:
 *
 * { var x = 0, proc p (int y) { x := x + y };
 *   { var x = 1; call p(3); write(x) };
 *   call p(4); write(x)
 * }
 */
public class Exemplo2 {

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
        Id idX = new Id("x");
        Id idY = new Id("y");
        Id idP = new Id("p");

        // Declaracao de variavel do bloco externo: var x = 0
        DeclaracaoVariavel declX = new DeclaracaoVariavel(idX, new ValorInteiro(0));

        // Parametro formal do procedimento p: int y
        DeclaracaoParametro paramY = new DeclaracaoParametro(idY, TipoPrimitivo.INTEIRO);
        ListaDeclaracaoParametro listaParamY = new ListaDeclaracaoParametro(paramY);

        // Corpo do procedimento p: x := x + y
        Atribuicao corpoP = new Atribuicao(idX, new ExpSoma(idX, idY));

        // Definicao do procedimento p (com parametro formal int y)
        DefProcedimento defP = new DefProcedimento(listaParamY, corpoP);

        // Declaracao de procedimento: proc p (int y) { x := x + y }
        DeclaracaoProcedimento declP = new DeclaracaoProcedimento(idP, defP);

        // Declaracao composta do bloco externo: var x = 0, proc p (int y) { ... }
        DeclaracaoComposta declExterno = new DeclaracaoComposta(declX, declP);

        // Bloco interno: { var x = 1; call p(3); write(x) }
        DeclaracaoVariavel declXInterno = new DeclaracaoVariavel(idX, new ValorInteiro(1));

        // call p(3) — parametro real: 3
        ChamadaProcedimento chamadaP3 = new ChamadaProcedimento(
                idP, new ListaExpressao(new ValorInteiro(3)));

        // write(x) dentro do bloco interno
        Write writeXInterno = new Write(idX);

        // Sequencia interna: call p(3); write(x)
        SequenciaComando seqInterna = new SequenciaComando(chamadaP3, writeXInterno);

        // Bloco interno completo: { var x = 1; call p(3); write(x) }
        ComandoDeclaracao blocoInterno = new ComandoDeclaracao(declXInterno, seqInterna);

        // Comandos do bloco externo apos as declaracoes:
        //   { var x = 1; call p(3); write(x) }; call p(4); write(x)

        // call p(4) — parametro real: 4
        ChamadaProcedimento chamadaP4 = new ChamadaProcedimento(
                idP, new ListaExpressao(new ValorInteiro(4)));

        // write(x) no bloco externo
        Write writeXExterno = new Write(idX);

        // Sequencia externa: blocoInterno; call p(4); write(x)
        SequenciaComando seqExterna = new SequenciaComando(
                blocoInterno,
                new SequenciaComando(chamadaP4, writeXExterno)
        );

        // Bloco completo:
        // { var x = 0, proc p (int y) { x := x + y };
        //   { var x = 1; call p(3); write(x) };
        //   call p(4); write(x)
        // }
        ComandoDeclaracao blocoCompleto = new ComandoDeclaracao(declExterno, seqExterna);

        // Ambiente de execucao
        ContextoExecucaoImperativa2 ambiente =
                new ContextoExecucaoImperativa2(new ListaValor());

        // Programa
        Programa prog = new Programa(blocoCompleto);

        // Executa
        executar(
            "{ var x = 0, proc p (int y) { x := x + y };\n" +
            "    { var x = 1; call p(3); write(x) };\n" +
            "call p(4); write(x) }",
            prog,
            ambiente
        );
    }
}
