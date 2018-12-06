from base64 import urlsafe_b64encode


def encode_base64_str(string):
    string = string.encode('ascii')
    encoded_string = urlsafe_b64encode(string)
    return encoded_string.decode('ascii')


if __name__ == '__main__':

    print(encode_base64_str("test"))
