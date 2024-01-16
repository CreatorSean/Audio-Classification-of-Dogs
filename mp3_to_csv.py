import os
import numpy as np
from pydub import AudioSegment
from scipy.io import wavfile
from scipy.fft import fft
import matplotlib.pyplot as plt

def mp3_to_wav(input_path, output_path):
    audio = AudioSegment.from_mp3(input_path)
    audio.export(output_path, format="wav")

def preprocess_audio(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith(".mp3"):
            input_path = os.path.join(input_folder, filename)

            # mp3 -> wav
            wav_path = os.path.join(output_folder, os.path.splitext(filename)[0] + ".wav")
            mp3_to_wav(input_path, wav_path)

            _, data = wavfile.read(wav_path) 
            fft_result = fft(data)
            
            fft_result = np.abs(fft_result)

            output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + "_fft.csv")
            np.savetxt(output_path, fft_result)
            os.remove(wav_path)

            plt.plot(fft_result)
            plt.title(f"FFT Result - {filename}")
            plt.xlabel("Frequency")
            plt.ylabel("Amplitude")
            plt.show()

            print(f"{filename} 파일을 {output_path} 및 그래프로 변환중...")

if __name__ == "__main__":
    input_folder = "assets/mp3"
    output_folder = "assets/csv"
    preprocess_audio(input_folder, output_folder)
