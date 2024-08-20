import webbrowser
import psutil


def open_browser():
    default_browser = "Google Chrome"
    browsers = ["Google Chrome", "Safari", "Firefox"]

    opened_browser = None

    for process in psutil.process_iter(['name']):
        if process.info['name'] in browsers:
            opened_browser = process.info['name']
            print(f"{process.info['name']} вже відкрито.")
            if process.info['name'] == default_browser:
                return

    print(f"Відкриваю браузер за замовчуванням: {default_browser}")
    webbrowser.open_new_tab("https://www.google.com")
