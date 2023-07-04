public class Seriado implements Comparable<Seriado> {

    private String nome;
    private String streaming;
    private int temporadas, ano;

    //Construtores
    public Seriado() {}

    public Seriado(String nome, String streaming, int temporadas, int ano) {
        this.nome = nome;
        this.streaming = streaming;
        this.ano = ano;

        //tratamento
        try{
            if(temporadas < 1){
                throw new TemporadaException();
            }
            this.temporadas = temporadas;

        } catch (TemporadaException e) {
            e.temporadaIncorreta();
        }
    }

    //Getters e setters
    public String getNome() {
        return nome;
    }
    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getStreaming() {
        return streaming;
    }
    public void setStreaming(String streaming) {
        this.streaming = streaming;
    }

    public int getTemporadas() {
        return temporadas;
    }

    public void setTemporadas(int temporadas) {
        //tratamento
        try{
            if(temporadas < 1){
                throw new TemporadaException();
            }
            this.temporadas = temporadas;

        } catch (TemporadaException e) {
            e.temporadaIncorreta();
        }
    }

    public int getAno() {
        return ano;
    }
    public void setAno(int ano) {
        this.ano = ano;
    }

    @Override
    public int compareTo(Seriado s) {
        return nome.compareTo(s.nome);
    }

}