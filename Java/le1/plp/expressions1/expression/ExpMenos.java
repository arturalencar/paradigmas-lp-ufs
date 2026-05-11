package le1.plp.expressions1.expression;

import le1.plp.expressions1.util.Tipo;

/**
* Um objeto desta classe representa uma Expressao de menos unario.
*/

public class ExpMenos extends ExpUnaria{

	/**
	 * Controi uma Expressao de menos unario com expressao especificada
	 *
	 * @param exp Expressao cuja avaliacao resulta <code>ValorInteiro</code>.
	 */
	public ExpMenos(Expressao exp){
		super(exp, "-");
	}

	/**
	 * Retorna o valor da Expressao de menos unario
	 */
	public Valor avaliar(){
		return new ValorInteiro(- ((ValorInteiro)getExp().avaliar()).valor());
	}

	/**
	 * Realiza a verificacao de tipos desta expressao.
	 *
	 * @return <code>true</code> se os tipos da expressao sao validos;
	 *          <code>false</code> caso contrario.
	 */
	protected boolean checaTipoElementoTerminal() {
		return (getExp().getTipo().eInteiro());
	}

	/**
	 * Retorna os tipos possiveis desta expressao.
	 *
	 * @return os tipos possiveis desta expressao.
	 */
	public Tipo getTipo() {
		return Tipo.TIPO_INTEIRO;
	}
}
