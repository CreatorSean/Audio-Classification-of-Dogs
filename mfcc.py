import matplotlib.pyplot as plt
import librosa.display
import librosa
import numpy as np

path = 'assets/wav/1.wav'
sample_rate = 44100

x = librosa.load(path)[0]
S = librosa.feature.melspectrogram(y=x, sr=sample_rate, n_mels=128)
log_S = librosa.power_to_db(S, ref=np.max)
mfcc = librosa.feature.mfcc(S=log_S, n_mfcc=20)

delta2_mfcc = librosa.feature.delta(mfcc, order=2)

plt.figure(figsize=(12, 4))
librosa.display.specshow(delta2_mfcc)
plt.ylabel('MFCC coeffs')
plt.xlabel('Time')
plt.title('MFCC')
plt.colorbar()
plt.tight_layout()

plt.show()