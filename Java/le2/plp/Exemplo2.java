package le2.plp;

import java.util.ArrayList;
import java.util.List;

import le2.plp.expressions2.Programa;
import le2.plp.expressions2.declaration.DecVariavel;
import le2.plp.expressions2.expression.ExpDeclaracao;
import le2.plp.expressions2.expression.ExpSoma;
import le2.plp.expressions2.expression.Id;
import le2.plp.expressions2.expression.ValorInteiro;

/**
 * Atividade - Linguagem de Expressão 2 (le2)
 *
 * Avalia a expressão:
 *   let var x = 1 in
 *       let var x = 2 in x + 1
 *
 * Árvore de expressão:
 *
 *         ExpDeclaracao (externa)
 *        /                      \
 *   DecVariavel              ExpDeclaracao (interna)
 *   (x = 1)                 /                     \
 *                      DecVariavel              ExpSoma
 *                      (x = 2)                 /        \
 *                                           Id(x)    ValorInteiro(1)
 *
 * Observação: o x interno (= 2) sombreia o x externo (= 1).
 *             Logo, a soma x + 1 calcula 2 + 1.
 *
 * Resultado esperado: 3
 */
public class Exemplo2 {

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

    public static void main(String[] args) {

        // --- Escopo externo: var x = 1 ---
        Id xExterno = new Id("x");
        ValorInteiro v1 = new ValorInteiro(1);
        DecVariavel decXExterno = new DecVariavel(xExterno, v1);

        List<DecVariavel> declaracoesExternas = new ArrayList<DecVariavel>();
        declaracoesExternas.add(decXExterno);

        // --- Escopo interno: var x = 2 ---
        Id xInterno = new Id("x");
        ValorInteiro v2 = new ValorInteiro(2);
        DecVariavel decXInterno = new DecVariavel(xInterno, v2);

        List<DecVariavel> declaracoesInternas = new ArrayList<DecVariavel>();
        declaracoesInternas.add(decXInterno);

        // --- Corpo do escopo interno: x + 1  (soma) ---
        // O x resolvido aqui será o do escopo interno, cujo valor é 2.
        ExpSoma soma = new ExpSoma(new Id("x"), new ValorInteiro(1));

        // --- ExpDeclaracao interna: let var x = 2 in x + 1 ---
        ExpDeclaracao expInterna = new ExpDeclaracao(declaracoesInternas, soma);

        // --- ExpDeclaracao externa: let var x = 1 in <expInterna> ---
        ExpDeclaracao expExterna = new ExpDeclaracao(declaracoesExternas, expInterna);

        // Programa é a expressão raiz
        Programa programa = new Programa(expExterna);

        executar("let var x = 1 in let var x = 2 in x + 1", programa);

        System.out.println("--------------------------------------------------");
    }
}
