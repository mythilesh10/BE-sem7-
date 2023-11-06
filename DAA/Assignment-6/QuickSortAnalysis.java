import java.util.Arrays;
import java.util.Random;
import java.util.Scanner;
import java.util.*;

public class QuickSortAnalysis {
    // Deterministic Quicksort
    static int partition(List<Integer> arr, int low, int high) {
        int pivot = arr.get(low);
        int i = low;
        int j = high;
        while (i < j) {
            while (arr.get(i) <= pivot && i <= high - 1) {
                i++;
            }
            while (arr.get(j) > pivot && j >= low + 1) {
                j--;
            }
            if (i < j) {
                int temp = arr.get(i);
                arr.set(i, arr.get(j));
                arr.set(j, temp);
            }
        }
        int temp = arr.get(low);
        arr.set(low, arr.get(j));
        arr.set(j, temp);
        return j;
    }

    static void qs(List<Integer> arr, int low, int high) {
        if (low < high) {
            int pIndex = partition(arr, low, high);
            qs(arr, low, pIndex - 1);
            qs(arr, pIndex + 1, high);
        }
    }

    public static List<Integer> deterministicQuickSort(List<Integer> arr) {
        qs(arr, 0, arr.size() - 1);
        return arr;
    }

    // Randomized Quicksort
    static int randomizedPartition(List<Integer> arr, int low, int high) {
        Random rand = new Random();
        int randomIndex = rand.nextInt(high - low) + low;
        int temp = arr.get(randomIndex);
        arr.set(randomIndex, arr.get(high));
        arr.set(high, temp);
        return partition(arr, low, high);
    }

    static void randomizedQs(List<Integer> arr, int low, int high) {
        if (low < high) {
            int pIndex = randomizedPartition(arr, low, high);
            randomizedQs(arr, low, pIndex - 1);
            randomizedQs(arr, pIndex + 1, high);
        }
    }

    public static List<Integer> randomizedQuickSort(List<Integer> arr) {
        randomizedQs(arr, 0, arr.size() - 1);
        return arr;
    }
}
