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

public class Exemplo1 {

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
            DecVariavelObjeto decC = new DecVariavelObjeto(
                new TipoClasse(new Id("Contador")), 
                new Id("c"), 
                new Id("Contador")
            );

            // c.inc();
            Comando cInc = new ChamadaMetodo(new Id("c"), new Id("inc"), new ListaExpressao());

            // c.print();
            Comando cPrint = new ChamadaMetodo(new Id("c"), new Id("print"), new ListaExpressao());

            // c.inc(); c.print();
            Comando incEPrint = new Sequencial(cInc, cPrint);

            // { Contador c := new Contador; c.inc(); c.print(); }
            Comando comDeclaracao = new ComDeclaracao(decC, incEPrint);

            // Programa
            Programa prog = new Programa(decClasse, comDeclaracao);

            // Executar
            executar(prog, "Contador c := new Contador; c.inc(); c.print();", new ContextoExecucaoOO1());
            
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
