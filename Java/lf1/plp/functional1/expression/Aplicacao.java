//Mudar o for do iterator para o novo for.
package lf1.plp.functional1.expression;

import java.util.HashMap;
import java.util.Iterator;
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
import lf1.plp.functional1.memory.AmbienteExecucaoFuncional;
import lf1.plp.functional1.util.ValorFuncao;

public class Aplicacao implements Expressao {

	private Id func;
	private List<Expressao> argsExpressao;

	public Aplicacao(Id f, List<Expressao> expressoes) {
		func = f;
		argsExpressao = expressoes;
	}

	/**
	 * Retorna uma representacao String desta expressao. Util para depuracao.
	 *
	 * @return uma representacao String desta expressao.
	 */
	public String toString() {
		StringBuffer sb = new StringBuffer();
		sb.append(func.toString());
		sb.append(" (");
		sb.append(argsExpressao.toString());
		sb.append(')');
		return sb.toString();
	}

	public Valor avaliar(AmbienteExecucao ambiente)
		throws VariavelNaoDeclaradaException, VariavelJaDeclaradaException {
		AmbienteExecucaoFuncional ambienteFuncional =
			(AmbienteExecucaoFuncional) ambiente;
		
		ValorFuncao funcao = ambienteFuncional.getFuncao(func);
		
		Map<Id,Valor> mapIdValor = resolveParametersBindings(ambiente, funcao);

		ambiente.incrementa();

		includeValueBindings(ambiente, mapIdValor);

		Valor vresult = funcao.getExp().avaliar(ambiente);
		ambiente.restaura();
		return vresult;
	}

	private void includeValueBindings(AmbienteExecucao ambiente, Map<Id,Valor> mapIdValor)
		throws VariavelJaDeclaradaException {
		for(Map.Entry<Id,Valor> mapeamento:mapIdValor.entrySet()){
			Id id = (Id) mapeamento.getKey();
			Valor valor = (Valor) mapeamento.getValue();
			ambiente.map(id, valor);
		}
	}

	private Map<Id,Valor> resolveParametersBindings(AmbienteExecucao ambiente, ValorFuncao funcao)
		throws VariavelNaoDeclaradaException, VariavelJaDeclaradaException {
		List<Id> parametrosId = funcao.getListaId();
		List<Expressao> expressoesValorReal = argsExpressao;
		
		Map<Id,Valor> mapIdValor = new HashMap<Id,Valor>();

		Iterator<Expressao> iterExpressoesValor = expressoesValorReal.iterator();
        for(Id id:parametrosId){	
			Expressao exp = iterExpressoesValor.next();
			Valor valorReal = exp.avaliar(ambiente);
			mapIdValor.put(id, valorReal);			
        }	
		return mapIdValor;
	}

	/**
	 * Realiza a verificacao de tipos desta expressao.
	 *
	 * @param amb o ambiente de compila��o.
	 * @return <code>true</code> se os tipos da expressao sao validos;
	 *          <code>false</code> caso contrario.
	 * @exception VariavelNaoDeclaradaException se existir um identificador
	 *          nao declarado no ambiente.
	 * @exception VariavelNaoDeclaradaException se existir um identificador
	 *          declarado mais de uma vez no mesmo bloco do ambiente.
	 */
	public boolean checaTipo(AmbienteCompilacao ambiente)
		throws VariavelNaoDeclaradaException, VariavelJaDeclaradaException {	

		Tipo tipoFuncao = ambiente.get(func);
	
		return checkArgumentListSize(tipoFuncao) 
				&& checkArgumentTypes(ambiente, tipoFuncao) ;
	}

	private boolean checkArgumentTypes(
		AmbienteCompilacao ambiente,
		Tipo tipoFuncao)		
		throws VariavelNaoDeclaradaException, VariavelJaDeclaradaException {
		boolean result = true;
		List<Expressao> expressoesValorReal = argsExpressao;
		
		
		for(Expressao valorReal:expressoesValorReal){
			if (!valorReal.checaTipo(ambiente)) {
				result = false;
			}
			Tipo tipoArg = valorReal.getTipo(ambiente);
			if (tipoArg.intersecao(tipoFuncao).eVoid()) {
				result = false;
			}
			tipoFuncao = tipoFuncao.getProx();
		}	
		return result;
	}

	private boolean checkArgumentListSize(Tipo tipoFuncao) {
		boolean res;
		{
				res = true;
				
				List<Expressao> expressoesValorReal = argsExpressao;
		
				Tipo aux = tipoFuncao;
		
				int tamanhoTipo = 0;
				while (aux != null) {
					tamanhoTipo++;
					aux = aux.getProx();
				}
				if ((tamanhoTipo - 1) != expressoesValorReal.size()) {
					res = false;
				}
				
		}	
		return res;
	}

	/**
	 * Retorna os tipos possiveis desta expressao.
	 *
	 * @param amb o ambiente de compila��o.
	 * @return os tipos possiveis desta expressao.
	 * @exception VariavelNaoDeclaradaException se existir um identificador
	 *          nao declarado no ambiente.
	 * @exception VariavelNaoDeclaradaException se existir um identificador
	 *          declarado mais de uma vez no mesmo bloco do ambiente.
	 * @precondition this.checaTipo();
	 */
	public Tipo getTipo(AmbienteCompilacao ambiente)
		throws VariavelNaoDeclaradaException, VariavelJaDeclaradaException {
		Tipo t = ambiente.get(func);
		while (t.getProx() != null) {
			t = t.getProx();
		}
		return t;
	}

	/**
	 * Returns the func.
	 * @return Id
	 */
	public Id getFunc() {
		return func;
	}

	/**
	 * Returns the args.
	 * @return ListaExpressao
	 */
	public List<Expressao> getArgsExpressao() {
		return argsExpressao;
	}
}
