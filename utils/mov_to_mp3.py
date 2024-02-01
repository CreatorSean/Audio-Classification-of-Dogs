from moviepy.editor import *
from glob import glob

mov_file = 'assets/mov/*'

def mov_to_mp3(mov_paths:list):
    for path in mov_paths:
        mov_name = path.split("\\")[1].split(".")[0]
        print(mov_name+" 파일 mp3로 변환중...")
        mov = VideoFileClip(path)
        mp3_path = 'assets/mp3/'+mov_name+".mp3"
        mov.audio.write_audiofile(mp3_path)
        print(mp3_path+" 변환 완료!")

def get_mov_path_list():
    mov_paths = glob(mov_file)
    return mov_paths

def main():
    mov_paths = get_mov_path_list()
    mov_to_mp3(mov_paths=mov_paths)

main()