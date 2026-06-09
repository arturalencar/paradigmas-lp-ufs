package lf1.plp.functional1.util;

import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;
import java.util.HashMap;
import java.util.Iterator;
import java.util.List;
import java.util.Map;

import lf1.plp.expressions1.util.Tipo;
import lf1.plp.expressions2.expression.ExpAnd;
import lf1.plp.expressions2.expression.ExpConcat;
import lf1.plp.expressions2.expression.ExpEquals;
import lf1.plp.expressions2.expression.ExpLength;
import lf1.plp.expressions2.expression.ExpMenos;
import lf1.plp.expressions2.expression.ExpNot;
import lf1.plp.expressions2.expression.ExpOr;
import lf1.plp.expressions2.expression.ExpSoma;
import lf1.plp.expressions2.expression.ExpSub;
import lf1.plp.expressions2.expression.Expressao;
import lf1.plp.expressions2.expression.Id;
import lf1.plp.expressions2.expression.ValorInteiro;
import lf1.plp.expressions2.expression.ValorBooleano;
import lf1.plp.expressions2.expression.ValorString;
import lf1.plp.expressions2.memory.AmbienteCompilacao;
import lf1.plp.expressions2.memory.VariavelJaDeclaradaException;
import lf1.plp.expressions2.memory.VariavelNaoDeclaradaException;
import lf1.plp.functional1.declaration.DecFuncao;
import lf1.plp.functional1.declaration.DeclaracaoFuncional;
import lf1.plp.functional1.expression.Aplicacao;
import lf1.plp.functional1.expression.ExpDeclaracao;
import lf1.plp.functional1.expression.IfThenElse;

/**
 * @author Sérgio
 *
 * To change this generated comment edit the template variable "typecomment":
 * Window>Preferences>Java>Templates.
 * To enable and disable the creation of type comments go to
 * Window>Preferences>Java>Code Generation.
 */
public class RestrictTypesVisitor {
	private static Map<String,Method> metodosVisit;
	

	static {
		metodosVisit = new HashMap<String,Method>();
		Method metodos[] = RestrictTypesVisitor.class.getMethods();
		
		for(Method method:metodos){
			if (method.getName().startsWith("_visit")) {
				metodosVisit.put(method.getName(), method);
			}		
		}
	}

	public static Map<String,Method> visit(
		Expressao exp,
		AmbienteCompilacao ambiente,
		Map tipos,
		Tipo tipoEsperado) {

		// Class.getName() returns package information as well.
		// This strips off the package information giving us
		// just the class name
		String methodName = exp.getClass().getName();
		methodName =
			"_visit" + methodName.substring(methodName.lastIndexOf('.') + 1);

		Map<String,Method> result = null;
		// Now we try to invoke the method visit
		try {
			// Get the method visitFoo(Foo foo)
			Method m = getMethod(methodName);
			// Try to invoke visitFoo(Foo foo)
			result =
				(Map) m.invoke(
					null,
					new Object[] { exp, ambiente, tipos, tipoEsperado });
		} catch (IllegalAccessException e) {
			System.out.println(e.getMessage());
			e.printStackTrace();
			throw new IllegalStateException(
				"Não foi possível executar o método ("
					+ methodName
					+ "). IllegalAccessException");

		} catch (InvocationTargetException e) {
			System.out.println(e.getMessage());
			e.printStackTrace();

			throw new IllegalStateException(
				"Não foi possível executar o método ("
					+ methodName
					+ "). InvocationTargetException");

		} catch (NoSuchMethodException e) {
			System.out.println(e.getMessage());
			e.printStackTrace();

			throw new IllegalStateException(
				"O método visit chamado ("
					+ methodName
					+ ") não foi implementado");
		}
		return result;
	}

	private static Method getMethod(String name) throws NoSuchMethodException {
		Object method = metodosVisit.get(name);
		if (method == null) {
			throw new NoSuchMethodException(
				"O método '" + name + "' especificado não foi encontrado");
		}
		return (Method) method;
	}

