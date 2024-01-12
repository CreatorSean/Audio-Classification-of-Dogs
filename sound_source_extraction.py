from moviepy.editor import VideoFileClip

def extract_audio_from_video(video_path, output_audio_path):
    video = VideoFileClip(video_path)
    audio = video.audio
    audio.write_audiofile(output_audio_path)

video_path = 'assets/mp4/*'  # 비디오 파일 경로
output_audio_path = 'extracted_audio.mp3'  # 추출된 오디오 저장 경로

def main():
    extract_audio_from_video(video_path, output_audio_path)

main()



