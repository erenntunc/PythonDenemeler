# import required libraries
import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv

#frekans default
freq = 44100 #44100 or 48000

# kayıt süresi
duration = 5

# Kaydediciyi verilen değerlerle başlatın
# süre ve örnek sıklığı
recording = sd.rec(int(duration * freq),
				samplerate=freq, channels=2)

# Belirtilen saniye sayısı boyunca sesi kaydedin
sd.wait()

# Scipy kullanarak:

# Bu, NumPy dizisini bir ses dizisine dönüştürecektir
# belirtilen örnekleme frekansına sahip dosya

write("recording0.wav", freq, recording)


# wavio kullanarak:
# NumPy dizisini ses dosyasına dönüştür

wv.write("recording1.wav", recording, freq, sampwidth=2)
