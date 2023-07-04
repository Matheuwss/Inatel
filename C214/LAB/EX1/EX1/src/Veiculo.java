public class Veiculo {

    protected String placa;
    protected int ano;

    public Veiculo(){
    }

    public Veiculo(String placa, int ano) {
        this.placa = placa;
        this.ano = ano;
    }

    public void setPlaca(String placa) {
        this.placa = placa;
    }

    public void setAno(int ano) {
        this.ano = ano;
    }

    public void setAno(String ano) {
        this.ano = Integer.parseInt(ano);
    }

    public String getPlaca() {
        return placa;
    }

    public int getAno() {
        return ano;
    }


    public void exibirDados() {
        System.out.println("DADOS DO VEÍCULO (COMUM):\n" +
                "PLACA: " + placa + "\n" +
                "Ano de fabricação: " + ano + "\n");
    }
}