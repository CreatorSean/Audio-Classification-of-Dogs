from pydub import AudioSegment
import numpy as np
import pywt
import matplotlib.pyplot as plt

# MP3 파일 로드
mp3_file = 'assets/mp3/1.mp3'
audio = AudioSegment.from_mp3(mp3_file)

# 오디오 데이터를 numpy 배열로 변환 (모노로 변환)
print(mp3_file + " numpy 배열로 변환 수행중...")
samples = np.array(audio.get_array_of_samples())
print(len(samples))

# 웨이블릿 변환 수행
print(mp3_file + " 웨이블릿 변환 수행중...")
scales = np.arange(1, 100)  # 스케일 범위를 조정할 수 있습니다
coeffs, freqs = pywt.cwt(samples, scales, wavelet='morl')
print(coeffs)
print(freqs)

# 결과 시각화
plt.imshow(coeffs, extent=[0, len(samples), 1, 100], cmap='PRGn', aspect='auto',
           vmax=abs(coeffs).max(), vmin=-abs(coeffs).max())
plt.colorbar(label='Magnitude')
plt.title('Wavelet Transform of Audio Signal')
plt.ylabel('Scale')
plt.xlabel('Time')
plt.show()
