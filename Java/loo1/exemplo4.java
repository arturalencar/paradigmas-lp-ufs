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
    public void remove(int v) {
        LValor aux = this;
        while (aux.prox != null && aux.prox.valor != v) {
            aux = aux.prox;
        }
        if (aux.prox != null) {
            aux.prox = aux.prox.prox;
        }

    public void print() {
        System.out.println(valor);
        if (prox != null) {
            prox.print();
        }
    }
}

public class Exemplo4 {
    public static void main(String[] args) {
        LValor lv = new LValor();
        lv.insere(2);
        lv.insere(3);
        lv.insere(4);
        lv.print();
        System.out.println("Após remover 3:");
        lv.remove(3);
        lv.print();
    }
}