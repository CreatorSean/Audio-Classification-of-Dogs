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

# 특정 스케일에서 웨이블릿 계수 선택
scale_idx = 50  # 이 값을 변경하여 다른 스케일의 결과를 볼 수 있습니다
selected_scale_coeffs = coeffs[scale_idx, :]

# 시간 축 생성
time = np.arange(len(selected_scale_coeffs))

# 웨이블릿 계수 플롯
plt.figure(figsize=(10, 6))
plt.plot(time, selected_scale_coeffs)
plt.title(f'Wavelet Transform Coefficients at Scale {scale_idx} wav')
plt.xlabel('Time')
plt.ylabel('Coefficient Value')
plt.grid(True)
plt.show()
