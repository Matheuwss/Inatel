public class Vendedor extends Funcionario implements Venda {

    private double totalComissao;

    //Construtores


    @Override
    public void recebeSalario() {
        System.out.println("O vendedor " + nome + " recebeu seu salário de " + salario + " reais");
    }

    public void mostraInfo(){
        super.mostrarInfo();
        System.out.println("Comissão: " + totalComissao);
    }

    @Override
    public void fechaVenda(double valorVenda) {
        totalComissao += 20 / 100.0 * valorVenda;
    }

    //Getters and Setters
    public void setTotalComissao(double totalComissao) {
        this.totalComissao = totalComissao;
    }

}