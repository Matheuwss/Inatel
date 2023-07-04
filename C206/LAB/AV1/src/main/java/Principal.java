import java.util.Scanner;

public class Principal {
    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);
        boolean flag = true;
        int n = 0;

        Jogador j1 = new Jogador();
        j1.nome = "Matheus";
        j1.email = "matheusr@gec.inatel.br";

        while(flag) {
            System.out.println("1 - Mostrar informações");
            System.out.println("2 - Adicionar personagem");
            System.out.println("3 - Mostrar Media");
            System.out.println("4 - Calcular Magia");
            System.out.println("5 - Sair");
            n = input.nextInt();

            switch (n) {
                case 1:
                    j1.mostrarInfo();
                    break;

                case 2:
                    Personagem p1 = new Personagem();
                    input.nextLine();
                    System.out.println("Classe do Personagem");
                    p1.classe = input.nextLine();
                    System.out.println("Arma do Personagem");
                    p1.arma = input.nextLine();
                    System.out.println("Nivel do Personagem");
                    p1.nivel = input.nextInt();
                    System.out.println("Poder do Personagem");
                    p1.poder = input.nextDouble();
                    System.out.println("Personagem usa Magia?");
                    p1.usaMagia = input.nextBoolean();
                    j1.adicionaPersonagem(p1);
                    break;

                case 3:
                    j1.mostraMediaNivel();
                    break;

                case 4:
                    int numeroMagia = j1.calculaMagia();
                    System.out.println("Personagens que usam magia " + numeroMagia);
                    break;

                case 5:
                    flag = false;
                    break;

                default:
                    break;
            }
        }
    }

}