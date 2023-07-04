public class Principal {

    public static void main(String[] args) {

        Funcionario[] funcionarios = new Funcionario[10];

        GerenteRegional g1 = new GerenteRegional();
        g1.matricula = 1111;
        g1.nome = "Matheus";
        g1.salario = 2000;
        g1.setDepartamento("Financeiro");
        g1.carro.setCor("Preto");
        g1.carro.setMarca("Ford");

        Vendedor v1 = new Vendedor();
        v1.matricula = 2222;
        v1.nome = "Carlos";
        v1.salario = 3000;
        v1.setTotalComissao(0);
        v1.carro.setMarca("Vermelho");
        v1.carro.setMarca("Chevrolet");

        Contador c1 = new Contador();
        c1.matricula = 2222;
        c1.nome = "Carlos";
        c1.salario = 3000;
        c1.setRamal(36531326);
        c1.carro.setMarca("Vermelho");
        c1.carro.setMarca("Volkswagen");

        funcionarios[0] = g1;
        funcionarios[1] = v1;
        funcionarios[2] = c1;

        for(Funcionario funcionario:funcionarios){
            if (funcionario instanceof GerenteRegional){
                GerenteRegional gerente = (GerenteRegional) funcionario; //Casting
                gerente.recebeSalario();
                gerente.promoveFuncionario();
                gerente.agendaReuniao("Definir novas metas");
                gerente.fechaVenda(200);
                gerente.mostraInfo();
                System.out.println();
            }

            if (funcionario instanceof Vendedor){
                Vendedor vendedor = (Vendedor) funcionario; //Casting
                vendedor.recebeSalario();
                vendedor.fechaVenda(200);
                vendedor.mostraInfo();
                System.out.println();
            }

            if (funcionario instanceof Contador){
                Contador contador = (Contador) funcionario; //Casting
                contador.recebeSalario();
                contador.cadastraDespesa("Reformas");
                contador.mostraInfo();
                System.out.println();
            }
        }

        System.out.println("Foram cadastrados " + Funcionario.contador + " funcionários");
    }
}