import impl.Observador;
import impl.Observavel;
import org.junit.Test;
import static org.junit.Assert.*;

public class TesteObserver {

    @Test
    public void testeInscritos(){
        Observavel aplicativo = new Observavel();
        Observador obs = new Observador(1);
        aplicativo.addObservador(obs);
        assertTrue(!aplicativo.getClientes().isEmpty());
    }

    @Test
    public void teste2Inscritos(){
        Observavel aplicativo = new Observavel();
        Observador obs1 = new Observador(1);
        Observador obs2 = new Observador(2);
        Observador obs3 = new Observador(3);
        aplicativo.addObservador(obs1);
        aplicativo.addObservador(obs2);
        aplicativo.addObservador(obs3);
        aplicativo.removeObservador(obs3);
        assertEquals(aplicativo.getClientes().size(), 2);
    }

    @Test
    public void testTotalDePalavras() {
        Observavel aplicativo = new Observavel();
        Observador obs = new Observador(1);
        aplicativo.addObservador(obs);

        aplicativo.setFrase("Frase teste");

        assertEquals(2, aplicativo.totalPalavras());
    }

    @Test
    public void testQtdPalavrasPares() {
        Observavel aplicativo = new Observavel();
        Observador obs = new Observador(1);
        aplicativo.addObservador(obs);

        aplicativo.setFrase("Frase teste.");

        assertEquals(0, aplicativo.PalavrasQtdParesDeCaracteres());
    }

    @Test
    public void testPalavrasMaiusculas() {
        Observavel aplicativo = new Observavel();
        Observador obs = new Observador(1);
        aplicativo.addObservador(obs);

        aplicativo.setFrase("Frase teste!");

        assertEquals(1, aplicativo.PalavrasMaisculas());
    }
}