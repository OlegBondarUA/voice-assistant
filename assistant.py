import random
import speech_recognition as sr
import simpleaudio as sa


def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Скажіть щось...")
        audio = recognizer.listen(source)

    try:
        # Розпізнавання української мови
        text = recognizer.recognize_google(audio, language="uk-UA")
        print(f"Ви сказали: {text}")
        return text.lower()
    except sr.UnknownValueError:
        print("Не вдалося розпізнати мову.")
    except sr.RequestError as e:
        print(f"Помилка сервісу розпізнавання мови; {e}")

    return ""


def respond_to_jarvis():
    greetings = ['audio_responses/greet1.wav',
                 'audio_responses/greet2.wav',
                 'audio_responses/greet3.wav']

    # Вибір випадкового привітання
    response = random.choice(greetings)

    # Відтворення файлу
    wave_obj = sa.WaveObject.from_wave_file(response)
    play_obj = wave_obj.play()
    play_obj.wait_done()


def main():
    while True:
        speech = recognize_speech()
        if "саша" in speech:
            respond_to_jarvis()


if __name__ == "__main__":
    main()
