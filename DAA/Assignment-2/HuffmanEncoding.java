import java.util.*;

class HuffmanNode {
    int data;
    char c;
    HuffmanNode left;
    HuffmanNode right;
}

class MyComparator implements Comparator<HuffmanNode> {
    public int compare(HuffmanNode x, HuffmanNode y) {
        return x.data - y.data;
    }
}

public class HuffmanEncoding {

    public static void printCode(HuffmanNode root, String s) {
        if (root.left == null && root.right == null && Character.isLetter(root.c)) {
            System.out.println(root.c + ":" + s);
            return;
        }
        printCode(root.left, s + "0");
        printCode(root.right, s + "1");
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the string to encode: ");
        String s = scanner.nextLine();
        scanner.close();

        int[] charFreq = new int[256];
        for (char c : s.toCharArray()) {
            charFreq[c]++;
        }

        PriorityQueue<HuffmanNode> pq = new PriorityQueue<>(new MyComparator());

        for (int i = 0; i < 256; i++) {
            if (charFreq[i] > 0) {
                HuffmanNode hn = new HuffmanNode();
                hn.c = (char) i;
                hn.data = charFreq[i];
                hn.left = null;
                hn.right = null;
                pq.add(hn);
            }
        }

        HuffmanNode root = null;
        while (pq.size() > 1) {
            HuffmanNode x = pq.peek();
            pq.poll();
            HuffmanNode y = pq.peek();
            pq.poll();
            HuffmanNode f = new HuffmanNode();
            f.data = x.data + y.data;
            f.c = '-';
            f.left = x;
            f.right = y;
            root = f;
            pq.add(f);
        }
        System.out.println("Huffman Codes are : ");
        printCode(root, "");
    }
}
