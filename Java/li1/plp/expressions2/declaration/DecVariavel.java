package li1.plp.expressions2.declaration;

import li1.plp.expressions2.expression.Expressao;
import li1.plp.expressions2.expression.Id;

public class DecVariavel{
	private Id id;
	private Expressao expressao;
	
	public DecVariavel(Id idArg, Expressao expressaoArg) {
		id = idArg;
		expressao = expressaoArg;
	}
	
	public Id getID() {
		return id;
	}
	public Expressao getExpressao() {
		return expressao;
	}
}
