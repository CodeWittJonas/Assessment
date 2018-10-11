# Please do not modify this part of the code!
import string
from random import shuffle

alphabet = string.ascii_lowercase


def print_cipher(key):
    for i in range(len(key)):
        print(f'{alphabet[i]} - {key[i]}')


def shuffle_letters(letters):
    scrambled = list(letters)
    shuffle(scrambled)
    return ''.join(scrambled)


# ======== You can define the encrypt and decrypt function here. Do not write any code other than your solution here! ================





# ====================================================================================================================================


if __name__ == '__main__':
    # Here you can write code to test your function. Code you write here is solely for testing and will not be evaluated.
    """
        Keys to play around with. You can generate new ones if you want, using the 'shuffle_letters' function!
        Also try calling print_cipher with one of these keys to see how the mapping works.
        
        key_1 = 'wfrjucxmeziqpagbsnlkytvhod'
    
        key_2 = 'vzfpbncyrosdwjqumhikxlegat'
    
        key_3 = 'gcbmkezpsiaxdqvhonjftulyrw'
        
        print_cipher(key_1)
    
        plain_text = input('Please enter text to encrypt: ').lower() # input: 'hello'
    
        cipher = encrypt(plain_text, key) # cipher = 'muqqg'
    
        print(f'Encrypted text:\t "{cipher}"') # prints Encrypted text:     "muqqg"
    
        plain = decrypt(cipher, key) # plain = 'hello'
    
        print(f'Decrypted ciphertext:\t "{plain}"') # prints Decrypted ciphertext:   "hello"
        """
