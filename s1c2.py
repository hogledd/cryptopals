# -*- coding: utf-8 -*-
"""
@author: hogledd

CryptoPals - Set 1 Challenge 2

"""

import click

@click.command()
@click.option('--source', prompt='plaintext > ', help='The plaintext you wish to encrypt.')
@click.option('--key', prompt='key > ', help='The key to use for encrypting the plaintext.')
def encrypt(source, key):
    cipher_text = list()
    # check for equal length
    if len(source) == len(key):
        # print source and key to standard out
        # print("PLAIN HEXT:", source)
        # print("KEY HEXT:", key)

        # convert source and key from hex to ascii bytes
        input_bytes = bytes.fromhex(source)
        key_bytes = bytes.fromhex(key)

        # print byte results to standard out
        # print("PLAIN TEXT:", input_bytes)
        # print("KEY TEXT:", key_bytes)

        # operate xor on source and key
        mutable_input = bytearray(input_bytes)
        mutable_key = bytearray(key_bytes)

        for a, b in zip(mutable_input, mutable_key):
            cipher_bit = a ^ b
            cipher_text.append(cipher_bit)

        # print cipher text results to standard out
        # print("CIPHER TEXT:", bytes(cipher_text))
        # print("CIPHER HEXT:", bytes(cipher_text).hex())
        print(bytes(cipher_text).hex())

    else:
        print("Key length different")

if __name__ == '__main__':
    encrypt()