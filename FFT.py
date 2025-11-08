import numpy as np
import numpy.fft
from pydub import AudioSegment

def stretch(wave, factor):
    freqs = numpy.fft.fft(wave)
    N = len(wave)

    def f(x):
        total = 0

        for m in range(len(freqs)):
            total += freqs[m] * np.exp(2j * np.pi * m * x / N)

        # if(factor == 1/0.8):
        #     print(total)

        return total / N

    return [round(f(i / factor).real) for i in range(int(factor * len(wave)))]


def getAmp(audio: AudioSegment, index: int) -> int:
    return int.from_bytes(audio.get_frame(index), byteorder="little", signed=True)


def getArrayFromSegment(segment: AudioSegment):
    toReturn = []
    for i in range(int(segment.frame_count())):
        toReturn.append(getAmp(segment, i))
    return toReturn



arr = getArrayFromSegment(AudioSegment.from_wav("Phonemes/1.wav"))
newArr = stretch(arr, 1/0.7)
oriArr = stretch(newArr, 0.7)

print(arr)
print(newArr)
print(oriArr)