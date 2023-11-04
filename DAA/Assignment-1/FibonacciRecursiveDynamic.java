import java.util.Scanner;

//Time complexity = O(2^n)
//Space complexity = O(n)
public class FibonacciRecursiveDynamic {
    public static long fibonacci(int n) {
        if (n <= 1) {
            return n;
        }
        return fibonacci(n - 1) + fibonacci(n - 2);
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the value of n for the Fibonacci sequence: ");
        int n = scanner.nextInt();
        scanner.close();
        System.out.println("Fibonacci of " + n + " is: " + fibonacci(n));
    }
}
