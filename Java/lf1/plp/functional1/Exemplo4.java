package lf1.plp.functional1;

import java.util.ArrayList;
import java.util.List;

import lf1.plp.functional1.declaration.DecFuncao;
import lf1.plp.functional1.declaration.DeclaracaoFuncional;
import lf1.plp.functional1.expression.Aplicacao;
import lf1.plp.functional1.expression.ExpDeclaracao;
import lf1.plp.functional1.expression.IfThenElse;
import lf1.plp.functional1.util.ValorFuncao;
import lf1.plp.expressions2.expression.ExpEquals;
import lf1.plp.expressions2.expression.ExpSoma;
import lf1.plp.expressions2.expression.ExpSub;
import lf1.plp.expressions2.expression.Expressao;
import lf1.plp.expressions2.expression.Id;
import lf1.plp.expressions2.expression.ValorInteiro;

/**
 * Avalia a expressao:
 *
 *   let fun mult x y = if (x == 0) then (0) else (y + mult(x - 1, y)) in
 *     mult(3, 4)
 *
 * Calculo:
 *   mult(3,4) = 4 + mult(2,4)
 *             = 4 + 4 + mult(1,4)
 *             = 4 + 4 + 4 + mult(0,4)
 *             = 4 + 4 + 4 + 0
 * Resultado esperado: 12
 */
public class Exemplo4 {

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
        // Parametros formais de mult: x e y
        // ------------------------------------------------------------------
        Id idX = new Id("x");
        Id idY = new Id("y");

        List<Id> params = new ArrayList<Id>();
        params.add(idX);
        params.add(idY);

        // ------------------------------------------------------------------
        // Corpo recursivo: y + mult(x - 1, y)
        // ------------------------------------------------------------------

        // Argumentos da chamada recursiva: (x - 1)  e  y
        List<Expressao> argsRec = new ArrayList<Expressao>();
        argsRec.add(new ExpSub(new Id("x"), new ValorInteiro(1)));
        argsRec.add(new Id("y"));

        // Chamada recursiva: mult(x - 1, y)
        Expressao chamadaRec = new Aplicacao(new Id("mult"), argsRec);

        // Ramo else: y + mult(x - 1, y)
        Expressao ramoElse = new ExpSoma(new Id("y"), chamadaRec);

        // ------------------------------------------------------------------
        // Corpo completo de mult:
        //   if (x == 0) then (0) else (y + mult(x - 1, y))
        // ------------------------------------------------------------------
        Expressao condicao  = new ExpEquals(new Id("x"), new ValorInteiro(0));
        Expressao ramoThen  = new ValorInteiro(0);
        Expressao corpoMult = new IfThenElse(condicao, ramoThen, ramoElse);

        // ------------------------------------------------------------------
        // Declaracao: fun mult x y = <corpoMult>
        // ------------------------------------------------------------------
        ValorFuncao vfMult   = new ValorFuncao(params, corpoMult);
        DecFuncao   decMult  = new DecFuncao(new Id("mult"), vfMult);

        // ------------------------------------------------------------------
        // Corpo do let: mult(3, 4)
        // ------------------------------------------------------------------
        List<Expressao> argsMain = new ArrayList<Expressao>();
        argsMain.add(new ValorInteiro(3));
        argsMain.add(new ValorInteiro(4));
        Expressao aplicacaoMult = new Aplicacao(new Id("mult"), argsMain);

        // ------------------------------------------------------------------
        // Monta: let fun mult x y = ... in mult(3, 4)
        // ------------------------------------------------------------------
        List<DeclaracaoFuncional> decs = new ArrayList<DeclaracaoFuncional>();
        decs.add(decMult);
        Expressao letMult = new ExpDeclaracao(decs, aplicacaoMult);

        // ------------------------------------------------------------------
        // Executa o programa
        // ------------------------------------------------------------------
        Programa prog = new Programa(letMult);

        executar(
            "let fun mult x y = if (x == 0) then (0) else (y + mult(x - 1, y)) in\n" +
            "  mult(3, 4)",
            prog
        );
    }
}
