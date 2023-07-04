public class Main {

    public static void main(String[] args) {

        int pedidos = 4;
        Thread[] thread = new Thread[pedidos];

        for (int i = 0; i < pedidos; i++) {
            FilaPedidos fila = new FilaPedidos(i+1);
            thread[i] = new Thread(new Pedido(fila, i+1));
        }

        for (int i = 0; i < pedidos; i++) {
            thread[i].start();
        }
    }
    
}