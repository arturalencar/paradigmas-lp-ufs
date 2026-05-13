package le2.plp.expressions1.util;

	import java.util.Collections;
	import java.util.EnumSet;
	import java.util.Set;

	/**
	 * Classe que representa os possiveis tipos de uma expressao.
	 * Objetos desta classe sao imutaveis, portanto as vezes as
	 * instancias sao compartilhadas.
	 * 
	 * Modificado em 11/07/2005 por Leonardo Lucena para usar tipos enumerados
	 * 
	 */
	public class Tipo {
		
		public enum Tipos{INTEIRO, BOOLEANO, STRING, PID, TUPLA}
		
		public static final Tipo TIPO_INTEIRO = new Tipo(EnumSet.of(Tipos.INTEIRO));
		public static final Tipo TIPO_BOOLEANO = new Tipo(EnumSet.of(Tipos.BOOLEANO));
		public static final Tipo TIPO_STRING = new Tipo(EnumSet.of(Tipos.STRING));
		public static final Tipo TIPO_PID = new Tipo(EnumSet.of(Tipos.PID));
		public static final Tipo TIPO_TUPLA = new Tipo(EnumSet.of(Tipos.TUPLA));
		public static final Tipo TIPO_INDEFINIDO = new Tipo(EnumSet.noneOf(Tipos.class));
		
		private Set<Tipos> tipo;

		/**
		 * O tipo de retorno, no caso de ser uma funcao. O que ocorre por
		 * exemplo com uma funcao f(x) = x == 1 (do tipo Int -> Bool), &eacute;
		 * que seu tipo ser&aacute; um objeto desta classe do tipo Inteiro cujo
		 * campo <code>prox</code> ser&aacute; outro objeto desta classe, do
		 * tipo Booleano (que por sua vez ter&aacute; o campo <code>prox</code>
		 * igual a <code>null</code>.
		 */
		private Tipo prox;

		/**
		 * Construtor da classe que representa um tipo qualquer
		 * (inteiro, boolean ou string).
		 */
		public Tipo() {
			this(EnumSet.allOf(Tipos.class));
		}

		/**
		 * Construtor da classe que representa um tipo qualquer
		 * (inteiro, boolean ou string).
		 *
		 * @param prox o proximo head no tipo de uma funcao, ou
		 *          <code>null</code> para o caso de tipos primitivos.
		 */
		public Tipo(Tipo prox) {
			this(EnumSet.allOf(Tipos.class), prox);
		}

		/**
		 * Construtor da classe.
		 *
		 * @param tipo o tipo da expressao associada.
		 * @see #Tipos.INTEIRO
		 * @see #Tipos.BOOLEANO
		 * @see #Tipos.STRING
		 */
		public Tipo(Set<Tipos> tipo) {
			this(tipo, null);
		}

		/**
		 * Construtor da classe.
		 *
		 * @param tipo o tipo da expressao associada.
		 * @param prox o proximo head no tipo de uma funcao, ou
		 *          <code>null</code> para o caso de tipos primitivos.
		 * @see #Tipos.INTEIRO
		 * @see #Tipos.BOOLEANO
		 * @see #Tipos.STRING
		 */
		public Tipo(Set<Tipos> tipo, Tipo prox) {
			this.tipo = tipo;
			this.prox = prox;
		}

		/**
		 * Retorna o tipo da expressao associada.
		 *
		 * @return o tipo da expressao associada.
		 * @see #Tipos.INTEIRO
		 * @see #Tipos.BOOLEANO
		 * @see #Tipos.STRING
		 */
		public Set<Tipos> get() {
			return Collections.unmodifiableSet(tipo);
		}

		/**
		 * Indica se esta expressao &eacute; inteira.
		 *
		 * @return <code>true</code> se esta expressao for inteira;
		 *          <code>false</code> caso contrario.
		 */
		public boolean eInteiro() {
			return tipo.contains(Tipos.INTEIRO);
		}

		/**
		 * Indica se esta expressao &eacute; booleana.
		 *
		 * @return <code>true</code> se esta expressao for booleana;
		 *          <code>false</code> caso contrario.
		 */
		public boolean eBooleano() {
			return tipo.contains(Tipos.BOOLEANO);
		}

		/**
		 * Indica se esta expressao &eacute; string.
		 *
		 * @return <code>true</code> se esta expressao for string;
		 *          <code>false</code> caso contrario.
		 */
		public boolean eString() {
			return tipo.contains(Tipos.STRING);
		}
		
		/**
		 * Indica se esta expressao &eacute; string.
		 *
		 * @return <code>true</code> se esta expressao for string;
		 *          <code>false</code> caso contrario.
		 */
		public boolean ePid() {
			return tipo.contains(Tipos.PID);
		}
		
		public boolean eTupla() {
			return tipo.contains(Tipos.TUPLA);
		}

		/**
		 * Indica se esta expressao nao pode representar tipo algum.
		 *
		 * @return <code>true</code> se esta expressao for void;
		 *          <code>false</code> caso contrario.
		 */
		public boolean eVoid() {
			return tipo.isEmpty();
		}

		/**
		 * Compara este tipo com o tipo dado.
		 *
		 * @return <code>true</code> se se tratarem do mesmo tipo;
		 *          <code>false</code> caso contrario.
		 */
		@Override
		public boolean equals(Object obj) {
			return (obj instanceof Tipo && 
					((Tipo) obj).tipo.equals(tipo));
		}

		/**
		 * Retorna o tipo mais abrangente que engloba este tipo
		 * e o tipo dado. Por exemplo, se este tipo pode ser String
		 * ou inteiro e o tipo dado pode ser inteiro ou booleano,
		 * entao este metodo retorna um tipo que so pode ser inteiro.
		 *
		 * @param outroTipo o outro tipo.
		 * @return a <i>interse&ccedil;&atilde;o</i> entre este tipo e o
		 *          tipo dado.
		 */
		public Tipo intersecao(Tipo outroTipo) {
			Tipo novoTipo;
			if (tipo.equals(outroTipo.tipo)) {
				novoTipo = this;
			} else {
				Set<Tipos> t = EnumSet.copyOf(tipo);
				t.retainAll(outroTipo.tipo);
				novoTipo = new Tipo(t);
			}
			return novoTipo;
		}

		/**
		 * Retorna o tipo de retorno, no caso de ser uma funcao. O que ocorre por
		 * exemplo com uma funcao f(x) = x == 1 (do tipo Int -> Bool), &eacute;
		 * que seu tipo ser&aacute; um objeto desta classe do tipo Inteiro cujo
		 * campo <code>prox</code> ser&aacute; outro objeto desta classe, do
		 * tipo Booleano (que por sua vez ter&aacute; o campo <code>prox</code>
		 * igual a <code>null</code>.
		 *
		 * @return o tipo de retorno, no caso de uma fun��o, ou <code>null</code>
		 *          no caso de valor primitivo.
		 */
		public Tipo getProx() {
			return prox;
		} 
		
		public void setProx(Tipo novoProx)
		{
			this.prox = novoProx;
		}

		public boolean eValido() {
	           return (tipo.size() == 1);
		}

	    

}
