import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {

        ArrayList<Veiculo> veiculos = new ArrayList<Veiculo>();
        veiculos.add(new Veiculo("HHH-0000", 2020));
        veiculos.add(new Onibus("HPM-2222", 2018, 30));
        veiculos.add(new Caminhao("MBU-3333", 2010, 10));

        ArrayList<Onibus> onibus = new ArrayList<Onibus>();
        veiculos.add(new Veiculo("XPO-4484", 2019));
        veiculos.add(new Onibus("QUM-3341", 2018, 28));

        ArrayList<Caminhao> caminhoes = new ArrayList<Caminhao>();
        veiculos.add(new Veiculo("XTQ-8889", 2022));
        veiculos.add(new Caminhao("HMU-3348", 2014, 4));


        for (Veiculo veiculo : veiculos) {
            veiculo.exibirDados();
        }

        for (Onibus onibus0 : onibus) {
            onibus0.exibirDados();
        }

        for (Caminhao caminhao : caminhoes) {
            caminhao.exibirDados();
        }
    }
}