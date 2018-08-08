"""
@author: hogledd
@date: 08/08/18

Cryptopals Set 1 Challenge 3


"""

import click

@click.command()
@click.option('--ciphertext', prompt='ciphertext > ', help='The ciphertext you wish to denrypt.')

def score_try:
    # check frequency of letters in sample
    # compare frequencies for common letters
    # the closer (e.g. standard deviations) to well known english frequencies the better the score (e.g. 0-100)
    # return score

def decrypt(ciphertext):
    print(ciphertext)
    # attempt a key (i.e. brute force)
    # go get a score
    # show results for best scores

if __name__ == '__main__':
    decrypt()
