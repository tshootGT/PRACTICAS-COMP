#practica convolucion
#Tshoot
#201503740

import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import write
import wave

file = wave.open('more than words.wav')
audio = file.readframes(-1)
audio = np.frombuffer (audio, dtype=np.int16)

#plt.plot(audio) #es para scar la primer grafica eliminar el primer numeral
#plt.title('more than words') #es para scar la primer grafica eliminar el primer numeral
#plt.show() #es para scar la primer grafica eliminar el primer numeral

alfa = np.array([1.,0.,0.]) 
audio_modificado = np.convolve(audio, alfa)

audio_modificado = audio_modificado.astype(np.int16)
write('audio_moficado.wav',40000,audio_modificado)

plt.plot(audio_modificado)
plt.title('audio more than words modificada')
plt.show()