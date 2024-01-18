from pydub import AudioSegment
from glob import glob

# MP3 파일 경로
mp3_file = 'assets/mp3/*'

# WAV로 변환하고 저장
def mp3_to_wav(mp3_paths:list):
    for path in mp3_paths:
        mp3_name = path.split("\\")[1].split(".")[0]
        print(mp3_name+" 파일 wav로 변환중...")
        audio = AudioSegment.from_mp3(path)
        output_audio_path = "assets/wav/"+mp3_name+".wav" # 추출된 오디오 저장 경로
        audio.export(output_audio_path, format='wav')
        print(output_audio_path+" 변환 완료!")


def get_mp3_path_list():
    mp3_paths = glob(mp3_file)
    return mp3_paths


def main():
    mp3_paths = get_mp3_path_list()
    mp3_to_wav(mp3_paths)

main()
