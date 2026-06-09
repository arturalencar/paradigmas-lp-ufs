package lf1.plp.expressions2.memory;

import java.util.HashMap;
import java.util.Stack;

import lf1.plp.expressions2.expression.Id;
import lf1.plp.expressions2.expression.Valor;

public class ContextoExecucao extends Contexto<Valor> implements AmbienteExecucao {
	public ContextoExecucao clone()
	{
		ContextoExecucao ret = new ContextoExecucao();
		ret.setPilha((Stack<HashMap<Id,Valor>>)this.getPilha().clone());
		return ret;
	}
}

