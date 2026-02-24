import numpy as np
import matplotlib.pyplot as plt

#constants
sampling_rate = 1 #Hz
window_size = 100  #amount of samples/window size

overlap = 0.5 #overlap between windows in percent
step = window_size-int(window_size*overlap) #step size between windows

num_windows = int((len(t)-window_size/step)+1

spectogram = []

#fft
for i in range(num_windows):
    start = i*step
    end = start+window_size
    segment = wave[start:end]   

    fft = np.fft.fftshift(np.fft.fft(segment*np.hamming(window_size)))
    
    fftmag = np.abs(fft)
    fftangle = np.angle(fft)

    spectogram.append(fftmag)
