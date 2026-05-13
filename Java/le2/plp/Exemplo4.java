package le2.plp;

import java.util.ArrayList;
import java.util.List;

import le2.plp.expressions2.Programa;
import le2.plp.expressions2.declaration.DecVariavel;
import le2.plp.expressions2.expression.ExpDeclaracao;
import le2.plp.expressions2.expression.ExpSoma;
import le2.plp.expressions2.expression.Expressao;
import le2.plp.expressions2.expression.Id;
import le2.plp.expressions2.expression.ValorInteiro;

/**
 * Atividade 4 - le2
 *
 * let var x = 3 in
 *   let var y = x + 1 in
 *     let var x = 5 in
 *       y
 *
 * Rastreamento:
 *   Escopo 1: x = 3
 *   Escopo 2: y = x + 1 = 4   (usa x=3)
 *   Escopo 3: x = 5            (shadowing, mas nao usado)
 *   Corpo:    y = 4            (y veio do escopo 2)
 *
 * Resultado esperado: 4
 */
public class Exemplo4 {

    static void executar(String descricao, Programa prog) {
        System.out.println("--------------------------------------------------");
        System.out.println("Expressao : " + descricao);
        try {
            boolean bemTipada = prog.checaTipo();
            System.out.println("Bem tipada: " + bemTipada);
            if (bemTipada) {
                System.out.println("Resultado: " + prog.executar());
            } else {
                System.out.println("Erro de tipo: avaliacao abortada.");
            }
        } catch (Exception e) {
            System.out.println("Excecao capturada: " + e.getMessage());
            e.printStackTrace();
        }
    }

    public static void main(String[] args) throws Exception {

        // Bloco mais interno: let var x = 5 in y
        List<DecVariavel> decs3 = new ArrayList<DecVariavel>();
        decs3.add(new DecVariavel(new Id("x"), new ValorInteiro(5)));
        Expressao let3 = new ExpDeclaracao(decs3, new Id("y"));

        // Bloco do meio: let var y = x + 1 in <let3>
        List<DecVariavel> decs2 = new ArrayList<DecVariavel>();
        decs2.add(new DecVariavel(new Id("y"), new ExpSoma(new Id("x"), new ValorInteiro(1))));
        Expressao let2 = new ExpDeclaracao(decs2, let3);

        // Bloco externo: let var x = 3 in <let2>
        List<DecVariavel> decs1 = new ArrayList<DecVariavel>();
        decs1.add(new DecVariavel(new Id("x"), new ValorInteiro(3)));
        Expressao let1 = new ExpDeclaracao(decs1, let2);

        Programa prog = new Programa(let1);

        executar("let var x = 3 in let var y = x+1 in let var x = 5 in y", prog);

        System.out.println("--------------------------------------------------");
    }
}
