package lf1.plp.expressions2.memory;

import lf1.plp.expressions2.expression.Id;
import lf1.plp.functional1.memory.ContextoExecucaoFuncional;

public interface Ambiente<T> {

  public void incrementa();
  public void restaura();
  
  public void map( Id idArg, T tipoId) throws VariavelJaDeclaradaException;
  public T get( Id idArg ) throws VariavelNaoDeclaradaException;

} 
