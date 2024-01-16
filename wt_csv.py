import librosa
import librosa.display
import pywt
import matplotlib.pyplot as plt
import numpy as np

# 오디오 파일 로드
audio_file = 'assets/wav/6.wav'  # WAV 파일 경로를 지정하세요
signal, sr = librosa.load(audio_file, sr=None)  # 신호 로드

# 웨이블릿 변환 수행
coeffs, freqs = pywt.cwt(signal, scales=np.arange(1, 100), wavelet='morl')

# 결과 시각화
plt.figure(figsize=(10, 6))
plt.imshow(coeffs, extent=[0, 1, 1, 100], cmap='coolwarm', aspect='auto',
           vmax=abs(coeffs).max(), vmin=-abs(coeffs).max())
plt.colorbar(label='Magnitude')
plt.title('Wavelet Transform of Audio Signal')
plt.ylabel('Scale')
plt.xlabel('Time')
plt.show()
