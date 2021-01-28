# basic audio io
import wave
from scipy.io import wavfile
import matplotlib.pyplot as plt

FILE = '/Users/Xuan/PycharmProjects/thinkDSP/ThinkDSP/practice/speech_male.wav'
fs, y = wavfile.read(FILE)
plt.plot(y)
plt.show()
print('done')
