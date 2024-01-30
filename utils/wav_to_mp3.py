from pydub import AudioSegment
from glob import glob
wav_file = 'assets/wav/*'

def wav_to_mp3(wav_paths:list):
    for path in wav_file:
        wav_name = path.split("\\")[1].split(".")[0]
        print(wav_name+" 파일 mp3로 변환중...")
        wav_audio = AudioSegment.from_file(path,format="wav")
        output_audio_path="assets/mp3/"+wav_name+".mp3"
        wav_audio.export(output_audio_path,format='mp3')
        print(output_audio_path+" 변환 완료!")


def get_wav_path_list():
    wav_paths = glob(wav_file)
    return wav_paths

def main():
    wav_paths = get_wav_path_list()
    wav_to_mp3(wav_paths)

main()