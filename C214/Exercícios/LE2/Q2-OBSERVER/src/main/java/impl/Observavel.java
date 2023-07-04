package impl;

import interfaces.iObservavel;
import java.util.ArrayList;
import java.util.List;

public class Observavel implements iObservavel {

    private List<Observador> clientes;
    private String frase;

    public Observavel() {
        clientes = new ArrayList<Observador>();
    }

    @Override
    public void addObservador(Observador obs) {
        clientes.add(obs);
    }

    @Override
    public void removeObservador(Observador obs) {
        if(clientes.contains(obs))
            clientes.remove(obs);
    }

    @Override
    public void notifyObservadores() {
        for (Observador observador : clientes) {
            observador.update(this);
        }
    }

    //Método chamado sempre que os valores se modificacam
    private void novasMedidas() {
        notifyObservadores();
    }

    public String[] quebrarFraseEmPalavras() {
        frase = frase.replace(".", "");
        frase = frase.replace(",", "");
        frase = frase.replace("?", "");
        frase = frase.replace("!", "");
        String[] palavras = frase.split(" ");
        return palavras;
    }

    public int totalPalavras() {
        String[] palavras = quebrarFraseEmPalavras();
        int totalPalavras = palavras.length;
        return totalPalavras;
    }

    public int PalavrasQtdParesDeCaracteres() {
        String[] palavras = quebrarFraseEmPalavras();
        int palavrasQtdParesDeCaracteres = 0;

        for (String p : palavras) {
            if (p.length() % 2 == 0) {
                palavrasQtdParesDeCaracteres++;
            }
        }
        return palavrasQtdParesDeCaracteres;
    }

    public int PalavrasMaisculas() {
        String[] palavras = quebrarFraseEmPalavras();
        int palavrasMaiusculas = 0;

        for (String p : palavras) {
            if (Character.isUpperCase(p.charAt(0))) {
                palavrasMaiusculas++;
            }
        }
        return palavrasMaiusculas;
    }

    public void setFrase(String frase) {
        System.out.println("\n---------- NOVA FRASE PARA ANÁLISE ----------\n");
        this.frase = frase;
        novasMedidas();
    }

    public void setClientes(List<Observador> clientes) {
        this.clientes = clientes;
    }

    public String getFrase() {
        return frase;
    }

    public List<Observador> getClientes() {
        return clientes;
    }

}