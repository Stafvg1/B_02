import numpy as np
import matplotlib.pyplot as plt
#constants
sampling_rate = 1 #Hz
N = 100  #amount of samples
t = np.arange(N)
margin = sampling_rate/N

#wave creation
#frequency = 0.15
#wave = np.sin(frequency*2*np.pi*t)

#fft
fft = np.fft.fftshift(np.fft.fft(wave*np.hamming(N)))
fftmag = np.abs(fft)
fftangle = np.angle(fft)

#plotting
t = np.arange(sampling_rate/-2, sampling_rate/2, sampling_rate/N)
plt.plot(t,fftmag,".-")
plt.axis([-(sampling_rate/2+margin), sampling_rate/2+margin,-1, max(fftmag)*1.1])
plt.ylabel("Magnitude")
plt.xlabel("Time(s)")
plt.show()

