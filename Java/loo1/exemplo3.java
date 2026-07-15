class LValor {
    private int valor = -100;
    private LValor prox = null;
    public void insere(int v) {
        if (valor == -100) {
            valor = v;
            prox = new LValor();
        } else {
            prox.insere(v);
        }
    }
    public void print() {
        System.out.println(valor);

        if (prox != null) {
            prox.print();
        }
    }
}
public class Exemplo3 {
    public static void main(String[] args) {
        LValor lv = new LValor();
        lv.insere(3);
        lv.insere(4);
        lv.print();
    }
}