import librosa

# 파일 로드
path = 'assets/wav/1.wav'  # 오디오 파일 경로를 지정하세요
audio, sample_rate = librosa.load(path, sr=None)  # sr=None으로 설정하면 기본 샘플링 레이트를 사용합니다

print(f"Sample rate: {sample_rate}")
