// Alterar tudo de mapFuncao para map e de getFuncao para get
package lf1.plp.functional1.memory;

import java.util.HashMap;
import java.util.Stack;

import lf1.plp.expressions2.expression.Id;
import lf1.plp.expressions2.expression.Valor;
import lf1.plp.expressions2.memory.Contexto;
//import lf1.plp.expressions2.memory.ContextoCompilacao;
import lf1.plp.expressions2.memory.ContextoExecucao;
import lf1.plp.expressions2.memory.VariavelJaDeclaradaException;
import lf1.plp.expressions2.memory.VariavelNaoDeclaradaException;
import lf1.plp.functional1.util.ValorFuncao;

public class ContextoExecucaoFuncional
	implements AmbienteExecucaoFuncional {

	/**
	 * A pilha de blocos de funcao deste contexto.
	 */
	private Stack<HashMap<Id, ValorFuncao>> pilhaFuncao;
	private ContextoExecucao pilhaIdValor;
	private Contexto<ValorFuncao> pilhaIdValorFunc;

	/**
	 * Construtor da classe.
	 */
	public ContextoExecucaoFuncional() {
		this.pilhaFuncao = new Stack<HashMap<Id, ValorFuncao>>();
		this.pilhaIdValor = new ContextoExecucao();
		this.pilhaIdValorFunc = new Contexto<ValorFuncao>();
		// essa � mesmo a melhor solucao??
		this.pilhaIdValorFunc.setPilha(this.pilhaFuncao); // falta só esse
	}
	
	
	public ContextoExecucaoFuncional(Stack<HashMap<Id, ValorFuncao>> pilhaFuncao, ContextoExecucao pilhaIdValor, Contexto<ValorFuncao> pilhaIdValorFunc) {
		this.pilhaFuncao = pilhaFuncao;
		this.pilhaIdValor = pilhaIdValor;
		this.pilhaIdValorFunc = pilhaIdValorFunc;
	}
	
		
	public void incrementa() {
		this.pilhaIdValor.incrementa();
		pilhaFuncao.push(new HashMap<Id, ValorFuncao>());
	}

	public void restaura() {
		this.pilhaIdValor.restaura();
		pilhaFuncao.pop();
	}

	//Remover esse m�todo. J� tem em ContextoExecucao
	/**
	 * Mapeia um identificador em uma funcao.
	 *
	 * @param idArg o identificador
	 * @param funcao a funcao.
	 * @exception VariavelJaDeclaradaException se o id ja' estiver declarado.
	 */
	public void mapFuncao(Id idArg, ValorFuncao funcao)
		throws VariavelJaDeclaradaException {
        this.pilhaIdValorFunc.map(idArg, funcao);
	}

	//Remover esse m�todo. J� tem em ContextoExecucao
	/**
	 * Retorna uma funcao.
	 *
	 * @param idArg o identificador que mapeia a funcao
	 * @param funcao a funcao.
	 * @exception VariavelNaoDeclaradaException se o id nao estiver declarado.
	 */
	public ValorFuncao getFuncao(Id idArg)
		throws VariavelNaoDeclaradaException {
		return this.pilhaIdValorFunc.get(idArg);
	}

	public Valor get(Id idArg) throws VariavelNaoDeclaradaException {
		return this.pilhaIdValor.get(idArg);
	}

	public void map(Id idArg, Valor tipoId) throws VariavelJaDeclaradaException {
		this.pilhaIdValor.map(idArg, tipoId);
	}
		
	
	protected Stack<HashMap<Id, ValorFuncao>> getPilhaFuncao(){
		return pilhaFuncao;
	}
	protected ContextoExecucao getPilhaIdValor(){
		return pilhaIdValor;
	}
	protected Contexto<ValorFuncao> getPilhaIdValorFunc(){ 
		return pilhaIdValorFunc;
	}


	protected void setPilhaFuncao(Stack<HashMap<Id, ValorFuncao>> pilhaFuncao) {
		this.pilhaFuncao = pilhaFuncao;
	}


	protected void setPilhaIdValor(ContextoExecucao pilhaIdValor) {
		this.pilhaIdValor = pilhaIdValor;
	}


	protected void setPilhaIdValorFunc(Contexto<ValorFuncao> pilhaIdValorFunc) {
		this.pilhaIdValorFunc = pilhaIdValorFunc;
	}
	

}
