package lf1.plp.expressions2.expression;

import lf1.plp.expressions1.util.Tipo;
import lf1.plp.expressions2.memory.AmbienteCompilacao;

/**
 * Este valor primitivo encapsula um String. 
 */
public class ValorString extends ValorConcreto<String>{

		/**
	 * cria um objeto encapsulando o String fornecido
	 */
	public ValorString(String valor) {
		super(valor);
	}


	/**
	 * Retorna os tipos possiveis desta expressao.
	 *
	 * @param amb o ambiente de compilação.
	 * @return os tipos possiveis desta expressao.
	 */
	public Tipo getTipo(AmbienteCompilacao amb) {
		return Tipo.TIPO_STRING;
	}
}
