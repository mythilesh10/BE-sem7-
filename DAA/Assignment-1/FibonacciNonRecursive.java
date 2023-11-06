import java.util.Scanner;

//Time complexity=O(n)
//Space complexity=O(1)
public class FibonacciNonRecursive {
    public static long fibonacci(int n) {
        if (n <= 1) {
            return n;
        }
        long a = 0, b = 1, c;
        for (int i = 2; i <= n; i++) {
            c = a + b;
            a = b;
            b = c;
        }
        return b;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the value of n for the Fibonacci sequence: ");
        int n = scanner.nextInt();
        scanner.close();
        long startTime = System.nanoTime();
        long result = fibonacci(n);
        long endTime = System.nanoTime();
        long timeElapsed = endTime - startTime;
        long size = Runtime.getRuntime().totalMemory() - Runtime.getRuntime().freeMemory();
        System.out.println("Fibonacci of " + n + " is: " + fibonacci(n));
        System.out.println("Time taken for execution in nanoseconds: " + timeElapsed);
        System.out.println("Space complexity: " + size + " bytes");
    }
}
