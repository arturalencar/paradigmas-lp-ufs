package lf1.plp.functional1.expression;

import lf1.plp.expressions1.util.Tipo;
import lf1.plp.expressions2.expression.Expressao;
import lf1.plp.expressions2.expression.Valor;
import lf1.plp.expressions2.expression.ValorBooleano;
import lf1.plp.expressions2.memory.AmbienteCompilacao;
import lf1.plp.expressions2.memory.AmbienteExecucao;
import lf1.plp.expressions2.memory.VariavelJaDeclaradaException;
import lf1.plp.expressions2.memory.VariavelNaoDeclaradaException;

public class IfThenElse implements Expressao {
	Expressao condicao;
	Expressao then;
	Expressao elseExpressao;

	public IfThenElse(
		Expressao teste,
		Expressao thenExpressao,
		Expressao elseExpressao) {
		this.condicao = teste;
		this.then = thenExpressao;
		this.elseExpressao = elseExpressao;
	}

	public Valor avaliar(AmbienteExecucao ambiente)
		throws VariavelNaoDeclaradaException, VariavelJaDeclaradaException {
		if (((ValorBooleano) condicao.avaliar(ambiente)).valor())
			return then.avaliar(ambiente);
		else
			return elseExpressao.avaliar(ambiente);
	}

	/**
	 * Retorna texto representando um objeto desta classe.
	 */
	public String toString() {
		StringBuffer sb = new StringBuffer();
		sb.append("if (");
		sb.append(condicao.toString());
		sb.append(") then (");
		sb.append(then.toString());
		sb.append(") else (");
		sb.append(elseExpressao.toString());
		sb.append(")");
		return sb.toString();
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
	public boolean checaTipo(AmbienteCompilacao amb)
		throws VariavelNaoDeclaradaException, VariavelJaDeclaradaException {
		boolean result = true;
		if (!condicao.getTipo(amb).eBooleano()) {
			result = false;
		} else if (
			then.getTipo(amb).intersecao(elseExpressao.getTipo(amb)).eVoid()) {
			result = false;
		}
		return result;
	}

	/**
	 * Retorna os tipos possiveis desta expressao.
	 *
	 * @param amb o ambiente de compilação.
	 * @return os tipos possiveis desta expressao.
	 * @exception VariavelNaoDeclaradaException se existir um identificador
	 *          nao declarado no ambiente.
	 * @exception VariavelNaoDeclaradaException se existir um identificador
	 *          declarado mais de uma vez no mesmo bloco do ambiente.
	 */
	public Tipo getTipo(AmbienteCompilacao amb)
		throws VariavelNaoDeclaradaException, VariavelJaDeclaradaException {
		return then.getTipo(amb).intersecao(elseExpressao.getTipo(amb));
	}

	/**
	 * Returns the condicao.
	 * @return Expressao
	 */
	public Expressao getCondicao() {
		return condicao;
	}

	/**
	 * Returns the then.
	 * @return Expressao
	 */
	public Expressao getThen() {
		return then;
	}

	/**
	 * Returns the elseExpressao.
	 * @return Expressao
	 */
	public Expressao getElseExpressao() {
		return elseExpressao;
	}

}
