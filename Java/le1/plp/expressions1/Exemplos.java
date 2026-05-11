package le1.plp.expressions1;

import le1.plp.expressions1.expression.*;

public class Exemplos {

    static void executar(String descricao, Programa prog) {
        System.out.println("--------------------------------------------------");
        System.out.println("Expressão : " + descricao);

        boolean bemTipada = prog.checaTipo();
        System.out.println("Bem tipada: " + bemTipada);

        if (bemTipada) {
            prog.executar();
        } else {
            System.out.println("Erro de tipo: expressão mal tipada, avaliação abortada.");
        }
    }

    public static void main(String[] args) {

        // 1) -4 + 12 - 3
        Expressao exp1 = new ExpSub(
                            new ExpSoma(
                                new ExpMenos(new ValorInteiro(4)),
                                new ValorInteiro(12)),
                            new ValorInteiro(3));
        executar("-4 + 12 - 3", new Programa(exp1));

        // 2) length("abc") + 3
        Expressao exp2 = new ExpSoma(
                            new ExpLength(new ValorString("abc")),
                            new ValorInteiro(3));
        executar("length(\"abc\") + 3", new Programa(exp2));

        // 3) true and false
        Expressao exp3 = new ExpAnd(
                            new ValorBooleano(true),
                            new ValorBooleano(false));
        executar("true and false", new Programa(exp3));

        // 4) "curso" ++ " de " ++ " paradigmas"
        Expressao exp4 = new ExpConcat(
                            new ExpConcat(
                                new ValorString("curso"),
                                new ValorString(" de ")),
                            new ValorString(" paradigmas"));
        executar("\"curso\" ++ \" de \" ++ \" paradigmas\"", new Programa(exp4));

        // 5) 1 + true (erro de tipo - NAO avalia)
        Expressao exp5 = new ExpSoma(
                            new ValorInteiro(1),
                            new ValorBooleano(true));
        executar("1 + true", new Programa(exp5));

        System.out.println("--------------------------------------------------");
    }
}
