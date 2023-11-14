import os
import subprocess

def convert_to_wav(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".mp3"):
            mp3_file = os.path.join(directory, filename)
            wav_file = os.path.join(directory, os.path.splitext(filename)[0] + ".wav")

            # Команда для конвертации
            subprocess.run(["ffmpeg", "-i", mp3_file, wav_file])

            print(f"Converted {mp3_file} to {wav_file}")
            
if __name__ == "__main__":
    directory = r"C:\Users\79819\Documents\GitHub\convert\sampl"  # Замените на путь к вашей директории
    convert_to_wav(directory)