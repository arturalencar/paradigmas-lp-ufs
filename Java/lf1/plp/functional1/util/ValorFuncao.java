package lf1.plp.functional1.util;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

import lf1.plp.expressions1.util.Tipo;
import lf1.plp.expressions2.expression.Expressao;
import lf1.plp.expressions2.expression.Id;
import lf1.plp.expressions2.memory.AmbienteCompilacao;
import lf1.plp.expressions2.memory.VariavelJaDeclaradaException;
import lf1.plp.expressions2.memory.VariavelNaoDeclaradaException;

public class ValorFuncao {

	private List<Id> argsId;

	private Expressao exp;

	public ValorFuncao(List<Id> argsId, Expressao exp) {
		this.argsId = argsId;
		this.exp = exp;
	}

	public List<Id> getListaId() {
		return argsId;
	}

	public Expressao getExp() {
		return exp;
	}

	/**
	 * Retorna a aridade desta funcao.
	 *
	 * @return a aridade desta funcao.
	 */
	public int getAridade() {
		return argsId.size();
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
		ambiente.incrementa();
		Tipo t = getTipo(ambiente);
		for (Id id : argsId) {
			ambiente.map(id, new Tipo(t.get()));
			t = t.getProx();
		}

		ambiente.restaura();
		return true;
	}

	/**
	 * Retorna os tipos possiveis desta função.
	 *
	 * @param amb o ambiente que contem o mapeamento entre identificadores
	 *          e tipos.
	 * @return os tipos possiveis desta declaração.
	 * @exception VariavelNaoDeclaradaException se houver uma vari&aacute;vel
	 *          n&atilde;o declarada no ambiente.
	 * @exception VariavelJaDeclaradaException se houver uma mesma
	 *           vari&aacute;vel declarada duas vezes no mesmo bloco do
	 *           ambiente.
	 * @precondition exp.checaTipo();
	 */
	public Tipo getTipo(AmbienteCompilacao ambiente)
		throws VariavelNaoDeclaradaException, VariavelJaDeclaradaException {
		Map<Id, Tipo> mapIdTipo = new HashMap<Id, Tipo>();
		Id[] idsArg = new Id[argsId.size()];

		int i = 0;
		for (Id id : argsId) {
			mapIdTipo.put(id, new Tipo());
			idsArg[i++] = id;
		}

		RestrictTypesVisitor.visit(exp, ambiente, mapIdTipo, new Tipo());

		ambiente.incrementa();
		for (Id id : mapIdTipo.keySet()) {
			ambiente.map(id, mapIdTipo.get(id));
		}

		Tipo result = exp.getTipo(ambiente);
		for (i = argsId.size() - 1; i >= 0; i--) {
			result =
				new Tipo(((Tipo) mapIdTipo.get(idsArg[i])).get(), result);
		}
		ambiente.restaura();
		return result;
	}
}
