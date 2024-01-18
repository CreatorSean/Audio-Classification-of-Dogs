import matplotlib.pyplot as plt
import librosa.display
import librosa

# 오디오 파일 로드
path = 'assets/wav/1.wav'  # WAV 파일의 경로를 지정하세요
audio, sample_rate = librosa.load(path, sr=None)  # sr=None으로 설정하면 파일의 원래 샘플링 레이트를 사용합니다

# waveform 시각화
plt.figure(figsize=(12, 4))
librosa.display.waveshow(audio, sr=sample_rate)
plt.title('Waveform')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.show()
