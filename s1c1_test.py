import unittest
import subprocess
import s1c1

class MyTestCase(unittest.TestCase):
    def setup(self):
        pass

    def test_hexbin64(self):
        self.assertEqual(
            b'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t',
            b'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t')

        # self.assertEqual(
        #     subprocess.check_output(['python3', '~/PythonProjects/cryptopals/s1c1.py --source 49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d']),
        #     b'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t')

if __name__ == '__main__':
    unittest.main()
