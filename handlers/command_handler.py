from commands.macbook.volume_control import increase_volume, decrease_volume, mute_volume
from commands.macbook.browser_control import open_browser


class CommandHandler:
    def __init__(self):
        self.commands = {
            "зроби звук гучніше": (increase_volume, "Збільшую гучність"),
            "зроби звук тихіше": (decrease_volume, "Зменшую гучність"),
            "вимкни звук": (mute_volume, "Вимикаю звук"),
            "браузер": (open_browser, "відкриваю браузер"),
        }

    def handle_macbook_command(self, speech):
        for command, (action, message) in self.commands.items():
            if command in speech:
                action()
                print(message)
