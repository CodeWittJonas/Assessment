from urllib import request


def decode_base64_str(encoded_str):
    result = request.urlopen(f"https://httpbin.org/base64/{encoded_str}").read().decode('ascii')
    return result


if __name__ == '__main__':
    print(decode_base64_str("SFRUUEJJTiBpcyBhd2Vzb21l"))