	/**
	 * Realiza a inferencia de tipos dos identificadores do mapeamento dado.
	 *
	 * @param ambiente o ambiente que contem o mapeamento entre
	 *          identificadores e tipos.
	 * @param listaIds o mapeamento atual dos identificadores em tipos.
	 * @param tipoEsperado o tipo esperado desta expressao.
	 * @return um mapeamento mais restrito dos identificadores nos seus tipos.
	 */
	public static Map _visitAplicacao(
		Aplicacao aplicacao,
		AmbienteCompilacao ambiente,
		Map tipos,
		Tipo tipoEsperado) {
		try {
			Tipo t = ambiente.get(aplicacao.getFunc());
			List auxExpressoes = aplicacao.getArgsExpressao();
			Map mapIdTipo = tipos;
			for (Iterator iterExpressoes = auxExpressoes.iterator();
				iterExpressoes.hasNext();
				) {
				Expressao exp = (Expressao) iterExpressoes.next();
				Tipo tArg = new Tipo(t.get());
				// para pegar o tipo somente do argumento.
				mapIdTipo =
					RestrictTypesVisitor.visit(exp, ambiente, mapIdTipo, tArg);
				t = t.getProx();
			}

			return mapIdTipo;
		} catch (VariavelNaoDeclaradaException e) {
			// se a funcao nao estiver declarada, tenta fazer a restrição das expressões.
			Map mapIdTipo = tipos;
			Tipo tudo = new Tipo();
			for (Iterator iterExpressoes =
				aplicacao.getArgsExpressao().iterator();
				iterExpressoes.hasNext();
				) {
				Expressao exp = (Expressao) iterExpressoes.next();
				mapIdTipo =
					RestrictTypesVisitor.visit(exp, ambiente, mapIdTipo, tudo);

			}

			return mapIdTipo;
		}
	}

	/**
	 * Realiza a inferencia de tipos dos identificadores do mapeamento dado.
	 *
	 * @param ambiente o ambiente que contem o mapeamento entre
	 *          identificadores e tipos.
	 * @param listaIds o mapeamento atual dos identificadores em tipos.
	 * @param tipoEsperado o tipo esperado desta expressao.
	 * @return um mapeamento mais restrito dos identificadores nos seus tipos.
	 */
	public static Map _visitExpAnd(
		ExpAnd expressao,
		AmbienteCompilacao ambiente,
		Map mapIdTipo,
		Tipo tipoEsperado) {
		Map aux =
			visit(expressao.getEsq(), ambiente, mapIdTipo, Tipo.TIPO_BOOLEANO);
		aux = visit(expressao.getDir(), ambiente, aux, Tipo.TIPO_BOOLEANO);
		return aux;
	}

	/**
	 * Realiza a inferencia de tipos dos identificadores do mapeamento dado.
	 *
	 * @param ambiente o ambiente que contem o mapeamento entre
	 *          identificadores e tipos.
	 * @param listaIds o mapeamento atual dos identificadores em tipos.
	 * @param tipoEsperado o tipo esperado desta expressao.
	 * @return um mapeamento mais restrito dos identificadores nos seus tipos.
	 */
	public static Map _visitExpConcat(
		ExpConcat expressao,
		AmbienteCompilacao ambiente,
		Map mapIdTipo,
		Tipo tipoEsperado) {
		Map aux =
			visit(expressao.getEsq(), ambiente, mapIdTipo, Tipo.TIPO_STRING);
		aux = visit(expressao.getDir(), ambiente, aux, Tipo.TIPO_STRING);
		return aux;
	}

