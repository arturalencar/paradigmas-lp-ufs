package le1.plp.expressions1.expression;

import le1.plp.expressions1.util.Tipo;

/**
 * Um objeto desta classe representa uma Disjuncao Logica.
 */
public class ExpOr extends ExpBinaria {

	/**
	 * Controi uma Expressao de disjuncao logica  com as sub-expressoes
	 * especificadas.Estas devem ser tais que sua avaliacao resulta em
	 * <code>ValorBooleano</code>
	 *
	 * @param esq Expressao da esquerda
	 * @param dir Expressao da direita
	 */
	public ExpOr(Expressao esq, Expressao dir){
		super(esq, dir, "or");
	}


	/**
	 * Retorna o valor da Expressao de disjuncao logica
	 */
	public Valor avaliar(){
	return new ValorBooleano(
				((ValorBooleano)getEsq().avaliar()).valor() ||
				((ValorBooleano)getDir().avaliar()).valor() );
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
