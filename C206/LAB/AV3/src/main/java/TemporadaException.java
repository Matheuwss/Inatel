public class TemporadaException extends Exception {

    public void temporadaIncorreta(){
        System.out.println("Não é possível cadastrar seriados com menos de 1 temp.");
    }

}