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

def findMinInRange(v_list, t, target):
    slope = v_list[t] - v_list[t-1]
    val = (target-v_list[t])**2
    index = t
    for i in range(250):
        if (t-i<0 or t+i>=len(v_list)):
            break
        val1 = 2*(target-v_list[t-i])**2 + (v_list[t-i] - v_list[t-i-1])**2
        val2 = 2*(target-v_list[t+i])**2 + (v_list[t+i] - v_list[t+i-1])**2
        if val1<val and math.copysign(1, v_list[t-i] - v_list[t-i-1]) == math.copysign(1, slope):
            val = val1
            index = t-i
        if val2 < val and math.copysign(1, v_list[t+i] - v_list[t+i-1]) == math.copysign(1, slope):
            val = val2
            index = t+i
    return index

bounds = []

voice = AudioSegment.from_wav("Phonemes/sentence.wav")
v_arr = getArrayFromSegment(voice)
print(len(v_arr))

for p_num in range (45):
    phon = AudioSegment.from_wav("Phonemes/" + str(p_num) + ".wav")
    p_arr = getArrayFromSegment(phon)
    print(len(p_arr))

    temp_r = getAvgRatio(p_arr, v_arr, 0)
    lowestStart = 0
    lowestValue = calcError(v_arr, p_arr, temp_r, 0)

    for t in range(0, len(v_arr) - len(p_arr) + 1, 5):
        r = getAvgRatio(p_arr, v_arr, t)
        err = calcError(v_arr, p_arr, r, t)

        if r <= 3 and r >= 0 and err < lowestValue:
            lowestValue = err
            lowestStart = t

    lowestEnd = lowestStart + len(p_arr)
    print(lowestStart, v_arr[lowestStart])
    print(lowestEnd, v_arr[lowestEnd])
    lowestEnd = findMinInRange(v_arr, lowestEnd, v_arr[lowestStart])
    print(lowestEnd, v_arr[lowestEnd])
    print(lowestValue)

    t1 = int((lowestStart / voice.frame_count()) * len(voice))
    t2 = int((lowestEnd / voice.frame_count()) * len(voice))

    bounds.append([t1, t2])

output = voice[bounds[0][0] : bounds[0][1]]
output += voice[bounds[1][0] : bounds[1][1]] * 3
output += voice[bounds[2][0] : bounds[2][1]] * 2
output.export("output.wav")

output3 = voice[bounds[2][0] : bounds[2][1]]
output3.export("output3.wav")