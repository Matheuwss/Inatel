package poo_projetoFinal;

public class Cliente {

    private int idCliente;
    private String cpfCliente;
    private String endCliente;
    private String telCliente;
    private String nomeCliente;
    static int qtdClientes = 0;

    public Cliente(String nomeCliente, String cpfCliente, String endCliente, String telCliente) {
        super();
        qtdClientes++;
        this.idCliente = qtdClientes;
        this.cpfCliente = cpfCliente;
        this.endCliente = endCliente;
        this.nomeCliente = nomeCliente;
        this.telCliente = telCliente;
    }

    //Getters e setters
    public int getIdCliente() {
        return idCliente;
    }

    public void setIdCliente(int idCliente) {
        this.idCliente = idCliente;
    }

    public String getNomeCliente() {
        return nomeCliente;
    }

    public void setNomeCliente(String nomeCliente) {
        this.nomeCliente = nomeCliente;
    }

    public String getCpfCliente() {
        return cpfCliente;
    }

    public void setCpfCliente(String cpfCliente) {
        this.cpfCliente = cpfCliente;
    }

    public String getEndCliente() {
        return endCliente;
    }

    public void setEndCliente(String endCliente) {
        this.endCliente = endCliente;
    }

    public String getTelCliente() {
        return telCliente;
    }

    public void setTelCliente(String endCliente) {
        this.telCliente = telCliente;
    }


    public void updateCliente(String nome, String tel, String end){
        setNomeCliente(nome);
        setTelCliente(tel);
        setEndCliente(end);
    }

}