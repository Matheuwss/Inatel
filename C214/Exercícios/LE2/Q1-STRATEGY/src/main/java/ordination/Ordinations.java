package ordination;

public abstract class Ordinations {

    //COMPOSIÇÃO COM INSTÂNCIA DE ORDENAÇÃO
    protected Ordination ordination;

    //COMPORTAMENTO DELEGADO
    public int[] ordenarDados(int[] vetor) {
        return ordination.ordenarDados(vetor);
    }

    //GETTEER E SETTER
    public Ordination getOrdination() {
        return ordination;
    }

    public void setOrdination(Ordination ordination) {
        this.ordination = ordination;
    }

}