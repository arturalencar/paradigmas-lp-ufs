package le2.plp.expressions2.expression;

import le2.plp.expressions1.util.Tipo;
import le2.plp.expressions2.memory.AmbienteCompilacao;
import le2.plp.expressions2.memory.AmbienteExecucao;
import le2.plp.expressions2.memory.VariavelNaoDeclaradaException;

public class Id implements Expressao {

	private String  idName;

	public Id(String strName) {
		idName =  strName;
	}

	public boolean equals(Object obj) {
		if (obj instanceof Id) {
			return ((Id) obj).idName.equals(this.idName);
		}
		return false;
	}

	public int hashCode() {
		return idName.hashCode();
	}

	public String toString() {
		return idName;
	}

	public Valor avaliar(AmbienteExecucao ambiente) throws VariavelNaoDeclaradaException {
		return ambiente.get(this);
	}

	/**
	 * Realiza a verificacao de tipos desta expressao.
	 * Ser&aacute; v&aacute;lida se o identificador estiver declarado.
	 *
	 * @param amb o ambiente de compila��o.
	 * @return <code>true</code> se os tipos da expressao sao validos;
	 *          <code>false</code> caso contrario.
	 * @exception VariavelNaoDeclaradaException se este identificador nao
	 *          estiver no ambiente.
	 */
	public boolean checaTipo(AmbienteCompilacao amb) throws VariavelNaoDeclaradaException {
		boolean result = true;
		//Tipo t = amb.get(this); // se estiver no ambiente, entao esta ok.
		return result;
	}

	/**
	 * Retorna os tipos possiveis desta expressao.
	 *
	 * @param amb o ambiente de compila��o.
	 * @return os tipos possiveis desta expressao.
	 * @exception VariavelNaoDeclaradaException se este identificador nao
	 *          estiver no ambiente.
	 */
	public Tipo getTipo(AmbienteCompilacao amb) throws VariavelNaoDeclaradaException {
		return amb.get(this);
	}

	public String getIdName() {
		return idName;
	}

	public void setIdName(String idName) {
		this.idName = idName;
	}

}
