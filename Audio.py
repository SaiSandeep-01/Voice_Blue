import openai
import pyaudio
import wave
from keys import API_KEY
            
# OpenAI authentication
openai.api_key = API_KEY

# Audio settings
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
CHUNK_SIZE = 1024
RECORD_SECONDS = 6
WAVE_OUTPUT_FILENAME = "audio.wav"

def Audio():
    # Set up audio input
    audio = pyaudio.PyAudio()
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK_SIZE)

    # Capture audio
    frames = []
    print("Listening...")
    for i in range(0, int(RATE / CHUNK_SIZE * RECORD_SECONDS)):
        data = stream.read(CHUNK_SIZE)
        frames.append(data)

    print("Recording complete.")

    # Save audio to file
    wave_file = wave.open(WAVE_OUTPUT_FILENAME, "wb")
    wave_file.setnchannels(CHANNELS)
    wave_file.setsampwidth(audio.get_sample_size(FORMAT))
    wave_file.setframerate(RATE)
    wave_file.writeframes(b"".join(frames))
    wave_file.close()

    # Audio to Text using Whisper Engine (Open AI)
    audio_file= open(WAVE_OUTPUT_FILENAME, "rb")
    print("Transcripting")
    transcript = openai.Audio.transcribe("whisper-1", audio_file)

    return transcript['text']