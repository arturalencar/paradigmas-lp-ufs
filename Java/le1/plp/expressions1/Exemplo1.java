package le1.plp.expressions1;

import le1.plp.expressions1.expression.ExpSoma;
import le1.plp.expressions1.expression.ExpSub;
import le1.plp.expressions1.expression.ValorInteiro;

/**
 * Atividade 1 - Linguagem de Expressão 1 (le1)
 *
 * Avalia a expressão:  4 + 12 - 3
 *
 * Árvore de expressão:
 *        ExpSub
 *       /      \
 *   ExpSoma     3
 *   /     \
 *  4      12
 *
 * Resultado esperado: (4 + 12) - 3 = 13
 */
public class Exemplo1 {

    public static void main(String[] args) {

        // Valores constantes inteiros
        ValorInteiro v4  = new ValorInteiro(4);
        ValorInteiro v12 = new ValorInteiro(12);
        ValorInteiro v3  = new ValorInteiro(3);

        // 4 + 12
        ExpSoma soma = new ExpSoma(v4, v12);

        // (4 + 12) - 3
        ExpSub sub = new ExpSub(soma, v3);

        // Programa é a expressão raiz
        Programa programa = new Programa(sub);

        System.out.println("Expressão: 4 + 12 - 3");
        System.out.println("Bem tipada: " + programa.checaTipo());
        programa.executar();
    }
}
