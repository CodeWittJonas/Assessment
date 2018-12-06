from base64_encoder import encode_base64_str as encode
from base64_decoder import decode_base64_str as decode


def verify_encoding_decoding(string):
    original_string = string
    string = encode(string)
    string = decode(string)

    return original_string == string


if __name__ == '__main__':

    verify_encoding_decoding("test")
