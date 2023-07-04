package br.inatel.cdg;

public class Atendimento {

    private String nomePROFESSOR;
    private String HORARIO;
    private String PERIODO;
    private int SALA;
    //private int[] PREDIO;

    public Atendimento(String nomePROFESSOR, String HORARIO, String PERIODO, int SALA) {
        this.nomePROFESSOR = nomePROFESSOR;
        this.HORARIO = HORARIO;
        this.PERIODO = PERIODO;
        this.SALA = SALA;
    }

    public String getNomePROFESSOR() {
        return nomePROFESSOR;
    }

    public String getHORARIO() {
        return HORARIO;
    }

    public String getPERIODO() {
        return PERIODO;
    }

    public int getSALA() {
        return SALA;
    }

    //MÉTODO QUE CALCULA E RETORNA O PRÉDIO ONDE O ATENDIMENTO OCORRE
    public int getPREDIO(int sala) {
        int predio = (int) Math.ceil(sala/5.0);
        return predio;
    }
}