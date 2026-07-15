package plp.orientadaObjetos1.comando;

import java.io.EOFException;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.util.ArrayList;
import java.util.List;

import plp.expressions2.memory.VariavelJaDeclaradaException;
import plp.expressions2.memory.VariavelNaoDeclaradaException;
import plp.orientadaObjetos1.excecao.declaracao.ClasseNaoDeclaradaException;
import plp.orientadaObjetos1.excecao.declaracao.ObjetoJaDeclaradoException;
import plp.orientadaObjetos1.excecao.declaracao.ObjetoNaoDeclaradoException;
import plp.orientadaObjetos1.excecao.execucao.EntradaInvalidaException;
import plp.orientadaObjetos1.expressao.Expressao;
import plp.orientadaObjetos1.expressao.leftExpression.Id;
import plp.orientadaObjetos1.expressao.valor.ValorRef;
import plp.orientadaObjetos1.memoria.AmbienteCompilacaoOO1;
import plp.orientadaObjetos1.memoria.AmbienteExecucaoOO1;
import plp.orientadaObjetos1.memoria.Objeto;
import plp.orientadaObjetos1.util.Tipo;

/**
 * Representa um comando de leitura.
 */
public class ReadFile implements IO{
	/**
	 * O identificador ao qual ser� atribu�do o valor lido.
	 */
    private Id id;
	/**
	 * O tipo do identificador cujo novo valor ser� lido.
	 */
    private Tipo tipoId;
    
    private Expressao dir;

    private Expressao index;

	/**
	 * Construtor.
	 * @param id O identificador ao qual ser� a atribu�do o valor lido.
	 */
    public ReadFile ( Id id, Expressao dir, Expressao index){
        this.id = id;
        this.dir = dir;
        this.index = index;
    }

    /**
     * L� da entrada padr�o.
     * @param ambiente o ambiente de execu��o.
     * @return o ambiente depois de modificado pela execu��o
     * do comando read.
     *
     */
    public AmbienteExecucaoOO1 executar(AmbienteExecucaoOO1 ambiente)
        throws VariavelJaDeclaradaException, VariavelNaoDeclaradaException, EntradaInvalidaException {
        
    	try{

        	String path = this.dir.avaliar(ambiente).toString();
        	
			//Carrega o arquivo
			FileInputStream arquivoLeitura = new FileInputStream(path);

			//Classe responsavel por recuperar os objetos do arquivo
			ObjectInputStream objLeitura = new ObjectInputStream(arquivoLeitura);
						
			int count = 0;
			List <Objeto> objetos = new ArrayList<>();
			
			//pegue todos os objetos para obter o certo
			while (count != -1){
				try{
					objetos.add((Objeto) objLeitura.readObject());
					count++;
				}catch (EOFException eofExc){
					count = -1;
				}
			}
			
			ValorRef proxRef = ambiente.getProxRef();
			
			int pos = Integer.parseInt(this.index.avaliar(ambiente).toString());

			ambiente.mapObjeto(proxRef, objetos.get(pos));
			ambiente.changeValor(this.id, proxRef);
			
			objLeitura.close();
			arquivoLeitura.close();
			
    	}catch(NullPointerException | ObjetoNaoDeclaradoException | ClasseNaoDeclaradaException | 
    			IOException | ClassNotFoundException | ObjetoJaDeclaradoException exc){
        	exc.printStackTrace( );
    	} 

        return ambiente;
    }

    /**
     * Realiza a verificacao de tipos da entrada
     * @param ambiente o ambiente de compila��o.
     * @return <code>true</code> se a express�o da entrada est� bem tipada;
     *          <code>false</code> caso contrario.
     */
    public boolean checaTipo(AmbienteCompilacaoOO1 ambiente)
        throws VariavelNaoDeclaradaException {
//          Alteramos a implementa��o, pois em tempo de compila��o n�o se pode saber
//          o tipo da entrada que ser� lida.

//            Tipo tipo = ambiente.getTipoEntrada();
//            Tipo tipo2 = id.getTipo(ambiente);

        this.tipoId = id.getTipo(ambiente);
        return id.checaTipo(ambiente);

        //return id.getTipo(ambiente).equals(ambiente.getTipoEntrada());
    }

}
