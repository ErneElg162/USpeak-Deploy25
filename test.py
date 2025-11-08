from pydub import AudioSegment
from pydub import effects


def getAmp(audio: AudioSegment, index: int) -> int:
    return int.from_bytes(audio.get_frame(index), byteorder="little", signed=True)



d = AudioSegment.from_wav("Phonemes/2.wav")
a = AudioSegment.from_wav("Phonemes/25.wav")

dad = d + a * 3 + d * 3

dad.export("DAD.wav")


"""
numPhonemes = 4

for i in range(1, numPhonemes + 1):
    a = AudioSegment.from_wav(f"Phonemes/{i}.wav") * 1000
    a.export(f"TestWav/{i}.wav")
"""