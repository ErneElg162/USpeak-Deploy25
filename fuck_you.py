from pydub import AudioSegment
import math


def getAmp(audio: AudioSegment, index: int) -> int:
    return int.from_bytes(audio.get_frame(index), byteorder="little", signed=True)

def getArrayFromSegment(segment: AudioSegment):
    toReturn = []
    for i in range(int(segment.frame_count())):
        toReturn.append(getAmp(segment, i))
    return toReturn

def calcError(v, phoenemeArray, r, t):
    err = 0
    n = len(phoenemeArray)
    for i in range(n):
        err += (r * v[i + t] - phoenemeArray[i]) ** 2
    return err

def getAvgRatio(p_list, v_list, v_start_i):
    total_ratio = 0
    n = 0

    for i in range(len(p_list)):
        if v_list[v_start_i + i] != 0:
            total_ratio += p_list[i]/v_list[v_start_i + i]
            n += 1

    return total_ratio / n

h = 1 #not used yet, this is the amount the samples will be stretched horizontally using fft
h = 2

phon = AudioSegment.from_wav("Phonemes/25.wav")
p_arr = getArrayFromSegment(phon)
voice = AudioSegment.from_wav("Phonemes/cat2.wav")
v_arr = getArrayFromSegment(voice)

temp_r = getAvgRatio(p_arr, v_arr, 0)
lowestStart = 0
lowestValue = calcError(v_arr, p_arr, temp_r, 0)

for t in range(0, len(v_arr) - len(p_arr) + 1):
    r = getAvgRatio(p_arr, v_arr, t)
    err = calcError(v_arr, p_arr, r, t)
    if err < lowestValue:
        lowestValue = err
        lowestStart = t

lowestEnd = lowestStart + len(p_arr)
print(lowestStart)
print(lowestEnd)

finalSample = voice[lowestStart: lowestEnd] * 100
finalSample.export("voice.wav")

for i in range(lowestStart, lowestEnd):
    print(v_arr[i])