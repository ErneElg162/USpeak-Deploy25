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
    if n == 0:
        return -1

    return total_ratio / n


bounds = []

voice = AudioSegment.from_wav("SAMPLE_AUD.wav")
v_arr = getArrayFromSegment(voice)
print(len(v_arr))

scales = [1] * 44

for p_num in range (1, 45):
    print(f"WORKING ON {p_num}")
    if p_num == 39 or p_num == 40 or p_num == 43 or p_num == 44:
        bounds.append([0,0,0])
        continue
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
    print(lowestEnd, v_arr[lowestEnd])
    print(lowestValue)

    t1 = int((lowestStart / voice.frame_count()) * len(voice))
    t2 = int((lowestEnd / voice.frame_count()) * len(voice))

    bounds.append([t1, t2, scales[p_num - 1]])

with open("audio_data.txt", 'w') as file:
    for i in range(44):
        file.write(str(bounds[i][0]) + ", " + str(bounds[i][1]) + ", " + str(bounds[i][2]) + "\n")