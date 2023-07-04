package poo_projetoFinal;

public class Conta {

    private int numero;
    private String tipo;
    private Double saldo;
    private Cliente cliente;
    static int qtdContas = 0;
    private boolean status;

    public Conta(Cliente cliente, String tipo, Double saldo) {
        super();
        qtdContas++;
        this.numero = qtdContas;
        this.cliente = cliente;
        this.saldo = saldo;
        this.tipo = tipo;
        this.status = false;
    }

    //Getters e setters
    public int getNumero() {
        return numero;
    }

    public void setNumero(int numero) {
        this.numero = numero;
    }

    public Cliente getCliente() {
        return cliente;
    }

    public void setCliente(Cliente cliente) {
        this.cliente = cliente;
    }

    public String getTipo() {
        return tipo;
    }

    public void setTipo(String tipo) {
        this.tipo = tipo;
    }

    public Double getSaldo() {
        return saldo;
    }

    public void setSaldo(Double saldo) {
        this.saldo = saldo;
    }

    public boolean getStatus() {
        return status;
    }

    public void setStatus(boolean status) {
        this.status = status;
    }

    public void MostrarDadosBancarios(){
        System.out.println("");
        System.out.println("---------------------------");
        System.out.println("----- Dados Bancários -----");
        System.out.println("Número: " + numero);
        System.out.println("SALDO: R$" + saldo);
        System.out.println("TIPO: " + tipo);
        System.out.println("CPF DO TITULAR: " + getCliente().getCpfCliente());
        System.out.println("NOME DO TITULAR: " + getCliente().getNomeCliente());
        System.out.println("ENDEREÇO DO TITULAR: " + getCliente().getEndCliente());
        System.out.println("TELEFONE DO TITULAR: " + getCliente().getTelCliente());
        System.out.println("---------------------------");
        System.out.println("");
    }

    public String encerrarConta() {
        if (this.status == true && this.saldo == 0) {
            this.status = false;
            String msg = "CONTA ENCERRADA COM SUCESSO!";
            return msg;
        } else {
            String msg = "Conta inexistente ou com saldo positivo/devedor";
            return msg;
        }
    }

    public void depositar(Double valorDeposito){
        if (valorDeposito > 0 ){
            this.saldo += valorDeposito;
            System.out.println("Depósito na conta de " + getCliente().getNomeCliente() + " realizado com sucesso");
        }
        else System.out.println("Valor inválido!! Depósito NÃO realizado!");
    }

    public void sacar(Double valorSaque){
        if (valorSaque < this.saldo || valorSaque > 0){
            this.saldo -= valorSaque;
            System.out.println("O saque na conta de " + getCliente().getNomeCliente() + " foi realizado com sucesso");
        }
        else System.out.println("Valor inválido!! Saque NÃO realizado!");
    }

}