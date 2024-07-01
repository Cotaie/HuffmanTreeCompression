from node import TreeNode
from input import text
import json
import struct


def _serialize_codes_dict(codes_dict: dict):
    return json.dumps(codes_dict)

def _get_padding_size(code: str):
    return 8 - len(code) % 8


def main():

    freq_dict = TreeNode.build_freq_dict(text)
    tree = TreeNode.build_tree(freq_dict)
    codes_dict = TreeNode.build_codes_dict(tree)
    codes_dict_json = _serialize_codes_dict(codes_dict)
    code = TreeNode.build_code(text, codes_dict)
    code_padding = code.ljust(len(code) + _get_padding_size(code), "0")
    padded_length = len(code) + _get_padding_size(code)

    print(freq_dict)
    print(tree)
    print(codes_dict)
    print(codes_dict_json)
    print(code)
    print(code_padding)
    print("Text len: ", len(text))

    with open("output.bin", 'wb') as file:
        #file.write(str(len(codes_dict_json)).encode("utf-8"))
        #file.write(struct.pack("B", len(codes_dict_json)))
        file.write(struct.pack("I", 60000))
        for key, code in codes_dict.items():
            file.write(key.encode("utf-8"))
            file.write(struct.pack("B", len(code)))
            char_code_padding_value = code.ljust(len(code) + _get_padding_size(code), "0")
            for i in range(0,len(code) + _get_padding_size(code), 8):
                byte = char_code_padding_value[i:i+8]
                file.write(struct.pack("B", int(byte, 2)))
        #file.write(codes_dict_json.encode("utf-8"))
        file.write(struct.pack("B", _get_padding_size(code)))
        for i in range(0, padded_length, 8):
            byte = code_padding[i:i+8]
            file.write(struct.pack("B", int(byte, 2)))


main()
