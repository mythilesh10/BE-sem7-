import heapq
from collections import defaultdict, Counter
import time

start = time.time()

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(data):
    # Count the frequency of each character in the input data
    freq_dict = Counter(data)

    # Create a priority queue (min heap) to store HuffmanNodes
    heap = [HuffmanNode(char, freq) for char, freq in freq_dict.items()]
    heapq.heapify(heap)

    # Build the Huffman tree
    while len(heap) > 1:
        left_node = heapq.heappop(heap)
        right_node = heapq.heappop(heap)
        merged_node = HuffmanNode(None, left_node.freq + right_node.freq)
        merged_node.left = left_node
        merged_node.right = right_node
        heapq.heappush(heap, merged_node)

    return heap[0]

def build_huffman_codes(node, current_code, huffman_codes):
    if node is None:
        return

    if node.char is not None:
        huffman_codes[node.char] = current_code
        return

    build_huffman_codes(node.left, current_code + "0", huffman_codes)
    build_huffman_codes(node.right, current_code + "1", huffman_codes)

def huffman_encoding(data):
    if not data:
        return None, None

    root = build_huffman_tree(data)
    huffman_codes = {}
    build_huffman_codes(root, "", huffman_codes)

    encoded_data = "".join(huffman_codes[char] for char in data)
    return encoded_data, root

def huffman_decoding(encoded_data, root):
    if not encoded_data:
        return None

    decoded_data = []
    current_node = root

    for bit in encoded_data:
        if bit == "0":
            current_node = current_node.left
        else:
            current_node = current_node.right

        if current_node.char is not None:
            decoded_data.append(current_node.char)
            current_node = root

    return "".join(decoded_data)

# Example usage
data = "this is an example for huffman encoding"
encoded_data, huffman_tree = huffman_encoding(data)
decoded_data = huffman_decoding(encoded_data, huffman_tree)

print("Original data:", data)
print("Encoded data:", encoded_data)
print("Decoded data:", decoded_data)

end = time.time()
print("\nExecution time is: {}ms".format((end-start)*10**3))