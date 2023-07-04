package ordination.implementation;
import ordination.Ordination;

public class SelectionSort implements Ordination {

    @Override
    public int[] ordenarDados(int[] arr) {
        for (int fixo = 0; fixo < arr.length - 1; fixo++) {
            int minIndex = fixo;

            for (int i = fixo + 1; i < arr.length; i++) {
                if (arr[i] < arr[minIndex]) {
                    minIndex = i;
                }
            }
            //TROCA ARR[fixo] COM O MENOR ELEMENTO
            int aux = arr[minIndex];
            arr[minIndex] = arr[fixo];
            arr[fixo] = aux;
        }
        return arr;
    }
}