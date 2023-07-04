public class GerenteRegional extends Funcionario implements Reuniao, Venda {

    private String departamento;

    //Construtores


    @Override
    public void recebeSalario() {
        System.out.println("O gerente regional " + nome + " recebeu seu salário de " + salario + " reais");
    }

    public void mostraInfo(){
        super.mostrarInfo();
        System.out.println("Departamento: " + departamento);
    }

    public void promoveFuncionario(){
        System.out.println("O gerente regional " + nome + " promoveu um funcionário");
    }

    @Override
    public void agendaReuniao(String motivo) {
        System.out.println("Uma reunião foi agenda pelo seguinte motivo: " + motivo);
    }
    @Override
    public void fechaVenda(double valorVenda) {
        System.out.println("O gerente geral " + nome + " realizou uma venda no valor de " + valorVenda + " reais");
    }

    //Getters and Setters
    public void setDepartamento(String departamento) {
        this.departamento = departamento;
    }

}