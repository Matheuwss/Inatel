public class Onibus extends Veiculo {

    private int assentos;

    public Onibus(String placa, int ano, int assentos) {
        super(placa, ano);
        this.assentos = assentos;
    }

    public void setAssentos(int assentos) {
        this.assentos = assentos;
    }

    public int getAssentos() {
        return assentos;
    }

    public void exibirDados() {
        System.out.println("DADOS DO VEÍCULO (ÔNIBUS):\n" +
                "PLACA: " + placa + "\n" +
                "Ano de fabricação: " + ano + "\n" +
                "Quantidade de assentos: " + assentos + "\n");
    }
}