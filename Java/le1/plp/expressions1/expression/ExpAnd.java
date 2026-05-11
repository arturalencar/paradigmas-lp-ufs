package le1.plp.expressions1.expression;

import le1.plp.expressions1.util.Tipo;

/**
 * Um objeto desta classe representa uma Expressao de Conjuncao logica.
 */
public class ExpAnd extends ExpBinaria{

	/**
	 * Controi uma Expressao de Conjuncao logica  com as sub-expressoes
	 * especificadas. Estas devem ser tais que sua avaliacao retorna
	 * <code>ValorBooleano</code>
	 *
	 * @param esq Expressao da esquerda
	 * @param dir Expressao da direita
	 */
	public ExpAnd(Expressao esq, Expressao dir) {
		super(esq, dir, "and");
	}


	/**
	 * Retorna o valor da Expressao de Conjuncao Logica
	 */
	 public Valor avaliar(){
		return new ValorBooleano(
					((ValorBooleano)getEsq().avaliar()).valor() &&
					((ValorBooleano)getDir().avaliar()).valor()
		);
	}
 
	/**
	 * Realiza a verificacao de tipos desta expressao.
	 *
	 * @return <code>true</code> se os tipos da expressao sao validos;
	 *          <code>false</code> caso contrario.
	 */
	protected boolean checaTipoElementoTerminal() {
		return (getEsq().getTipo().eBooleano() && getDir().getTipo().eBooleano());
	}

	/**
	 * Retorna os tipos possiveis desta expressao.
	 *
	 * @return os tipos possiveis desta expressao.
	 */
	public Tipo getTipo() {
		return Tipo.TIPO_BOOLEANO;
	}

}
