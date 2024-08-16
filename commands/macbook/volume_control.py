import os


def increase_volume():
    os.system("osascript -e 'set volume output volume (output volume of (get volume settings) + 10)'")


def decrease_volume():
    os.system("osascript -e 'set volume output volume (output volume of (get volume settings) - 10)'")


def mute_volume():
    os.system("osascript -e 'set volume with output muted'")
