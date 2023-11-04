import java.util.*;

public class KnapsackProblem {

    public static int knapsack(int W, int[] wt, int[] val, int n) {
        int[][] K = new int[n + 1][W + 1];

        for (int i = 0; i <= n; i++) {
            for (int w = 0; w <= W; w++) {
                if (i == 0 || w == 0) {
                    K[i][w] = 0;
                } else if (wt[i - 1] <= w) {
                    K[i][w] = Math.max(val[i - 1] + K[i - 1][w - wt[i - 1]], K[i - 1][w]);
                } else {
                    K[i][w] = K[i - 1][w];
                }
            }
        }
        return K[n][W];
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the number of items: ");
        int n = scanner.nextInt();
        int[] val = new int[n];
        int[] wt = new int[n];
        System.out.println("Enter the values and weights of the items:");
        for (int i = 0; i < n; i++) {
            System.out.print("Value of item " + (i + 1) + ": ");
            val[i] = scanner.nextInt();
            System.out.print("Weight of item " + (i + 1) + ": ");
            wt[i] = scanner.nextInt();
        }
        System.out.print("Enter the maximum weight the knapsack can hold: ");
        int W = scanner.nextInt();
        scanner.close();
        System.out.println("The maximum value that can be obtained is: " + knapsack(W, wt, val, n));
    }
}
