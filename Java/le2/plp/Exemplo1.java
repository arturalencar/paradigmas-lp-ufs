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

public class Exemplo1 {

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
        DecVariavel decX = new DecVariavel(new Id("x"), new ValorInteiro(1));
        List<DecVariavel> decs = new ArrayList<DecVariavel>();
        decs.add(decX);
        
        Expressao corpo  = new ExpSoma(new Id("x"), new ValorInteiro(1));
        Expressao let    = new ExpDeclaracao(decs, corpo);
        Programa prog    = new Programa(let);

        executar("let var x = 1 in x + 1", prog);

        System.out.println("--------------------------------------------------");
    }
}