	/**
	 * Realiza a inferencia de tipos dos identificadores do mapeamento dado.
	 *
	 * @param ambiente o ambiente que contem o mapeamento entre
	 *          identificadores e tipos.
	 * @param listaIds o mapeamento atual dos identificadores em tipos.
	 * @param tipoEsperado o tipo esperado desta expressao.
	 * @return um mapeamento mais restrito dos identificadores nos seus tipos.
	 */
	public static Map _visitExpDeclaracao(
		ExpDeclaracao expressao,
		AmbienteCompilacao ambiente,
		Map tipos,
		Tipo tipoEsperado) {
		ambiente.incrementa();
		Map map = tipos;

		for (Iterator iterDecFuncional =
			expressao.getSeqdecFuncional().iterator();
			iterDecFuncional.hasNext();
			) {
			DeclaracaoFuncional decFuncional =
				(DeclaracaoFuncional) iterDecFuncional.next();
			Tipo tipoProcurado = null;
			try {
				if (decFuncional.getAridade() == 0) {
					tipoProcurado =
						decFuncional.getExpressao().getTipo(ambiente);
					ambiente.map(decFuncional.getID(), tipoProcurado);
				} else {
					DecFuncao decFuncao = (DecFuncao) decFuncional;
					Tipo tipo = decFuncao.getFuncao().getTipo(ambiente);
					tipoProcurado = tipo;
					if (tipo != Tipo.TIPO_INDEFINIDO) {
						ambiente.map(decFuncional.getID(), tipo);
					}
				}
			} catch (VariavelJaDeclaradaException e) { // Não vai ocorrer.
			} catch (VariavelNaoDeclaradaException e) {
			} // Não vai ocorrer.

			map =
				visit(
					decFuncional.getExpressao(),
					ambiente,
					map,
					tipoProcurado);
		}
		map = visit(expressao.getExpressao(), ambiente, map, tipoEsperado);
		ambiente.restaura();
		return map;
	}

	/**
	 * Realiza a inferencia de tipos dos identificadores do mapeamento dado.
	 *
	 * @param ambiente o ambiente que contem o mapeamento entre
	 *          identificadores e tipos.
	 * @param listaIds o mapeamento atual dos identificadores em tipos.
	 * @param tipoEsperado o tipo esperado desta expressao.
	 * @return um mapeamento mais restrito dos identificadores nos seus tipos.
	 */
	public static Map _visitExpEquals(
		ExpEquals expressao,
		AmbienteCompilacao ambiente,
		Map tipos,
		Tipo tipoEsperado) {
		return tipos;
	}

	/**
	 * Realiza a inferencia de tipos dos identificadores do mapeamento dado.
	 *
	 * @param ambiente o ambiente que contem o mapeamento entre
	 *          identificadores e tipos.
	 * @param listaIds o mapeamento atual dos identificadores em tipos.
	 * @param tipoEsperado o tipo esperado desta expressao.
	 * @return um mapeamento mais restrito dos identificadores nos seus tipos.
	 */
	public static Map _visitExpLength(
		ExpLength expressao,
		AmbienteCompilacao ambiente,
		Map tipos,
		Tipo tipoEsperado) {
		Map aux = visit(expressao.getExp(), ambiente, tipos, Tipo.TIPO_STRING);
		return aux;
	}

	/**
	 * Realiza a inferencia de tipos dos identificadores do mapeamento dado.
	 *
	 * @param ambiente o ambiente que contem o mapeamento entre
	 *          identificadores e tipos.
	 * @param listaIds o mapeamento atual dos identificadores em tipos.
	 * @param tipoEsperado o tipo esperado desta expressao.
	 * @return um mapeamento mais restrito dos identificadores nos seus tipos.
	 */
	public static Map _visitExpMenos(
		ExpMenos expressao,
		AmbienteCompilacao ambiente,
		Map tipos,
		Tipo tipoEsperado) {
		Map aux = visit(expressao.getExp(), ambiente, tipos, Tipo.TIPO_INTEIRO);
		return aux;
	}

	/**
	 * Realiza a inferencia de tipos dos identificadores do mapeamento dado.
	 *
	 * @param ambiente o ambiente que contem o mapeamento entre
	 *          identificadores e tipos.
	 * @param listaIds o mapeamento atual dos identificadores em tipos.
	 * @param tipoEsperado o tipo esperado desta expressao.
	 * @return um mapeamento mais restrito dos identificadores nos seus tipos.
	 */
	public static Map _visitExpNot(
		ExpNot expressao,
		AmbienteCompilacao ambiente,
		Map tipos,
		Tipo tipoEsperado) {
		Map aux =
			visit(expressao.getExp(), ambiente, tipos, Tipo.TIPO_BOOLEANO);
		return aux;
	}

