public class Caminhao extends Veiculo {

    private int eixos;

    public Caminhao(String placa, int ano, int eixos) {
        super(placa, ano);
        this.eixos = eixos;
    }

    public void setEixos(int eixos) {
        this.eixos = eixos;
    }

    public int getEixos() {
        return eixos;
    }

    public void exibirDados() {
        System.out.println("DADOS DO VEÍCULO (CAMINHÃO):\n" +
                           "PLACA: " + placa + "\n" +
                           "Ano de fabricação: " + ano + "\n" +
                           "Quantidade de eixos: " + eixos + "\n");

    }
}