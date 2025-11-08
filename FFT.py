import numpy.fft

def stretch(wave, factor):
    freqs = numpy.fft.fft(wave)

    real = freqs.real
    img = freqs.imag

    def f(x):
        total = 0
        for i in range(len(real)):
            total += numpy.cos(real[i] * x) + numpy.sin(img[i] * x)

    return [f(factor * i) for i in range(len(wave))]


arr = []
stretch([1, 2, 3], 1)