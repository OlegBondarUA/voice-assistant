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


def open_browser(browser_name):
    if not browser_name:
        browser_name = "Google Chrome"
    for process in psutil.process_iter(['name']):
        if process.info['name'] == browser_name:
            print(f"{browser_name} вже відкрито.")
            activate_browser(browser_name)
            return

    print(f"Відкриваю браузер за замовчуванням: {browser_name}")
    if browser_name.lower() == "google chrome":
        webbrowser.get('google-chrome').open_new_tab("about:blank")
    elif browser_name.lower() == "firefox":
        webbrowser.get('firefox').open_new_tab("about:blank")
    elif browser_name.lower() == "safari":
        webbrowser.get('safari').open_new_tab("about:blank")


def get_browser_tabs(browser_name):
    script = f"""
    tell application "{browser_name}"
        set tabList to {{}}
        repeat with w in windows
            repeat with t in tabs of w
                set end of tabList to (URL of t as string)
            end repeat
        end repeat
        return tabList
    end tell
    """

    result = subprocess.run(["osascript", "-e", script], capture_output=True, text=True)
    tabs = result.stdout.strip().split("\n")
    return tabs


def focus_or_open_youtube(browser_name):
    activate_browser(browser_name)
    tabs = get_browser_tabs(browser_name)

    for tab in tabs:
        if "youtube.com" in tab:
            script = f"""
            tell application "{browser_name}"
                set found to false
                repeat with w in windows
                    set tabIndex to 1
                    repeat with t in tabs of w
                        if URL of t contains "youtube.com" then
                            set found to true
                            set active tab index of w to tabIndex
                            set index of w to 1
                            activate
                            return
                        end if
                        set tabIndex to tabIndex + 1
                    end repeat
                    if found then exit repeat
                end repeat
            end tell
            """
            subprocess.run(["osascript", "-e", script], capture_output=True, text=True)
            return

    script = f'''
    tell application "{browser_name}"
        if (count windows) = 0 then
            make new window
        end if
        tell front window
            make new tab with properties {{URL:"https://www.youtube.com"}}
            set active tab index to (count tabs)
            set index to 1
        end tell
        activate
    end tell
    '''
    subprocess.run(["osascript", "-e", script], capture_output=True, text=True)


def open_youtube():
    default_browser = "Google Chrome"
    open_browser(default_browser)
    focus_or_open_youtube(default_browser)


def search_youtube(query):
    encoded_query = quote(query)
    url = f"https://www.youtube.com/results?search_query={encoded_query}"
    webbrowser.open_new_tab(url)


def play_youtube_video(query):
    search_youtube(query)
