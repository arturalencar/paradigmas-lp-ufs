//Mudar o for do iterator para o novo for.
package lf1.plp.functional1.expression;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

import lf1.plp.expressions1.util.Tipo;
import lf1.plp.expressions2.expression.Expressao;
import lf1.plp.expressions2.expression.Id;
import lf1.plp.expressions2.expression.Valor;
import lf1.plp.expressions2.memory.AmbienteCompilacao;
import lf1.plp.expressions2.memory.AmbienteExecucao;
import lf1.plp.expressions2.memory.VariavelJaDeclaradaException;
import lf1.plp.expressions2.memory.VariavelNaoDeclaradaException;
import lf1.plp.functional1.declaration.DecFuncao;
import lf1.plp.functional1.declaration.DeclaracaoFuncional;
import lf1.plp.functional1.memory.AmbienteExecucaoFuncional;
import lf1.plp.functional1.util.ValorFuncao;

public class ExpDeclaracao implements Expressao {

	List<DeclaracaoFuncional> seqdecFuncional;
	Expressao expressao;

	public ExpDeclaracao(List<DeclaracaoFuncional> declaracoesFuncionais, Expressao expressaoArg) {
		seqdecFuncional = declaracoesFuncionais;
		expressao = expressaoArg;
	}

	/**
	 * Retorna uma representacao String desta expressao. Util para depuracao.
	 *
	 * @return uma representacao String desta expressao.
	 */
	public String toString() {
		StringBuffer sb = new StringBuffer();
		sb.append("let ");
		sb.append(seqdecFuncional.toString());
		sb.append("\nin\n");
		sb.append(expressao.toString());
		return sb.toString();
	}

	public Valor avaliar(AmbienteExecucao ambienteFuncional)
		throws VariavelNaoDeclaradaException, VariavelJaDeclaradaException {
		AmbienteExecucaoFuncional ambiente =
			(AmbienteExecucaoFuncional) ambienteFuncional;
		ambiente.incrementa();

		// Como declaracoes feitas neste nivel nao devem ter influencia
		// mutua, armazenamos os valores em uma tabela auxiliar, para depois
		// fazer o mapeamento.
		Map<Id,Valor> auxIdValor = new HashMap<Id,Valor>();
		Map<Id,ValorFuncao> auxIdValorFuncao = new HashMap<Id,ValorFuncao>();

		resolveBindings(ambiente, auxIdValor, auxIdValorFuncao);

		includeBindings(ambiente, auxIdValor, auxIdValorFuncao);

		Valor vresult = expressao.avaliar(ambiente);
		ambiente.restaura();
		return vresult;
	}

	private void includeBindings(
		AmbienteExecucaoFuncional ambiente,
		Map<Id,Valor> auxIdValor,
		Map<Id,ValorFuncao> auxIdValorFuncao)
		throws VariavelJaDeclaradaException {
	
		for(Map.Entry<Id,Valor> idValor:auxIdValor.entrySet()){
			Id id = (Id) idValor.getKey();
			Valor valor = (Valor) idValor.getValue();
			ambiente.map(id, valor);
		}
		
		for(Map.Entry<Id,ValorFuncao> idValorFuncao:auxIdValorFuncao.entrySet()){
			Id id = (Id) idValorFuncao.getKey();
			ValorFuncao valor = (ValorFuncao) idValorFuncao.getValue();
			ambiente.mapFuncao(id, valor);
		}	
	}

	private void resolveBindings(
		AmbienteExecucaoFuncional ambiente,
		Map<Id,Valor> auxIdValor,
		Map<Id,ValorFuncao> auxIdValorFuncao)
		throws VariavelNaoDeclaradaException, VariavelJaDeclaradaException {
			
		for(DeclaracaoFuncional decFuncional:this.seqdecFuncional){
			if (decFuncional.getAridade() == 0) {
				auxIdValor.put(
					decFuncional.getID(),
					decFuncional.getExpressao().avaliar(ambiente));
			} else {
				DecFuncao decFuncao = (DecFuncao) decFuncional;
				ValorFuncao valorFuncao = decFuncao.getFuncao();
				auxIdValorFuncao.put(decFuncional.getID(), valorFuncao);
			}			
		}
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
	public boolean checaTipo(AmbienteCompilacao ambiente)
		throws VariavelNaoDeclaradaException, VariavelJaDeclaradaException {
		ambiente.incrementa();

		boolean result = false;
		try {
			result = checkTypeBindings(ambiente);
			if (result) {
				Map<Id,Tipo> resolvedTypes = resolveTypeBidings(ambiente);
				includeTypeBindings(ambiente,resolvedTypes);		
				result = expressao.checaTipo(ambiente);
			}
		} finally {
			ambiente.restaura();				
		}
		return result;
	}

	private Map<Id,Tipo> resolveTypeBidings(AmbienteCompilacao ambiente)
		throws VariavelNaoDeclaradaException, VariavelJaDeclaradaException {
		Map<Id,Tipo> resolvedTypes = new HashMap<Id,Tipo>();
		
		for(DeclaracaoFuncional decFuncional:this.seqdecFuncional){
			if (resolvedTypes.put(decFuncional.getID(),decFuncional.getTipo(ambiente)) != null) {
				throw new VariavelJaDeclaradaException (decFuncional.getID());
			}
		}
		return resolvedTypes;
	}

	private boolean checkTypeBindings(AmbienteCompilacao ambiente)
		throws VariavelNaoDeclaradaException, VariavelJaDeclaradaException {
		boolean result = true;
		for(DeclaracaoFuncional decFuncional:this.seqdecFuncional){
			if (!decFuncional.checaTipo(ambiente)) {
				ambiente.restaura();
				result = false;
			}			
		}	
		return result;
	}


	private void includeTypeBindings(AmbienteCompilacao ambiente, Map<Id,Tipo> resolvedTypes)
			throws VariavelJaDeclaradaException {
		for(Id id:resolvedTypes.keySet()){
			Tipo type = (Tipo) resolvedTypes.get(id);
			ambiente.map(id, type);
		}
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
	 * @precondition this.checaTipo();
	 */
	public Tipo getTipo(AmbienteCompilacao ambiente)
		throws VariavelNaoDeclaradaException, VariavelJaDeclaradaException {
		ambiente.incrementa();
		for(DeclaracaoFuncional decFuncional:this.seqdecFuncional){
			if (decFuncional.getAridade() == 0) {
				ambiente.map(
					decFuncional.getID(),
					decFuncional.getExpressao().getTipo(ambiente));
			} else {
				DecFuncao decFuncao = (DecFuncao) decFuncional;
				Tipo tipo = decFuncao.getFuncao().getTipo(ambiente);
				if (tipo != Tipo.TIPO_INDEFINIDO) {
					ambiente.map(decFuncional.getID(), tipo);
				}
			}
		}
		Tipo vresult = expressao.getTipo(ambiente);
		ambiente.restaura();
		return vresult;
	}

	/**
	 * Returns the seqdecVariavel.
	 * @return List
	 */
	public List<DeclaracaoFuncional> getSeqdecFuncional() {
		return seqdecFuncional;
	}

	/**
	 * Returns the expressao.
	 * @return Expressao
	 */
	public Expressao getExpressao() {
		return expressao;
	}

}
