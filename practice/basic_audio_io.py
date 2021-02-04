# basic audio io
import scipy.io.wavfile as wav
import scipy.signal as signal
import numpy as np
from matplotlib import pyplot as plt

FILE = '/Users/Xuan/PycharmProjects/thinkDSP/ThinkDSP/practice/speech_male.wav'
fs, y = wav.read(FILE)
f, t, Zxx = signal.stft(y, fs=fs)
plt.figure()
plt.subplot(2, 1, 1)
plt.plot(y)
plt.subplot(2, 1, 2)
plt.pcolormesh(t, f, np.abs(Zxx))
plt.show()

import wave
import scipy.signal
from scipy.io import wavfile
import matplotlib.pyplot as plt

#
# fs, y = wavfile.read(FILE)
#
# Y = scipy.signal.stft(
#   y,
#   fs=fs,
#   window='hann',
#   nperseg=1024,
#   noverlap=512,
#   nfft=None,
#   detrend=False,
#   return_onesided=True,
#   boundary='zeros',
#   padded=True,
#   axis=-1
# )
#
#
#
# # plt.plot(Y)
# # plt.show()


print('done')