	/**
	 * Realiza a inferencia de tipos dos identificadores do mapeamento dado.
	 *
	 * @param ambiente o ambiente que contem o mapeamento entre
	 *          identificadores e tipos.
	 * @param listaIds o mapeamento atual dos identificadores em tipos.
	 * @param tipoEsperado o tipo esperado desta expressao.
	 * @return um mapeamento mais restrito dos identificadores nos seus tipos.
	 */
	public static Map _visitExpOr(
		ExpOr expressao,
		AmbienteCompilacao ambiente,
		Map tipos,
		Tipo tipoEsperado) {
		Map aux =
			visit(expressao.getEsq(), ambiente, tipos, Tipo.TIPO_BOOLEANO);
		aux = visit(expressao.getDir(), ambiente, aux, Tipo.TIPO_BOOLEANO);
		return aux;
	}

	/**
	 * Realiza a inferencia de tipos dos identificadores do mapeamento dado.
	 *
	 * @param ambiente o ambiente que contem o mapeamento entre
	 *          identificadores e tipos.
	 * @param listaIds o mapeamento atual dos identificadores em tipos.
	 * @param tipoEsperado o tipo esperado desta expressao.
	 * @return um mapeamento mais restrito dos identificadores nos seus tipos.
	 */
	public static Map _visitExpSoma(
		ExpSoma expressao,
		AmbienteCompilacao ambiente,
		Map tipos,
		Tipo tipoEsperado) {
		Map aux = visit(expressao.getEsq(), ambiente, tipos, Tipo.TIPO_INTEIRO);
		aux = visit(expressao.getDir(), ambiente, aux, Tipo.TIPO_INTEIRO);
		return aux;
	}

	/**
	 * Realiza a inferencia de tipos dos identificadores do mapeamento dado.
	 *
	 * @param ambiente o ambiente que contem o mapeamento entre
	 *          identificadores e tipos.
	 * @param listaIds o mapeamento atual dos identificadores em tipos.
	 * @param tipoEsperado o tipo esperado desta expressao.
	 * @return um mapeamento mais restrito dos identificadores nos seus tipos.
	 */
	public static Map _visitExpSub(
		ExpSub expressao,
		AmbienteCompilacao ambiente,
		Map tipos,
		Tipo tipoEsperado) {
		Map aux = visit(expressao.getEsq(), ambiente, tipos, Tipo.TIPO_INTEIRO);
		aux = visit(expressao.getDir(), ambiente, aux, Tipo.TIPO_INTEIRO);
		return aux;
	}

	/**
	 * Realiza a inferencia de tipos dos identificadores do mapeamento dado.
	 *
	 * @param ambiente o ambiente que contem o mapeamento entre
	 *          identificadores e tipos.
	 * @param listaIds o mapeamento atual dos identificadores em tipos.
	 * @param tipoEsperado o tipo esperado desta expressao.
	 * @return um mapeamento mais restrito dos identificadores nos seus tipos.
	 */
	public static Map _visitIfThenElse(
		IfThenElse expressao,
		AmbienteCompilacao ambiente,
		Map tipos,
		Tipo tipoEsperado) {
		Map aux =
			visit(expressao.getCondicao(), ambiente, tipos, Tipo.TIPO_BOOLEANO);
		aux = visit(expressao.getThen(), ambiente, aux, tipoEsperado);
		aux = visit(expressao.getElseExpressao(), ambiente, aux, tipoEsperado);
		return aux;
	}

	public static Map _visitId(
		Id thisId,
		AmbienteCompilacao ambiente,
		Map tipos,
		Tipo tipoEsperado) {

		for (Iterator iterIdTipo = tipos.entrySet().iterator();
			iterIdTipo.hasNext();
			) {
			Map.Entry idTipo = (Map.Entry) iterIdTipo.next();
			Id id = (Id) idTipo.getKey();
			Tipo tipoAtual = (Tipo) idTipo.getValue();
			if (id.equals(thisId)) {
				tipos.put(id, tipoEsperado.intersecao(tipoAtual));
			}
		}
		return tipos;
	}

    public static Map _visitValorInteiro(
		ValorInteiro valor,
		AmbienteCompilacao ambiente,
		Map tipos,
		Tipo tipoEsperado) {

	return tipos;
    }

    public static Map _visitValorString(
		ValorString valor,
		AmbienteCompilacao ambiente,
		Map tipos,
		Tipo tipoEsperado) {

	return tipos;
    }

    public static Map _visitValorBooleano(
		ValorBooleano valor,
		AmbienteCompilacao ambiente,
		Map tipos,
		Tipo tipoEsperado) {

	return tipos;
    }
}

