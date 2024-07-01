import heapq


class TreeNode:
    def __init__(self, _value, _frequency):
        self.left = None
        self.right = None
        self.value = _value
        self.frequency = _frequency

    def __lt__(self, other):
        return self.frequency < other.frequency

    def __gt__(self, other):
        return self.frequency > other.frequency

    def __eq__(self, other):
        return self.frequency == other.frequency

    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)

    def __ge__(self, other):
        return not self.__lt__(other)

    def __repr__(self):
        return f"{self.value} ({self.frequency})"

    def __add__(self, other):
        return TreeNode(None, self.frequency + other.frequency)

    @staticmethod
    def build_freq_dict(text: str):
        return {letter: text.count(letter) for letter in text}

    @staticmethod
    def build_tree(freq_dict: dict):
        heap = [TreeNode(char, freq) for char, freq in freq_dict.items()]
        heapq.heapify(heap)

        while len(heap) > 1:
            left = heapq.heappop(heap)
            right = heapq.heappop(heap)

            merged = left + right
            merged.left = left
            merged.right = right

            heapq.heappush(heap, merged)

        return heap[0]

    @staticmethod
    def build_codes_dict(node, prefix="", codes_dict={}):
        if node is not None:
            if node.value is not None:  # It's a leaf node
                codes_dict[node.value] = prefix
            TreeNode.build_codes_dict(node.left, prefix + '0', codes_dict)
            TreeNode.build_codes_dict(node.right, prefix + '1', codes_dict)
        return codes_dict

    @staticmethod
    def build_code(text: str, codes_dict):
        code = ""
        for letter in text:
            code += codes_dict.get(letter)
        return code

