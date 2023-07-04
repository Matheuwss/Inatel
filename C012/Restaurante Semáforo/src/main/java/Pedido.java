public class Pedido extends Thread {

    FilaPedidos fila;
    int mesa;

    public Pedido(FilaPedidos fp, int i){
        fila = fp;
        mesa = i;
    }

    @Override
    public void run(){
        System.out.println("O PEDIDO DA " + mesa + " ESTÁ PRONTO PARA ENTREGA");
        //fila.pedidoSemSemaforo();
        fila.pedidoComSemaforo();
    }

}