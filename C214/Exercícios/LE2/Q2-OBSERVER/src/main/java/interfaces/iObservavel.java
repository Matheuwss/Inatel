package interfaces;
import impl.Observador;

public interface iObservavel {
    public void addObservador(Observador obs);
    public void removeObservador(Observador obs);
    public void notifyObservadores();
}