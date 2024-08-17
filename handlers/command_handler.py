from commands.macbook.volume_control import increase_volume, decrease_volume, mute_volume


class CommandHandler:
    def handle_macbook_command(self, speech):
        if "зроби звук гучніше" in speech:
            increase_volume()
            print("Збільшую гучність")
        elif "зроби звук тихіше" in speech:
            decrease_volume()
            print("Зменшую гучність")
        elif "вимкни звук" in speech:
            mute_volume()
            print("Вимикаю звук")
