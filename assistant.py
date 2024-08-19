from handlers.speech_recognition_handler import SpeechRecognitionHandler
from handlers.command_handler import CommandHandler
import random
import simpleaudio as sa


def load_greetings():
    return [sa.WaveObject.from_wave_file('audio_responses/greet1.wav'),
            sa.WaveObject.from_wave_file('audio_responses/greet2.wav'),
            sa.WaveObject.from_wave_file('audio_responses/greet3.wav')]


def respond_to_jarvis(greetings):
    response = random.choice(greetings)
    play_obj = response.play()
    play_obj.wait_done()


def main():
    speech_handler = SpeechRecognitionHandler("models_vosk/uk")
    command_handler = CommandHandler()
    greetings = load_greetings()

    while True:
        speech = speech_handler.recognize_speech()
        if "алекс" in speech:
            respond_to_jarvis(greetings)
        else:
            command_handler.handle_macbook_command(speech)
