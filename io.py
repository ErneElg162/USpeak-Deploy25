from g2p_en import G2p
from pydub import AudioSegment

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
voice = AudioSegment.from_wav("Phonemes/sentence.wav")
blank_space = AudioSegment.from_wav("Phonemes/45.wav")

try:
    with open("my_file.txt", "r") as file:
        content = file.read()
        endlist = content.split("\n")
        for i in range(len(endlist)):
            endlist[i] = endlist[i].split(", ")
except FileNotFoundError:
    print("Error: The file 'my_file.txt' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")


dict = {"B": 1, "D": 2, "F": 3, "G": 4, "HH": 5, "JH": 6, "K": 7, "L": 8, "M": 9, "N": 10, "P": 11, "R": 12, "S": 13, "T": 14, "V": 15, "W": 16, "Z": 17, "ZH": 18, "CH": 19, "SH": 20, "TH": 21, "DH": 22, "NG": 23, "Y": 24, "AE1": 25, "EY1": 26, "EH1": 27, "IY1": 28, "IH1": 29, "AY1": 30, "AA1": 31, "OW1": 32, "UH1": 33, "AH1": 34, "UW1": 35, "OY1": 36, "AW1": 37, "AH0": 38, "ER1": 41, "A01": 42, " ": 45, ".": 45, "?": 45}

g2p = G2p()

text = input("Enter a sentence: ")
phonemes = g2p(text)
finalAudio = voice[endlist[dict[phonemes[0]]][0]: endlist[dict[phonemes[0]]][1]] * endlist[dict[phonemes[0]]][2]

for i in range(1, len(phonemes)):
    if phonemes[i] == " ":
        finalAudio += blank_space
    else:
        finalAudio += voice[endlist[dict[phonemes[i]]][0]: endlist[dict[phonemes[i]]][1]] * endlist[dict[phonemes[i]]][2]

finalAudio.export("finalAudio")