from pydub import AudioSegment
import numpy as np
import pywt
import matplotlib.pyplot as plt

# MP3 파일 로드
mp3_file = "assets/mp3/2.mp3"
audio = AudioSegment.from_mp3(mp3_file)

print(mp3_file + "numpy로 변환중...")
# 오디오 데이터를 numpy 배열로 변환 (모노로 변환)
samples = np.array(audio.get_array_of_samples())

print(mp3_file + "웨이블릿 실행중...")
# 웨이블릿 변환 수행
coeffs, freqs = pywt.cwt(samples, scales=np.arange(1, 100),wavelet='morl')

# 결과 시각화
plt.imshow(coeffs, extent=[0, 1, 1, 100], cmap='PRGn', aspect='auto',
           vmax=abs(coeffs).max(), vmin=-abs(coeffs).max())
plt.show()