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
import lf1.plp.expressions2.expression.ValorString;

/**
 * Avalia a expressao aninhada:
 *
 *   let var y = 3 in
 *     let fun f x = x + y in
 *       let var z = 'abc' in
 *         f 3
 *
 * Resultado esperado: f 3  =>  x + y = 3 + 3 = 6
 * (z = 'abc' e declarada mas nao e usada na aplicacao f 3)
 */
public class Exemplo3 {

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
        // Nivel 1: let var y = 3 in <nivel2>
        // ------------------------------------------------------------------

        // Declaracao: var y = 3
        DecVariavel decY = new DecVariavel(new Id("y"), new ValorInteiro(3));

        // ------------------------------------------------------------------
        // Nivel 2: let fun f x = x + y in <nivel3>
        // ------------------------------------------------------------------

        // Parametro formal da funcao f: x
        Id paramX = new Id("x");
        List<Id> params = new ArrayList<Id>();
        params.add(paramX);

        // Corpo de f: x + y  (y sera resolvido no ambiente do nivel 1)
        Expressao corpof = new ExpSoma(new Id("x"), new Id("y"));

        // ValorFuncao e DecFuncao para f
        ValorFuncao vf   = new ValorFuncao(params, corpof);
        DecFuncao   decf = new DecFuncao(new Id("f"), vf);

        // ------------------------------------------------------------------
        // Nivel 3: let var z = 'abc' in f 3
        // ------------------------------------------------------------------

        // Declaracao: var z = "abc"
        DecVariavel decZ = new DecVariavel(new Id("z"), new ValorString("abc"));

        // Aplicacao: f 3  (chama f do nivel 2)
        List<Expressao> argF = new ArrayList<Expressao>();
        argF.add(new ValorInteiro(3));
        Expressao aplicacaoF = new Aplicacao(new Id("f"), argF);

        // ExpDeclaracao do nivel 3
        List<DeclaracaoFuncional> decs3 = new ArrayList<DeclaracaoFuncional>();
        decs3.add(decZ);
        Expressao nivel3 = new ExpDeclaracao(decs3, aplicacaoF);

        // ------------------------------------------------------------------
        // Monta nivel 2 com nivel 3 como corpo
        // ------------------------------------------------------------------
        List<DeclaracaoFuncional> decs2 = new ArrayList<DeclaracaoFuncional>();
        decs2.add(decf);
        Expressao nivel2 = new ExpDeclaracao(decs2, nivel3);

        // ------------------------------------------------------------------
        // Monta nivel 1 com nivel 2 como corpo
        // ------------------------------------------------------------------
        List<DeclaracaoFuncional> decs1 = new ArrayList<DeclaracaoFuncional>();
        decs1.add(decY);
        Expressao nivel1 = new ExpDeclaracao(decs1, nivel2);

        // ------------------------------------------------------------------
        // Executa o programa
        // ------------------------------------------------------------------
        Programa prog = new Programa(nivel1);

        executar(
            "let var y = 3 in\n" +
            "  let fun f x = x + y in\n" +
            "    let var z = 'abc' in\n" +
            "      f 3",
            prog
        );
    }
}
