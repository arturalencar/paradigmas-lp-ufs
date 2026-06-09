package lf1.plp.expressions2.expression;

import lf1.plp.expressions1.util.Tipo;
import lf1.plp.expressions2.memory.AmbienteCompilacao;
import lf1.plp.expressions2.memory.AmbienteExecucao;
import lf1.plp.expressions2.memory.VariavelJaDeclaradaException;
import lf1.plp.expressions2.memory.VariavelNaoDeclaradaException;

/**
 * Um objeto desta classe representa uma Expressao de Igualdade entre 
 * Expressoes cuja avaliacao resulta num mesmo valor primitivo.
 */
public class ExpEquals extends ExpBinaria{

	/**
	 * Controi uma Expressao de Igualdade com as sub-expressoes especificadas.
	 * Assume-se que estas sub-expressoes resultam num mesmo valor primitivo
	 * quando avaliadas.
	 * @param esq Expressao da esquerda
	 * @param dir Expressao da direita
	 */
	public ExpEquals(Expressao esq, Expressao dir){
		super(esq, dir, "==");
	}

	/**
	 * Retorna o valor da Expressao de Igualdade
	 */
	public Valor avaliar(AmbienteExecucao amb) throws VariavelNaoDeclaradaException, VariavelJaDeclaradaException {
		return(
			new ValorBooleano(((ValorConcreto)getEsq().avaliar(amb)).isEquals((ValorConcreto)getDir().avaliar(amb)))
		);
	}

	/**
	 * Realiza a verificacao de tipos desta expressao.
	 *
	 * @param ambiente o ambiente de compila��o.
	 * @return <code>true</code> se os tipos da expressao sao validos;
	 *          <code>false</code> caso contrario.
	 * @exception VariavelNaoDeclaradaException se existir um identificador
	 *          nao declarado no ambiente.
	 * @exception VariavelNaoDeclaradaException se existir um identificador
	 *          declarado mais de uma vez no mesmo bloco do ambiente.
	 */
	protected boolean checaTipoElementoTerminal(AmbienteCompilacao ambiente)
			throws VariavelNaoDeclaradaException, VariavelJaDeclaradaException {
		return !getEsq().getTipo(ambiente).intersecao(getDir().getTipo(ambiente)).eVoid();
		//return (getEsq().getTipo(ambiente).equals(getDir().getTipo(ambiente)));
	}

	/**
	 * Retorna os tipos possiveis desta expressao.
	 *
	 * @param ambiente o ambiente de compila��o.
	 * @return os tipos possiveis desta expressao.
	 */
	public Tipo getTipo(AmbienteCompilacao ambiente) {
		return Tipo.TIPO_BOOLEANO;
	}

}
