import webbrowser
import psutil


def open_browser():
    browsers = ["Google Chrome", "Safari", "Firefox"]

    for process in psutil.process_iter(['name']):
        if process.info['name'] in browsers:
            print(f"{process.info['name']} вже відкрито.")
            return

    print("Відкриваю браузер...")
    webbrowser.open_new_tab("https://www.google.com")
