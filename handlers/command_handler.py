from commands.macbook.volume_control import increase_volume, decrease_volume, mute_volume
from commands.macbook.browser_control import *


class CommandHandler:
    def __init__(self):
        self.commands = {
            "зроби звук гучніше": (increase_volume, "Збільшую гучність"),
            "зроби звук тихіше": (decrease_volume, "Зменшую гучність"),
            "вимкни звук": (mute_volume, "Вимикаю звук"),
            "браузер": (open_browser, "відкриваю браузер"),
            "відкрий ютуб": (open_youtube, "Відкриваю YouTube"),
        }

    def handle_macbook_command(self, speech):
        for command, (action, message) in self.commands.items():
            if command in speech:
                action()
                print(message)
                break

        if "пошук у ютубі" in speech:
            query = speech.split("пошук у ютубі")[-1].strip()
            search_youtube(query)
            print(f"Шукаю на YouTube: {query}")

        elif "запуск відео" in speech:
            query = speech.split("запуск відео")[-1].strip()
            play_youtube_video(query)
            print(f"Запускаю відео на YouTube: {query}")
