package lf1.plp.functional1.declaration;

import lf1.plp.expressions1.util.Tipo;
import lf1.plp.expressions2.expression.Expressao;
import lf1.plp.expressions2.expression.Id;
import lf1.plp.expressions2.memory.AmbienteCompilacao;
import lf1.plp.expressions2.memory.VariavelJaDeclaradaException;
import lf1.plp.expressions2.memory.VariavelNaoDeclaradaException;

public class DecVariavel implements DeclaracaoFuncional {
	private Id id;
	private Expressao expressao;

	public DecVariavel(Id idArg, Expressao expressaoArg) {
		id = idArg;
		expressao = expressaoArg;
	}
	public int getAridade() {
		return 0;
	}

	/**
	 * Retorna uma representacao String desta expressao. Util para depuracao.
	 *
	 * @return uma representacao String desta expressao.
	 */
	public String toString() {
		StringBuffer sb = new StringBuffer();
		sb.append("var ");
		sb.append(id.toString());
		sb.append(" = ");
		sb.append(expressao.toString());
		return sb.toString();
	}

	public Expressao getExpressao() {
		return expressao;
	}

	public Id getID() {
		return id;
	}

	/**
	 * Retorna os tipos possiveis desta declaração.
	 *
	 * @param amb o ambiente que contem o mapeamento entre identificadores
	 *          e tipos.
	 * @return os tipos possiveis desta declaração.
	 * @exception VariavelNaoDeclaradaException se houver uma vari&aacute;vel
	 *          n&atilde;o declarada no ambiente.
	 * @exception VariavelJaDeclaradaException se houver uma mesma
	 *           vari&aacute;vel declarada duas vezes no mesmo bloco do
	 *           ambiente.
	 * @precondition this.checaTipo(amb);
	 */
	public Tipo getTipo(AmbienteCompilacao amb)
		throws VariavelNaoDeclaradaException, VariavelJaDeclaradaException {
		return expressao.getTipo(amb);
	}

	/**
	 * Realiza a verificacao de tipos desta declaração.
	 *
	 * @param amb o ambiente de compilação.
	 * @return <code>true</code> se os tipos da expressao sao validos;
	 *          <code>false</code> caso contrario.
	 * @exception VariavelNaoDeclaradaException se existir um identificador
	 *          nao declarado no ambiente.
	 * @exception VariavelNaoDeclaradaException se existir um identificador
	 *          declarado mais de uma vez no mesmo bloco do ambiente.
	 */
	public boolean checaTipo(AmbienteCompilacao ambiente)
		throws VariavelNaoDeclaradaException, VariavelJaDeclaradaException {
		return expressao.checaTipo(ambiente);
	}

}
