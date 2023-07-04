import impl.Observavel;
import impl.Observador;

import java.util.Scanner;

public class Aplicativo {
    public static void main(String[] args) {

        //Criando o observável (subject) aplicativo.
        Observavel aplicativo = new Observavel();

        //Criando observadores e fazendo a inscrição no aplicativo.
        Observador obs = new Observador(1);
        aplicativo.addObservador(obs);

        //Recebendo a frase
        Scanner scanner = new Scanner(System.in);

        System.out.print("Digite a frase: ");
        String input = scanner.nextLine();

        aplicativo.setFrase(input);

        scanner.close();

    }
}