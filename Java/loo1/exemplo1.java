class Contador {
    private int valor = 1;

    public void inc() {
        valor++;
    }

    public void print() {
        System.out.println(valor);
    }
}

public class Exemplo1 {
    public static void main(String[] args) {
        Contador c = new Contador();

        c.inc();
        c.print();
    }
}
