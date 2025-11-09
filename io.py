"""""
yo dawg, if the downloads is kickin yo ass 'n shit then try the followingL:

import nltk
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context 
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

nltk.download() # <--with whatever you need to straight up download in here (cmudict, averaged_perceptron_tagger)

"""""

dict = {}


from g2p_en import G2p
import nltk

inp = ""

g2p = G2p()
while inp != "quit":
    inp = input("Enter a sentence: ")
    print(g2p(inp))
