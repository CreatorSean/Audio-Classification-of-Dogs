from moviepy.editor import VideoFileClip

path = 'assets/mp4/285_긍정.mp4'

def extract_audio_from_video(video_path):
    video_name = video_path.split("/")[2].split(".")[0]
    print(video_name)
    output_audio_path = "assets/mp3/"+video_name+".mp3"
    print(video_name+" 파일 오디오로 변환중...")
    video = VideoFileClip(video_path)
    audio = video.audio
    audio.write_audiofile(output_audio_path)
    print(output_audio_path+" 변환 완료!")

def main():
    extract_audio_from_video(path)

main()