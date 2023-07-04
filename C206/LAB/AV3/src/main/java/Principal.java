import java.util.Collections;
import java.util.ArrayList;

public class Principal {

    public static void main(String[] args) {

        Seriado s1 = new Seriado("Grey’s Anatomy","Netflix",18,2005);
        Seriado s2 = new Seriado("Os Simpsons","Disney+",33,1989);
        Seriado s3 = new Seriado("Friends","HBO MAX",10,1994);
        Seriado s4 = new Seriado("Game of Thrones","HBO MAX",8,2011);
        Seriado s5 = new Seriado("TEMP < 1", "TESTE", 0, 2000);             //TESTE

        Arquivo arquivo = new Arquivo();
        arquivo.escrever(s1);
        arquivo.escrever(s2);
        arquivo.escrever(s3);
        arquivo.escrever(s4);
        arquivo.escrever(s5);

        ArrayList<Seriado> seriados = new ArrayList<>();
        seriados = arquivo.ler();

        //ORDENANDO - ordem crescente
        Collections.sort(seriados);
        for(Seriado seriado:seriados) {
            System.out.println("Nome: " + seriado.getNome());
            System.out.println("Streaming: " + seriado.getStreaming());
            System.out.println("Temporadas: " + seriado.getTemporadas());
            System.out.println("Ano de Criação: " + seriado.getAno());
            System.out.println(" ");
        }

        System.out.println("------------------------------------------------");

        //ORDENANDO - ordem decrescente
        Collections.reverse(seriados);
        for(Seriado seriado:seriados) {
            System.out.println("Nome: " + seriado.getNome());
            System.out.println("Streaming: " + seriado.getStreaming());
            System.out.println("Temporadas: " + seriado.getTemporadas());
            System.out.println("Ano de Criação: " + seriado.getAno());
            System.out.println(" ");
        }

    }
}