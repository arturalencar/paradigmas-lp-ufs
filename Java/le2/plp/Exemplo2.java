package le2.plp;

import java.util.ArrayList;
import java.util.List;

import le2.plp.expressions2.Programa;
import le2.plp.expressions2.declaration.DecVariavel;
import le2.plp.expressions2.expression.ExpDeclaracao;
import le2.plp.expressions2.expression.ExpEquals;
import le2.plp.expressions2.expression.Id;
import le2.plp.expressions2.expression.ValorInteiro;

/**
 * Atividade - Linguagem de Expressão 2 (le2)
 *
 * Avalia a expressão:
 *   let var x = 1 in
 *       let var x = 2 in x = 1
 *
 * Árvore de expressão:
 *
 *         ExpDeclaracao (externa)
 *        /                      \
 *   DecVariavel              ExpDeclaracao (interna)
 *   (x = 1)                 /                     \
 *                      DecVariavel              ExpEquals
 *                      (x = 2)                 /        \
 *                                           Id(x)    ValorInteiro(1)
 *
 * Observação: o x interno (= 2) sombreia o x externo (= 1).
 *             Logo, a igualdade x = 1 compara 2 com 1.
 *
 * Resultado esperado: false
 */
public class Exemplo2 {

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

        // --- Corpo do escopo interno: x = 1  (igualdade) ---
        // O x resolvido aqui será o do escopo interno, cujo valor é 2.
        ExpEquals igualdade = new ExpEquals(new Id("x"), new ValorInteiro(1));

        // --- ExpDeclaracao interna: let var x = 2 in x = 1 ---
        ExpDeclaracao expInterna = new ExpDeclaracao(declaracoesInternas, igualdade);

        // --- ExpDeclaracao externa: let var x = 1 in <expInterna> ---
        ExpDeclaracao expExterna = new ExpDeclaracao(declaracoesExternas, expInterna);

        // Programa é a expressão raiz
        Programa programa = new Programa(expExterna);

        System.out.println("Expressão: let var x = 1 in");
        System.out.println("               let var x = 2 in x = 1");
        try {
            boolean bemTipada = programa.checaTipo();
            System.out.println("Bem tipada: " + bemTipada);
            if (bemTipada) {
                System.out.println("Resultado: " + programa.executar());
            } else {
                System.out.println("Erro de tipo: avaliacao abortada.");
            }
        } catch (Exception e) {
            System.out.println("Excecao capturada: " + e.getMessage());
            e.printStackTrace();
        }
    }
}
