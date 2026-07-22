package plp.orientadaObjetos1;

import plp.orientadaObjetos1.comando.*;
import plp.orientadaObjetos1.declaracao.classe.*;
import plp.orientadaObjetos1.declaracao.procedimento.*;
import plp.orientadaObjetos1.declaracao.variavel.*;
import plp.orientadaObjetos1.expressao.*;
import plp.orientadaObjetos1.expressao.binaria.*;
import plp.orientadaObjetos1.expressao.leftExpression.*;
import plp.orientadaObjetos1.expressao.valor.*;
import plp.orientadaObjetos1.memoria.*;
import plp.orientadaObjetos1.memoria.colecao.ListaValor;
import plp.orientadaObjetos1.util.*;

public class Exemplo2 {

    public static void executar(Programa prog, String descricao, ContextoExecucaoOO1 ambiente) {
        System.out.println("--------------------------------------------------");
        System.out.println("Programa: \n" + descricao + "\n");
        try {
            boolean bemTipado = prog.checaTipo(new ContextoCompilacaoOO1(new ListaValor()));
            System.out.println("Bem tipado: " + bemTipado);
            if (bemTipado) {
                ListaValor saida = prog.executar(ambiente);
                System.out.print("Saida: ");
                while (saida.length() > 0) {
                    System.out.print(saida.getHead() + " ");
                    saida = (ListaValor) saida.getTail();
                }
                System.out.println();
            } else {
                System.out.println("Erro de tipo: execucao abortada.");
            }
        } catch (Exception e) {
            System.out.println("Excecao capturada: " + e.getMessage());
            e.printStackTrace();
        }
        System.out.println("--------------------------------------------------");
    }

    public static void main(String[] args) {
        try {
            // int valor = 1;
            DecVariavel decValor = new SimplesDecVariavel(
                new TipoPrimitivo(TipoPrimitivo.INTEIRO), 
                new Id("valor"), 
                new ValorInteiro(1)
            );

            // proc print() { write(this.valor) }
            Comando writeValor = new Write(new AcessoAtributoThis(new This(), new Id("valor")));
            DecProcedimento procPrint = new DecProcedimentoSimples(
                new Id("print"), 
                new ListaDeclaracaoParametro(), 
                writeValor
            );

            // proc inc() { this.valor := this.valor + 1 }
            Comando incValor = new Atribuicao(
                new AcessoAtributoThis(new This(), new Id("valor")), 
                new ExpSoma(new AcessoAtributoThis(new This(), new Id("valor")), new ValorInteiro(1))
            );
            DecProcedimento procInc = new DecProcedimentoSimples(
                new Id("inc"), 
                new ListaDeclaracaoParametro(), 
                incValor
            );

            // proc print(), proc inc()
            DecProcedimento decProcedimentos = new DecProcedimentoComposta(procPrint, procInc);

            // classe Contador { ... }
            DecClasse decClasse = new DecClasseSimples(
                new Id("Contador"), 
                decValor, 
                decProcedimentos
            );

            // Contador c := new Contador;
            DecVariavelObjeto decC1 = new DecVariavelObjeto(
                new TipoClasse(new Id("Contador")), 
                new Id("c"), 
                new Id("Contador")
            );

            // Contador c2 := new Contador;
            DecVariavelObjeto decC2 = new DecVariavelObjeto(
                new TipoClasse(new Id("Contador")), 
                new Id("c2"), 
                new Id("Contador")
            );

            // Contador c := new Contador, Contador c2 := new Contador;
            DecVariavel decComposta = new CompostaDecVariavel(decC1, decC2);

            // c.inc();
            Comando cInc = new ChamadaMetodo(new Id("c"), new Id("inc"), new ListaExpressao());

            // c2.inc();
            Comando c2Inc1 = new ChamadaMetodo(new Id("c2"), new Id("inc"), new ListaExpressao());

            // c2.inc();
            Comando c2Inc2 = new ChamadaMetodo(new Id("c2"), new Id("inc"), new ListaExpressao());

            // c.print();
            Comando cPrint = new ChamadaMetodo(new Id("c"), new Id("print"), new ListaExpressao());

            // c2.print()
            Comando c2Print = new ChamadaMetodo(new Id("c2"), new Id("print"), new ListaExpressao());

            // Sequencia de chamadas:
            // c.inc(); c2.inc();
            Comando seq1 = new Sequencial(cInc, c2Inc1);
            // ... c2.inc();
            Comando seq2 = new Sequencial(seq1, c2Inc2);
            // ... c.print();
            Comando seq3 = new Sequencial(seq2, cPrint);
            // ... c2.print()
            Comando seq4 = new Sequencial(seq3, c2Print);

            // { Contador c := new Contador, Contador c2 := new Contador; c.inc(); c2.inc(); c2.inc(); c.print(); c2.print() }
            Comando comDeclaracao = new ComDeclaracao(decComposta, seq4);

            // Programa
            Programa prog = new Programa(decClasse, comDeclaracao);

            // Executar
            executar(prog, "Contador c := new Contador, Contador c2 := new Contador;\nc.inc();\nc2.inc();\nc2.inc();\nc.print();\nc2.print()", new ContextoExecucaoOO1());
            
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
