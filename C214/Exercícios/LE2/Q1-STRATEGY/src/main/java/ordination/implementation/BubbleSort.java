package ordination.implementation;
import ordination.Ordination;

public class BubbleSort implements Ordination {

    @Override
    public int[] ordenarDados(int[] arr) {
        boolean swapped = true;
        while (swapped) {
            swapped = false;
            for (int i = 0; i < arr.length - 1; i++) {
                if (arr[i] > arr[i + 1]) {
                    int aux = arr[i];
                    arr[i] = arr[i + 1];
                    arr[i + 1] = aux;
                    swapped = true;
                }
            }
        }
        return arr;
    }
}