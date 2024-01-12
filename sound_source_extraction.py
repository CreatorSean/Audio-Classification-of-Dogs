from moviepy.editor import VideoFileClip
from glob import glob

video_path = 'assets/mp4/*'  # 저장된 비디오 파일 경로

def extract_audio_from_video(video_paths:list):
    for path in video_paths:
        video_name = path.split("\\")[1].split(".")[0]
        output_audio_path = "assets/mp3/"+video_name+".mp3" # 추출된 오디오 저장 경로
        print(video_name+" 파일 오디오로 변환중...")
        video = VideoFileClip(path)
        audio = video.audio
        audio.write_audiofile(output_audio_path)
        print(output_audio_path+" 변환 완료!")

def get_video_path_list():
    video_paths = glob(video_path)
    return video_paths

def main():
    video_paths = get_video_path_list()
    extract_audio_from_video(video_paths)

main()



