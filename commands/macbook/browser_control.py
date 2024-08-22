import webbrowser
import psutil
import subprocess
from urllib.parse import quote


def activate_browser(browser_name):
    script = f"""
    tell application "{browser_name}"
        activate
    end tell
    """
    subprocess.run(["osascript", "-e", script])


def open_browser():
    default_browser = "Google Chrome"
    browsers = ["Google Chrome", "Safari", "Firefox"]

    opened_browser = None

    for process in psutil.process_iter(['name']):
        if process.info['name'] in browsers:
            opened_browser = process.info['name']
            print(f"{process.info['name']} вже відкрито.")
            if process.info['name'] == default_browser:
                activate_browser(default_browser)
                return

    print(f"Відкриваю браузер за замовчуванням: {default_browser}")
    webbrowser.open_new_tab("https://www.google.com")


def open_youtube():
    webbrowser.open_new_tab("https://www.youtube.com")


def search_youtube(query):
    encoded_query = quote(query)
    url = f"https://www.youtube.com/results?search_query={encoded_query}"
    webbrowser.open_new_tab(url)


def play_youtube_video(query):
    search_youtube(query)
