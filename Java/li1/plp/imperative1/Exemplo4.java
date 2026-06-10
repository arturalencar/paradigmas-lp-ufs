package li1.plp.imperative1;

import li1.plp.expressions2.expression.ExpEquals;
import li1.plp.expressions2.expression.Id;
import li1.plp.expressions2.expression.ValorInteiro;
import li1.plp.expressions2.expression.ValorString;
import li1.plp.imperative1.command.Atribuicao;
import li1.plp.imperative1.command.Comando;
import li1.plp.imperative1.command.ComandoDeclaracao;
import li1.plp.imperative1.command.IfThenElse;
import li1.plp.imperative1.command.SequenciaComando;
import li1.plp.imperative1.command.Write;
import li1.plp.imperative1.declaration.DeclaracaoComposta;
import li1.plp.imperative1.declaration.DeclaracaoVariavel;
import li1.plp.imperative1.memory.ContextoCompilacaoImperativa;
import li1.plp.imperative1.memory.ContextoExecucaoImperativa;
import li1.plp.imperative1.memory.ListaValor;

public class Exemplo4 {

    public static void main(String[] args) {
        Id idN = new Id("n");
        Id idM = new Id("m");

        // var n = 0, var m = 0
        DeclaracaoVariavel decN0 = new DeclaracaoVariavel(idN, new ValorInteiro(0));
        DeclaracaoVariavel decM0 = new DeclaracaoVariavel(idM, new ValorInteiro(0));
        DeclaracaoComposta decComposta = new DeclaracaoComposta(decN0, decM0);

        // n := 2
        Comando atribN2 = new Atribuicao(idN, new ValorInteiro(2));

        // m := 3
        Comando atribM3 = new Atribuicao(idM, new ValorInteiro(3));

        // if (m == n) then write(...) else write(...)
        ExpEquals condicaoIf = new ExpEquals(idM, idN);
        Comando thenBranch = new Write(new ValorString("valores de entrada iguais"));
        Comando elseBranch = new Write(new ValorString("valores de entrada diferentes"));
        Comando condicionalIf = new IfThenElse(condicaoIf, thenBranch, elseBranch);

        // Juntando os comandos em sequência: n := 2; m := 3; condicionalIf
        Comando seqComandos2 = new SequenciaComando(atribM3, condicionalIf);
        Comando sequenciaCompleta = new SequenciaComando(atribN2, seqComandos2);

        // Bloco do comando declaração completo
        Comando blocoDeclaracao = new ComandoDeclaracao(decComposta, sequenciaCompleta);

        Programa programa = new Programa(blocoDeclaracao);

        try {
            ContextoCompilacaoImperativa ambComp = new ContextoCompilacaoImperativa(new ListaValor());
            if (programa.checaTipo(ambComp)) {
                ContextoExecucaoImperativa ambExec = new ContextoExecucaoImperativa(new ListaValor());
                System.out.println("Saida do Exemplo 4: " + programa.executar(ambExec));
            } else {
                System.out.println("Erro de tipo no Exemplo 4!");
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}