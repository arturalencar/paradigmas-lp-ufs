package lf1.plp.expressions2.expression;

import lf1.plp.expressions1.util.Tipo;
import lf1.plp.expressions2.memory.AmbienteCompilacao;
import lf1.plp.expressions2.memory.AmbienteExecucao;
import lf1.plp.expressions2.memory.VariavelJaDeclaradaException;
import lf1.plp.expressions2.memory.VariavelNaoDeclaradaException;

/**
 * Um objeto desta classe representa uma Expressao de Negacao logica.
 */
public class ExpNot extends ExpUnaria{

	/**
	 * Controi uma Expressao de negacao logica com expressao
	 * especificada.
	 * 
	 * @param exp Expressao a ser negada. Assume-se que sua avaliacao resulta
	 *        em <code>ValorBooleano</code>.
	 */
	public ExpNot( Expressao exp) {
		super(exp, "~");
	}

	/**
	 * Retorna o valor da Expressao de negacao logica.
	 * 
	 * @param amb o ambiente de execução.
	 * @return o valor da expressão avaliada.
	 * @exception VariavelNaoDeclaradaException se a variável não está 
	 *            declarada no ambiente. 
	 */
	public Valor avaliar(AmbienteExecucao amb) throws VariavelJaDeclaradaException, 
			VariavelNaoDeclaradaException {
		return new ValorBooleano(!((ValorBooleano) getExp().avaliar(amb)).valor());
	}

	/**
	 * Realiza a verificacao de tipos desta expressao.
	 * 
	 * @param amb o ambiente de compilação.
	 * @return <code>true</code> se os tipos da expressao sao validos;
	 *          <code>false</code> caso contrario.
	 * @exception VariavelNaoDeclaradaException se existir um identificador
	 *          nao declarado no ambiente.
	 * @exception VariavelNaoDeclaradaException se existir um identificador
	 *          declarado mais de uma vez no mesmo bloco do ambiente.
	 */
	protected boolean checaTipoElementoTerminal(AmbienteCompilacao amb) throws VariavelJaDeclaradaException, 
			VariavelNaoDeclaradaException {
		return (getExp().getTipo(amb).eBooleano());
	}

	/**
	 * Retorna os tipos possiveis desta expressao.
	 *
	 * @param amb o ambiente de compilação.
	 * @return os tipos possiveis desta expressao.
	 */
	public Tipo getTipo(AmbienteCompilacao amb) {
		return Tipo.TIPO_BOOLEANO;
	}
}
