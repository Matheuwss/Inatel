public class Contador extends Funcionario implements Despesa {

    private int ramal;

    //Construtores

    @Override
    public void recebeSalario() {
        System.out.println("O contador " + nome + " recebeu seu salário de " + salario + " reais");
    }

    public void mostraInfo(){
        super.mostrarInfo();
        System.out.println("Ramal: " + ramal);
    }

    @Override
    public void cadastraDespesa(String despesa) {
        System.out.println("Foi cadastrada uma nova despesa: " + despesa);
    }

    //Getters and Setters
    public void setRamal(int ramal) {
        this.ramal = ramal;
    }

}