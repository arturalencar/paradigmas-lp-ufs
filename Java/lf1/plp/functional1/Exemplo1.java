package lf1.plp.functional1;

import java.util.ArrayList;
import java.util.List;

import lf1.plp.functional1.declaration.DecFuncao;
import lf1.plp.functional1.declaration.DeclaracaoFuncional;
import lf1.plp.functional1.expression.Aplicacao;
import lf1.plp.functional1.expression.ExpDeclaracao;
import lf1.plp.functional1.util.ValorFuncao;
import lf1.plp.functional1.memory.AmbienteExecucaoFuncional;
import lf1.plp.functional1.memory.ContextoExecucaoFuncional;
import lf1.plp.expressions2.expression.ExpSoma;
import lf1.plp.expressions2.expression.Expressao;
import lf1.plp.expressions2.expression.Id;
import lf1.plp.expressions2.expression.ValorInteiro;
import lf1.plp.expressions2.memory.AmbienteCompilacao;
import lf1.plp.expressions2.memory.ContextoCompilacao;

/**
 * Atividade 1 - lf1
 *
 * Avalia a expressão:
 *   let fun f x = x + 1 in f(2)
 *
 * Árvore:
 *   ExpDeclaracao
 *     DecFuncao: fun f [x] = ExpSoma(Id("x"), ValorInteiro(1))
 *     corpo:     Aplicacao( Id("f"), [ValorInteiro(2)] )
 *
 * Rastreamento:
 *   - Declara f com parâmetro x e corpo x+1
 *   - Aplica f(2): cria escopo com x=2, avalia x+1 = 3
 *
 * Resultado esperado: 3
 *
 * Classes de memória utilizadas:
 *   - AmbienteCompilacao / ContextoCompilacao : ambiente de checagem de tipos
 *   - AmbienteExecucaoFuncional / ContextoExecucaoFuncional : ambiente de execução
 *     que suporta mapeamento de funções (mapFuncao / getFuncao) além de variáveis
 */
public class Exemplo1 {

    /**
     * Executa a checagem de tipos e a avaliação da expressão usando os ambientes
     * de memória passados explicitamente.
     *
     * @param descricao texto descritivo da expressão
     * @param exp       expressão a ser avaliada
     * @param ambC      ambiente de compilação (checagem de tipos)
     * @param ambE      ambiente de execução funcional
     */
    static void executar(String descricao,
                         Expressao exp,
                         AmbienteCompilacao ambC,
                         AmbienteExecucaoFuncional ambE) {
        System.out.println("--------------------------------------------------");
        System.out.println("Expressao : " + descricao);
        try {
            // Fase 1 – checagem de tipos usando AmbienteCompilacao (ContextoCompilacao)
            boolean bemTipada = exp.checaTipo(ambC);
            System.out.println("Bem tipada: " + bemTipada);

            if (bemTipada) {
                // Fase 2 – avaliação usando AmbienteExecucaoFuncional (ContextoExecucaoFuncional)
                // O ContextoExecucaoFuncional mantém:
                //   - pilhaIdValor   : mapeamento Id -> Valor (variáveis)
                //   - pilhaIdValorFunc: mapeamento Id -> ValorFuncao (funções)
                System.out.println("Resultado : " + exp.avaliar(ambE));
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

        // ── ValorFuncao: parametros e corpo de f ─────────────
        List<Id> params = new ArrayList<Id>();
        params.add(new Id("x"));
        Expressao corpo = new ExpSoma(new Id("x"), new ValorInteiro(1));
        ValorFuncao vf = new ValorFuncao(params, corpo);

        // ── DecFuncao: fun f x = x + 1 ──────────────────────
        DecFuncao decF = new DecFuncao(new Id("f"), vf);

        // ── Corpo do let: f(2) ───────────────────────────────
        List<Expressao> argF = new ArrayList<Expressao>();
        argF.add(new ValorInteiro(2));
        Aplicacao chamadaF = new Aplicacao(new Id("f"), argF);

        // ── Bloco: let fun f x = x+1 in f(2) ────────────────
        List<DeclaracaoFuncional> decs = new ArrayList<DeclaracaoFuncional>();
        decs.add(decF);
        Expressao let = new ExpDeclaracao(decs, chamadaF);

        // ── Instanciação explícita dos ambientes de memória ──
        // ContextoCompilacao: implementa AmbienteCompilacao
        //   -> usado em checaTipo() para registrar e consultar tipos de variáveis
        AmbienteCompilacao ambC = new ContextoCompilacao();

        // ContextoExecucaoFuncional: implementa AmbienteExecucaoFuncional
        //   -> estende AmbienteExecucao com suporte a funções (mapFuncao/getFuncao)
        //   -> internamente usa pilhaIdValor (variáveis) e pilhaIdValorFunc (funções)
        AmbienteExecucaoFuncional ambE = new ContextoExecucaoFuncional();

        executar("let fun f x = x + 1 in f(2)", let, ambC, ambE);
    }
}