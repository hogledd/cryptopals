# -*- coding: utf-8 -*-
"""
author: hogledd

CryptoPals - Set 1 Challenge 1

"""
import click
import base64

@click.command()
@click.option('--source', prompt='plaintext > ', help='The plaintext you wish to encode.')

def hexbin64(source):
    inbytes = bytearray.fromhex(source)
    encoded = base64.b64encode(inbytes)
    print(encoded)
    return encoded

if __name__ == '__main__':
    hexbin64()