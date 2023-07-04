public class Personagem {

    String classe;
    String arma;
    int nivel;
    double poder;
    boolean usaMagia;

    void mostrarInfo() {
        System.out.println("Classe: " + classe);
        System.out.println("Arma: " + arma);
        System.out.println("Nivel: " + nivel);
        System.out.println("Poder: " + poder);
        System.out.println("Magia: " + usaMagia);
    }

}