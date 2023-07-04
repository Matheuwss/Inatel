package impl;
import interfaces.iObservador;

public class Observador implements iObservador {

    int id;

    public Observador(int id) {
        this.id = id;
    }

    @Override
    public void update(Observavel aplicativo) {
        System.out.println("Cliente: "+ this.id);
        System.out.println("Frase: " + aplicativo.getFrase());
        System.out.println("Total de palavras: " + aplicativo.totalPalavras());
        System.out.println("Palavras com quantidades pares de caracteres: " + aplicativo.PalavrasQtdParesDeCaracteres());
        System.out.println("Palavras começadas com maiúsculas: " + aplicativo.PalavrasMaisculas());
    }
}