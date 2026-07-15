class Contador {
    private int valor = 1;
    public void inc() {
        valor++;
    }
    public void print() {
        System.out.println(valor);
    }
}
public class Exemplo2 {
    public static void main(String[] args) {
        Contador c = new Contador();
        Contador c2 = new Contador();
        c.inc();
        c2.inc();
        c2.inc();
        c.print();
        c2.print();
    }
}