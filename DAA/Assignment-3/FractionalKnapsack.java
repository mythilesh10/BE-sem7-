import java.util.*;

class Item {
    int value, weight;

    public Item(int value, int weight) {
        this.value = value;
        this.weight = weight;
    }
}

public class FractionalKnapsack {

    public static double fractionalKnapsack(int capacity, Item[] items) {
        Arrays.sort(items, (a, b) -> ((b.value / b.weight) - (a.value / a.weight)));
        double totalValue = 0;
        for (Item item : items) {
            if (capacity >= item.weight) {
                totalValue += item.value;
                capacity -= item.weight;
            } else {
                totalValue += ((double) item.value / item.weight) * capacity;
                break;
            }
        }
        return totalValue;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the capacity of the knapsack: ");
        int capacity = scanner.nextInt();
        System.out.print("Enter the number of items: ");
        int n = scanner.nextInt();
        Item[] items = new Item[n];
        System.out.println("Enter the value and weight of each item:");
        for (int i = 0; i < n; i++) {
            System.out.print("Value of item " + (i + 1) + ": ");
            int value = scanner.nextInt();
            System.out.print("Weight of item " + (i + 1) + ": ");
            int weight = scanner.nextInt();
            items[i] = new Item(value, weight);
        }
        scanner.close();
        double totalValue = fractionalKnapsack(capacity, items);
        System.out.println("The maximum value that can be obtained is: " + totalValue);
    }
}
