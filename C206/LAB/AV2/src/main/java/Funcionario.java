public abstract class Funcionario {

    public static int contador;
    protected int matricula;
    protected String nome;
    protected double salario;
    Carro carro;

    //Construtores
    public Funcionario(){
        contador++;
        this.carro = new Carro();
    }

    public abstract void recebeSalario();

    public void mostrarInfo(){
        System.out.println("NOME: " + nome);
        System.out.println("SALÁRIO: " + salario);
        System.out.println("MATRÍCULA: " + matricula);
        System.out.println("COR: " + carro.getCor());
        System.out.println("MARCA: " + carro.getMarca());
    }

}