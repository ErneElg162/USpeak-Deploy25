from pydub import AudioSegment

def getAmp(audio, index):
    return int.from_bytes(bleh.get_frame(index), byteorder="little", signed=True)


bleh = AudioSegment.from_wav("test.wav")

for i in range(100000, 110000):
    print(getAmp(bleh, i))