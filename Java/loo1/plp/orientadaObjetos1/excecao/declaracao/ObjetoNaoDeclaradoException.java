package plp.orientadaObjetos1.excecao.declaracao;

import plp.expressions2.expression.Id;


/**
 * Exce��o lan�ada quando o objeto que est� sendo referenciado n�o
 * foi declarado.
 */
public class ObjetoNaoDeclaradoException extends Exception {
    /**
     * Construtor.
     * @param id Identificador representando o objeto.
     */
    public ObjetoNaoDeclaradoException(Id id) {
        super("Objeto" + id + " n�o declarado.");
    }
}
