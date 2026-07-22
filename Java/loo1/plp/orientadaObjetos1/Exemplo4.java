package plp.orientadaObjetos1;

import plp.orientadaObjetos1.comando.*;
import plp.orientadaObjetos1.declaracao.classe.*;
import plp.orientadaObjetos1.declaracao.procedimento.*;
import plp.orientadaObjetos1.declaracao.variavel.*;
import plp.orientadaObjetos1.expressao.*;
import plp.orientadaObjetos1.expressao.binaria.*;
import plp.orientadaObjetos1.expressao.unaria.*;
import plp.orientadaObjetos1.expressao.leftExpression.*;
import plp.orientadaObjetos1.expressao.valor.*;
import plp.orientadaObjetos1.memoria.*;
import plp.orientadaObjetos1.memoria.colecao.ListaValor;
import plp.orientadaObjetos1.util.*;

public class Exemplo4 {

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
            // Id LValor
            Id idLValor = new Id("LValor");
            Tipo tipoLValor = new TipoClasse(idLValor);

            // int valor = -100
            DecVariavel decValor = new SimplesDecVariavel(
                new TipoPrimitivo(TipoPrimitivo.INTEIRO), 
                new Id("valor"), 
                new ValorInteiro(-100)
            );

            // LValor prox = null
            DecVariavel decProx = new SimplesDecVariavel(
                tipoLValor, 
                new Id("prox"), 
                new ValorNull()
            );

            // CompostaDecVariavel(decValor, decProx)
            DecVariavel decVariaveis = new CompostaDecVariavel(decValor, decProx);

            // proc insere(int v) { ... }
            Id idV = new Id("v");
            ListaDeclaracaoParametro paramV = new ListaDeclaracaoParametro(
                new DecParametro(idV, new TipoPrimitivo(TipoPrimitivo.INTEIRO))
            );

            // if ((this).valor == -100)
            Expressao condInsere = new ExpEquals(
                new AcessoAtributoThis(new This(), new Id("valor")), 
                new ValorInteiro(-100)
            );

            // then { this.valor := v; this.prox := new LValor }
            Comando thisValorV = new Atribuicao(new AcessoAtributoThis(new This(), new Id("valor")), idV);
            Comando thisProxNew = new New(new AcessoAtributoThis(new This(), new Id("prox")), idLValor);
            Comando thenInsere = new Sequencial(thisValorV, thisProxNew);

            // else { (this).prox.insere(v) }
            ListaExpressao argV = new ListaExpressao(idV);
            Comando elseInsere = new ChamadaMetodo(new AcessoAtributoThis(new This(), new Id("prox")), new Id("insere"), argV);

            Comando ifInsere = new IfThenElse(condInsere, thenInsere, elseInsere);
            DecProcedimento procInsere = new DecProcedimentoSimples(new Id("insere"), paramV, ifInsere);

            // proc remove(int v) { ... }
            // LValor aux = this;
            DecVariavel decAux = new SimplesDecVariavel(tipoLValor, new Id("aux"), new This());

            // aux.prox
            Expressao auxProx = new AcessoAtributoId(new Id("aux"), new Id("prox"));

            // (aux.prox == null)
            Expressao auxProxIsNull = new ExpEquals(auxProx, new ValorNull());

            // ((aux).prox).valor
            Expressao auxProxValor = new AcessoAtributoId(new AcessoAtributoId(new Id("aux"), new Id("prox")), new Id("valor"));

            // (((aux).prox).valor == v)
            Expressao auxProxValorEqualsV = new ExpEquals(auxProxValor, idV);

            // (aux.prox == null) or (((aux).prox).valor == v)
            Expressao condOr = new ExpOr(auxProxIsNull, auxProxValorEqualsV);

            // not((aux.prox == null) or (((aux).prox).valor == v))
            Expressao condWhile = new ExpNot(condOr);

            // do { aux := aux.prox }
            Comando auxAssignAuxProx = new Atribuicao(new Id("aux"), auxProx);
            Comando whileCmd = new While(condWhile, auxAssignAuxProx);

