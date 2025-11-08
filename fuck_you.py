from pydub import AudioSegment

def getAvgRatio(p_list, v_list, v_start_i):
    total_ratio = 0
    n = 0

    for i in range(len(p_list)):
        if v_list[i] != 0:
            total_ratio += p_list[i]/v_list[v_start_i + i]
            n += 1

    return total_ratio / n

p_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
v_list = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
a = 0

print(getAvgRatio(p_list, v_list, a))
