package li1.plp.imperative1;

import li1.plp.expressions2.expression.ExpSoma;
import li1.plp.expressions2.expression.Id;
import li1.plp.expressions2.expression.ValorInteiro;
import li1.plp.imperative1.command.Comando;
import li1.plp.imperative1.command.ComandoDeclaracao;
import li1.plp.imperative1.command.SequenciaComando;
import li1.plp.imperative1.command.Write;
import li1.plp.imperative1.declaration.DeclaracaoComposta;
import li1.plp.imperative1.declaration.DeclaracaoVariavel;
import li1.plp.imperative1.memory.ContextoCompilacaoImperativa;
import li1.plp.imperative1.memory.ContextoExecucaoImperativa;
import li1.plp.imperative1.memory.ListaValor;

public class Exemplo2 {

    public static void main(String[] args) {
        Id idA = new Id("a");
        Id idB = new Id("b");

        // var a = 2, var b = 5
        DeclaracaoVariavel decA2 = new DeclaracaoVariavel(idA, new ValorInteiro(2));
        DeclaracaoVariavel decB5 = new DeclaracaoVariavel(idB, new ValorInteiro(5));
        DeclaracaoComposta decComposta = new DeclaracaoComposta(decA2, decB5);

        // write(a); write(b+a)
        Comando writeA_interno = new Write(idA);
        Comando writeBA_interno = new Write(new ExpSoma(idB, idA));
        Comando seq_interno = new SequenciaComando(writeA_interno, writeBA_interno);

        // Bloco interno completo: { var a = 2, var b = 5; write(a); write(b+a) }
        Comando blocoInterno = new ComandoDeclaracao(decComposta, seq_interno);


        // var a = 3
        DeclaracaoVariavel decA3 = new DeclaracaoVariavel(idA, new ValorInteiro(3));

        // Sequência de comandos externos: write(a); [blocoInterno]; write(a)
        Comando writeA_externo1 = new Write(idA);
        Comando writeA_externo2 = new Write(idA);

        Comando seq_externa2 = new SequenciaComando(blocoInterno, writeA_externo2);
        Comando sequenciaComandoCompleta = new SequenciaComando(writeA_externo1, seq_externa2);

        // Bloco externo completo
        Comando blocoExterno = new ComandoDeclaracao(decA3, sequenciaComandoCompleta);

        Programa programa = new Programa(blocoExterno);

        try {
            ContextoCompilacaoImperativa ambComp = new ContextoCompilacaoImperativa(new ListaValor());
            if (programa.checaTipo(ambComp)) {
                ContextoExecucaoImperativa ambExec = new ContextoExecucaoImperativa(new ListaValor());
                System.out.println("Saida do Exemplo 2: " + programa.executar(ambExec));
            } else {
                System.out.println("Erro de tipo no Exemplo 2!");
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}