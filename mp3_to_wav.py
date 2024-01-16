from pydub import AudioSegment
from glob import glob

# MP3 파일 경로
mp3_file = 'assets/mp3/*'

# WAV 파일 경로
wav_file = 'assets/wav'

# MP3 파일 로드
audio = AudioSegment.from_mp3(mp3_file)

# WAV로 변환하고 저장
audio.export(wav_file, format='wav')

def get_video_path_list():
    video_paths = glob(mp3_file)
    return video_paths