            // if ( not( aux.prox == null) )
            Expressao ifCond = new ExpNot(auxProxIsNull);

            // then { aux.prox := ((aux).prox).prox }
            Expressao auxProxProx = new AcessoAtributoId(new AcessoAtributoId(new Id("aux"), new Id("prox")), new Id("prox"));
            Comando thenIf = new Atribuicao(new AcessoAtributoId(new Id("aux"), new Id("prox")), auxProxProx);

            // else { skip }
            Comando elseIf = new Skip();

            Comando ifCmd = new IfThenElse(ifCond, thenIf, elseIf);

            // Sequencial whileCmd ; ifCmd
            Comando seqRemove = new Sequencial(whileCmd, ifCmd);

            Comando corpoRemove = new ComDeclaracao(decAux, seqRemove);
            DecProcedimento procRemove = new DecProcedimentoSimples(new Id("remove"), paramV, corpoRemove);

            // proc print() { ... }
            Comando writeValor = new Write(new AcessoAtributoThis(new This(), new Id("valor")));

            // if (not(this.prox == null))
            Expressao proxNull = new ExpEquals(new AcessoAtributoThis(new This(), new Id("prox")), new ValorNull());
            Expressao condPrint = new ExpNot(proxNull);

            // then { (this).prox.print() }
            Comando thenPrint = new ChamadaMetodo(new AcessoAtributoThis(new This(), new Id("prox")), new Id("print"), new ListaExpressao());

            // else { skip }
            Comando elsePrint = new Skip();

            Comando ifPrint = new IfThenElse(condPrint, thenPrint, elsePrint);
            Comando corpoPrint = new Sequencial(writeValor, ifPrint);

            DecProcedimento procPrint = new DecProcedimentoSimples(new Id("print"), new ListaDeclaracaoParametro(), corpoPrint);

            DecProcedimento decProcedimentos = new DecProcedimentoComposta(
                procInsere, 
                new DecProcedimentoComposta(procRemove, procPrint)
            );

            DecClasse decClasse = new DecClasseSimples(idLValor, decVariaveis, decProcedimentos);

            // Bloco Principal
            // LValor lv := new LValor;
            DecVariavelObjeto decLv = new DecVariavelObjeto(tipoLValor, new Id("lv"), idLValor);

            // lv.insere(2);
            Comando lvInsere2 = new ChamadaMetodo(new Id("lv"), new Id("insere"), new ListaExpressao(new ValorInteiro(2)));

            // lv.insere(3);
            Comando lvInsere3 = new ChamadaMetodo(new Id("lv"), new Id("insere"), new ListaExpressao(new ValorInteiro(3)));

            // lv.insere(4);
            Comando lvInsere4 = new ChamadaMetodo(new Id("lv"), new Id("insere"), new ListaExpressao(new ValorInteiro(4)));

            // lv.print();
            Comando lvPrint1 = new ChamadaMetodo(new Id("lv"), new Id("print"), new ListaExpressao());
            
            // lv.remove(3);
            Comando lvRemove3 = new ChamadaMetodo(new Id("lv"), new Id("remove"), new ListaExpressao(new ValorInteiro(3)));

            // lv.print();
            Comando lvPrint2 = new ChamadaMetodo(new Id("lv"), new Id("print"), new ListaExpressao());

            // Sequencia principal
            Comando seqPrin1 = new Sequencial(lvInsere2, lvInsere3);
            Comando seqPrin2 = new Sequencial(seqPrin1, lvInsere4);
            Comando seqPrin3 = new Sequencial(seqPrin2, lvPrint1);
            Comando seqPrin4 = new Sequencial(seqPrin3, lvRemove3);
            Comando seqPrin5 = new Sequencial(seqPrin4, lvPrint2);

            Comando comDeclaracao = new ComDeclaracao(decLv, seqPrin5);
            Programa prog = new Programa(decClasse, comDeclaracao);

            // Executar
            executar(prog, "LValor lv := new LValor;\nlv.insere(2); lv.insere(3);\nlv.insere(4); lv.print();\nlv.remove(3); lv.print()", new ContextoExecucaoOO1());
            
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
