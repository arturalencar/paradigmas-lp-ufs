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
 * Atividade 5 - le2
 *
 * let var x = 3 in
 *   let var x = x + 1 in
 *     let var y = x in
 *       x + y
 *
 * Rastreamento (declaracao COLATERAL):
 *   Escopo 1: x = 3
 *   Escopo 2: x = x_externo + 1 = 3 + 1 = 4
 *             (colateral: a expressao "x+1" e avaliada ANTES de x ser redeclarado,
 *              portanto usa x=3 do escopo externo)
 *   Escopo 3: y = x = 4   (usa x=4 do escopo 2)
 *   Corpo:    x + y = 4 + 4 = 8
 *
 * Resultado esperado: 8
 */
public class Exemplo5 {

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

        // Bloco mais interno: let var y = x in x + y
        Expressao corpoMaisInterno = new ExpSoma(new Id("x"), new Id("y"));
        List<DecVariavel> decs3 = new ArrayList<DecVariavel>();
        decs3.add(new DecVariavel(new Id("y"), new Id("x")));
        Expressao let3 = new ExpDeclaracao(decs3, corpoMaisInterno);

        // Bloco do meio: let var x = x + 1 in <let3>
        // A expressao "x + 1" e avaliada no ambiente ANTES de x ser redeclarado (colateral)
        List<DecVariavel> decs2 = new ArrayList<DecVariavel>();
        decs2.add(new DecVariavel(new Id("x"), new ExpSoma(new Id("x"), new ValorInteiro(1))));
        Expressao let2 = new ExpDeclaracao(decs2, let3);

        // Bloco externo: let var x = 3 in <let2>
        List<DecVariavel> decs1 = new ArrayList<DecVariavel>();
        decs1.add(new DecVariavel(new Id("x"), new ValorInteiro(3)));
        Expressao let1 = new ExpDeclaracao(decs1, let2);

        Programa prog = new Programa(let1);

        executar("let var x = 3 in let var x = x+1 in let var y = x in x + y", prog);

        System.out.println("--------------------------------------------------");
    }
}
