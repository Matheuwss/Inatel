import java.util.concurrent.Semaphore;

public class FilaPedidos {

    int mesa;

    public FilaPedidos(int i) {
        mesa = i;
    }

    public void pedidoSemSemaforo() {
        System.out.println("S-PEDIDO DA MESA " + mesa + " SAIU PARA ENTREGA");
        System.out.println("S-PEDIDO DA MESA " + mesa + " FOI ENTREGUE");
    }

    static Semaphore semaforo = new Semaphore(1);   //semáforo precisou ser static para funcionar

    public void pedidoComSemaforo(){
        try {
            semaforo.acquire();
            System.out.println("C-PEDIDO DA MESA " + mesa + " SAIU PARA ENTREGA");
        } catch (InterruptedException e) {}

        finally{
            System.out.println("C-PEDIDO DA MESA " + mesa + " FOI ENTREGUE");
            semaforo.release();
        }
    }

}