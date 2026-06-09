package lf1.plp.functional1;

import java.util.ArrayList;
import java.util.List;

import lf1.plp.functional1.declaration.DecFuncao;
import lf1.plp.functional1.declaration.DecVariavel;
import lf1.plp.functional1.declaration.DeclaracaoFuncional;
import lf1.plp.functional1.expression.Aplicacao;
import lf1.plp.functional1.expression.ExpDeclaracao;
import lf1.plp.functional1.util.ValorFuncao;
import lf1.plp.expressions2.expression.ExpSoma;
import lf1.plp.expressions2.expression.Expressao;
import lf1.plp.expressions2.expression.Id;
import lf1.plp.expressions2.expression.ValorInteiro;

/**
 * Avalia a expressao aninhada:
 *
 *   let fun f x = x + 1 in
 *     let fun f y = y + x in
 *       let var x = 5 in
 *         f 1
 *
 * Resultado esperado: f 1  =>  1 + 5 = 6
 * (f do nivel 2 usa y=1 e x=5 declarado no nivel 3)
 */
public class Exemplo2 {

    static void executar(String descricao, Programa prog) {
        System.out.println("--------------------------------------------------");
        System.out.println("Expressao : " + descricao);
        try {
            boolean bemTipada = prog.checaTipo();
            System.out.println("Bem tipada: " + bemTipada);
            if (bemTipada) {
                System.out.println("Resultado : " + prog.executar());
            } else {
                System.out.println("Erro de tipo: avaliacao abortada.");
            }
        } catch (Exception e) {
            System.out.println("Excecao capturada: " + e.getMessage());
            e.printStackTrace();
        }
        System.out.println("--------------------------------------------------");
    }

    public static void main(String[] args) {

        // ------------------------------------------------------------------
        // Nivel 1: let fun f x = x + 1 in <nivel2>
        // ------------------------------------------------------------------

        // Parametro formal da funcao f do nivel 1
        Id paramX = new Id("x");
        List<Id> params1 = new ArrayList<Id>();
        params1.add(paramX);

        // Corpo de f nivel 1: x + 1
        Expressao corpof1 = new ExpSoma(new Id("x"), new ValorInteiro(1));

        // ValorFuncao e DecFuncao para f nivel 1
        ValorFuncao vf1       = new ValorFuncao(params1, corpof1);
        DecFuncao   decf1     = new DecFuncao(new Id("f"), vf1);

        // ------------------------------------------------------------------
        // Nivel 2: let fun f y = y + x in <nivel3>
        // ------------------------------------------------------------------

        // Parametro formal da funcao f do nivel 2
        Id paramY = new Id("y");
        List<Id> params2 = new ArrayList<Id>();
        params2.add(paramY);

        // Corpo de f nivel 2: y + x  (x sera resolvido em tempo de execucao)
        Expressao corpof2 = new ExpSoma(new Id("y"), new Id("x"));

        // ValorFuncao e DecFuncao para f nivel 2
        ValorFuncao vf2   = new ValorFuncao(params2, corpof2);
        DecFuncao   decf2 = new DecFuncao(new Id("f"), vf2);

        // ------------------------------------------------------------------
        // Nivel 3: let var x = 5 in f 1
        // ------------------------------------------------------------------

        // Declaracao: var x = 5
        DecVariavel decX = new DecVariavel(new Id("x"), new ValorInteiro(5));

        // Aplicacao: f 1  (chama f do nivel 2)
        List<Expressao> argF = new ArrayList<Expressao>();
        argF.add(new ValorInteiro(1));
        Expressao aplicacaoF = new Aplicacao(new Id("f"), argF);

        // ExpDeclaracao do nivel 3
        List<DeclaracaoFuncional> decs3 = new ArrayList<DeclaracaoFuncional>();
        decs3.add(decX);
        Expressao nivel3 = new ExpDeclaracao(decs3, aplicacaoF);

        // ------------------------------------------------------------------
        // Monta nivel 2 com nivel 3 como corpo
        // ------------------------------------------------------------------
        List<DeclaracaoFuncional> decs2 = new ArrayList<DeclaracaoFuncional>();
        decs2.add(decf2);
        Expressao nivel2 = new ExpDeclaracao(decs2, nivel3);

        // ------------------------------------------------------------------
        // Monta nivel 1 com nivel 2 como corpo
        // ------------------------------------------------------------------
        List<DeclaracaoFuncional> decs1 = new ArrayList<DeclaracaoFuncional>();
        decs1.add(decf1);
        Expressao nivel1 = new ExpDeclaracao(decs1, nivel2);

        // ------------------------------------------------------------------
        // Executa o programa
        // ------------------------------------------------------------------
        Programa prog = new Programa(nivel1);

        executar(
            "let fun f x = x + 1 in\n" +
            "  let fun f y = y + x in\n" +
            "    let var x = 5 in\n" +
            "      f 1",
            prog
        );
    }
}
