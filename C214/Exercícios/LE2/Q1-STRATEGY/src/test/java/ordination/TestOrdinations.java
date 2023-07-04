package ordination;

import ordination.implementation.SelectionSort;
import ordination.implementation.InsertionSort;
import ordination.implementation.BubbleSort;
import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;
import org.junit.Assert;
import org.junit.Test;

public class TestOrdinations {

    Ordinations ordinations;

    @Test
    public void testeOrdenBubble() {
        ordinations = new ordenBubble();
        assertTrue(ordinations.getOrdination() instanceof BubbleSort);
    }

    @Test
    public void testeOrdenInsertion() {
        ordinations = new ordenInsertion();
        assertTrue(ordinations.getOrdination() instanceof InsertionSort);
    }

    @Test
    public void testeOrdenSelection() {
        ordinations = new ordenSelection();
        assertTrue(ordinations.getOrdination() instanceof SelectionSort);
    }

    @Test
    public void testBubbleSort() {
        ordinations = new ordenBubble();
        int[] arr = {8, 7, 6, 5, 4, 3, 2, 1, 0};

        int[] expected = ordinations.ordenarDados(arr);
        assertEquals(expected[0], 0);
    }

    @Test
    public void testInsertionSort() {
        ordinations = new ordenInsertion();
        int[] arr = {8, 7, 6, 5, 4, 3, 2, 1, 0};

        int[] expected = ordinations.ordenarDados(arr);
        assertEquals(expected[1], 1);
    }

    @Test
    public void testSelectionSort() {
        ordinations = new ordenSelection();
        int[] arr = {64, 34, 28, 12, 22, 11, 90};
        int[] expected = {11, 12, 22, 28, 34, 64, 90};

        Assert.assertArrayEquals(expected, ordinations.ordenarDados(arr));
    }

}