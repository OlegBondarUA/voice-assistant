import random

import vosk
import simpleaudio as sa
import json
import pyaudio

from commands.macbook.volume_control import *


def recognize_speech_vosk(model):
    recognizer = vosk.KaldiRecognizer(model, 16000)
    audio = pyaudio.PyAudio()
    stream = audio.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
    stream.start_stream()

    print("Скажіть щось...")

    while True:
        data = stream.read(4096, exception_on_overflow=False)
        if recognizer.AcceptWaveform(data):
            result = recognizer.Result()
            text = json.loads(result).get('text', '')
            print(f"Ви сказали: {text}")
            return text.lower()


def load_greetings():
    return [sa.WaveObject.from_wave_file('audio_responses/greet1.wav'),
            sa.WaveObject.from_wave_file('audio_responses/greet2.wav'),
            sa.WaveObject.from_wave_file('audio_responses/greet3.wav')]


def respond_to_jarvis(greetings):
    response = random.choice(greetings)
    play_obj = response.play()
    play_obj.wait_done()


def handle_macbook_command(speech):
    if "зроби звук гучніше" in speech:
        increase_volume()
        print("Збільшую гучність")
    elif "зроби звук тихіше" in speech:
        decrease_volume()
        print("Зменшую гучність")
    elif "вимкни звук" in speech:
        mute_volume()
        print("Вимикаю звук")


def main():
    model = vosk.Model("models_vosk/uk")
    greetings = load_greetings()

    while True:
        speech = recognize_speech_vosk(model)
        if "джарвіс" in speech:
            respond_to_jarvis(greetings)
        else:
            handle_macbook_command(speech)


if __name__ == "__main__":
    main()
