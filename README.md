# Project-Gideon
<div align="center">

[![Not-Baguette - Project-Gideon](https://img.shields.io/static/v1?label=Not-Baguette&message=Project-Gideon&color=blue&logo=github)](https://github.com/Not-Baguette/Project-Gideon "Go to GitHub repo")
[![GitHub tag](https://img.shields.io/github/tag/Not-Baguette/Project-Gideon?include_prereleases=&sort=semver&color=blue)](https://github.com/Not-Baguette/Project-Gideon/releases/)
[![License](https://img.shields.io/badge/License-MIT-blue)](#license)
[![issues - Project-Gideon](https://img.shields.io/github/issues/Not-Baguette/Project-Gideon)](https://github.com/Not-Baguette/Project-Gideon/issues)
</div>

<div align="center">

[![View site - Project-Gideon](https://img.shields.io/badge/View_site-GH_Pages-2ea44f?style=for-the-badge)](https://github.com/Not-Baguette/Project-Gideon)

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/f0082e38c41644ddb55e77a5e50185fa)](https://app.codacy.com/gh/Not-Baguette/Project-Gideon/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade)
</div>

## Update
Project development has ended, as it's no longer needed or interests me unfortunately.

## Description
A personal virus I made in python as a little fun project, This is continuation of Project Blackrod, a similar project but without a downloader and less features, you wouldn't be able to change the payload too because of that. Project Gideon will be regularly maintained and get features added if I got more nice ideas. I might not be updating it alot on Github though ~as I am too lazy to change it from personal use I made for myself or vice versa.~

## Todo (Totally not me just being lazy)
### Once this is done, I will make the 2.1.0-Beta Update
- [ ] Sufficient Testing with the new `get_chrome_history()` function
- [X] Finished decoupling with `browserhistory` library
- [ ] delete residual files with `os` lib on temp folder
- [ ] Make it so that chrome is unopenable via `ctypes` lib
- [ ] Make a builder for easier installation (Reason: I just never did it so I am not sure how and which approach should I do, should I go with `setup.py`? `build.bat`? [Probably going with `build.bat`])
- [ ] Add `Hidden` attribute to the payload via either win32 lib or subprocessing lib (Reason: I am not sure if it would be easily detectable by an antivirus if I do that)
- [ ] Consideration for sending stuff like chrome password etc via discord webhook
- [ ] Make a switch incase you want to do it at a specific time (Reason to not: Might be slightly memory consuming to check it every few seconds)
=======
Warning: `readme.md` is slightly outdated since I made it quite sometime ago

## Features:
`Downloader` Features:
- Updateable Payload
- Easily modifiable sleep time
- Silent and light
- No need for any paid services or complicated stuff

`Payload` Features:
- Silently sends Chrome History
- Silently sends some specific tabs you want with *cookies included* [Decoupled, See: [Gform Downloader](https://github.com/Not-Baguette/Project-Gideon/blob/1.4.0-stable/gform_download.py)]
- Silently sends Chrome Password
- Silently sends Files with certain `keywords`, `Date modified`, and `Extension`
- Send via email

It used to have a wifi pw stealer but they are often detected by antiviruses

## Flowchart
![Untitled Diagram drawio](https://user-images.githubusercontent.com/94969176/206345325-00603a96-ff7a-4c02-9fb3-18cb8979fcb6.png)

## Prerequisites
- Python
- Pyinstaller
- mimetypes
- smtplib
- email.message 
- urllib2
- urllib.request

(Not updated yet)
Most of these don't require installing, check [`requirements.txt`](https://github.com/Not-Baguette/Project-Gideon/blob/main/requirements.txt) for non-builtins libraries


## How to use 
`Disclaimer: Educational Purposes only, I do not hold any responsibility on what others do using this program. This program is only meant to teach how viruses can be made with innocent pieces of codes. By using this as an inspiration or using the code itself, you are agreeing that I do not hold any responsibilities of what you do.`

### Setting up the Payload
To set up the payload, you will need 2 email addresses, one to send and one to receive. For the sender, you will need an `App password` of the sender email, You can simply get this by turning 2FA

#### Turning on 2FA
- Go to [Gmail](https://mail.google.com/)
- Click your profile picture at top right of the page
- Click `Manage Your Google Account`
- Go to `Security` Tab
- Scroll down to 2FA, click, and follow the steps
- After you finished, Proceed with getting the app password

#### Getting the App Password
- Below 2FA, You'd find `App Password`, if not just go [here](https://myaccount.google.com/apppasswords)
- Just click `Select App` and choose `Other (Custom name)`, You are free to name it anything

![image](https://user-images.githubusercontent.com/94969176/206349063-86e9bed2-55b2-4310-bb16-c764b5896801.png)
- Copy the 16-characters code given

![image](https://user-images.githubusercontent.com/94969176/206349272-a3c30194-d1e5-4c87-87fe-14d21cc65fbe.png)

#### Putting it up on the payload and setting up the rest
- Open the payload in an IDE or any code editor
- Fill these up with the necessary credentials

![image](https://user-images.githubusercontent.com/94969176/206349684-0abc6646-8dad-46bb-bdfe-eb3d8833a520.png)
- Scroll down to `clairvoyance_mod` function
- Modify `EXTENSION`, `DETECT_KEYWORD`, `Days` (As in how many days back since modified) as you liked, I limited scans on `C:\\` to `DETECT_TUPLE`, you can change this by just changing the contents of the tuple to `("C:\\",)` 

![image](https://user-images.githubusercontent.com/94969176/206349810-97dcd923-9386-4698-ae2f-72c0fe3612e9.png)
- You also can download different types of websites with cookies on it by changing the requirements on this piece of code

![image](https://user-images.githubusercontent.com/94969176/206350298-99828a85-63fb-4609-96bd-342cec42f06a.png)
- Once you are ready, save it

### Setting up the downloader
- Open the downloader in an IDE or any code editor (Even Notepad)
- Make sure to already create the payload
- Open [Pastebin](https://pastebin.com/), Make sure to sign in/Sign Up so you have access into it. We are using pastebin because it provides a static link that we could use as a pointer to a link that changes once you change the file, *I am personally using discord as a dynamic link but it is incredibly up to you* (I reccomend Google Drive if it goes undetected by it as suspicious), just make sure the link will directly downloads the file. 
- Back to Pastebin, Just put the dynamic link inside the pastebin and set the `paste expiration` to `never` and `paste exposure` to `unlisted`
- Click `Create new paste`

![image](https://user-images.githubusercontent.com/94969176/206352778-e30ceeaa-3983-41c8-b13f-f12240d1a441.png)
- You should be redirected to your own pastebin, click `raw`

![image](https://user-images.githubusercontent.com/94969176/206353978-f866d418-9edd-40d2-897f-906323e55b3a.png)
- Copy the link, it should start with `https://pastebin.com/raw/` and end with a string of random numbers and letters

![image](https://user-images.githubusercontent.com/94969176/206353154-1755935e-8f8b-463d-82e9-90a7b1f54c56.png)
- Scroll to `download_payload` function and put your pastebin link there

![image](https://user-images.githubusercontent.com/94969176/206353671-c50c2a06-1459-4acd-9830-0b2571631816.png)
- Scroll to the bottom and change the `file_name` argument to something that does not raise suspicion if found

![image](https://user-images.githubusercontent.com/94969176/206353381-c86c5f4c-3be6-48e1-b8e2-9ec76b2da354.png)

#### Packing it into an EXE
- Open `Command Prompt`
- Get the current directory (Folder) name and add `cd ` before it (If it's on another drive, just write the drive name, I.e. if the file is on D: drive, type `D:` and press enter)

![image](https://user-images.githubusercontent.com/94969176/206350644-a3fb6f0d-af6e-4854-97d0-894aed3deb3f.png)
- type `Pyinstaller -F -w downloader.exe`, I usually use a powerpoint icon to make it seem more legit, if you are using that as well, I provided mine in the project files, You can write `Pyinstaller -F -w -i pptxico.ico downloader.exe`
- Wait until it finishes (If you got any errors, *probably* you either casually changed ".png" extension to ".ico" without [converters](https://convertico.com/) or you did not properly install pyinstaller)
- Once finished, a new directory called `build` and `dist` should appear, open `dist` and your personal downloader should be ready

## How to infect other devices
Just place the downloader (the payload is hosted on the internet) on a hard drive/internet and run it on another windows PC, or you can do the good old social engineering and make people download and run it I guess? (Remember this is only for educational purposes)

## How to Change payload
Since this is a general use downloader, you also can change the payload with your own personal payload, Just upload the payload and renew the link on your pastebin and it should work. So yeah you don't need to infect a device twice if you got a new payload. You can also just modify the given payload and follow the steps above again.

## Removal
Relax, I did not input my credentials to the source code so if you accidentally run the payload, just calmly terminate it from `Task Manager`. But If you run the Downloader, It will run every startup and infect you every few hours too. To stop this, terminate it from `Task Manager` and follow these steps;
- Open `registry Editor`

![image](https://user-images.githubusercontent.com/94969176/206354449-23807053-999d-47d0-b5fa-0c133cba08d0.png)
- Change it to `Computer\HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Run`
- You should see something called `Windows Security` as a key, right click and click delete
 
![image](https://user-images.githubusercontent.com/94969176/206354659-4db6379b-a698-4eb6-b63f-dd0f73c6441a.png)
- Since I placed it in somewhat hidden place, We should also remove it from our system despite being unnecessary, just to completely clean it up. Go to `C:\Users\{Your windows profile username}\AppData\Roaming\Microsoft\Windows\Start Menu\programs\`
- Delete anything resembling the payload and the downloader

![image](https://user-images.githubusercontent.com/94969176/206355150-b7da0ddb-6c0f-42a5-9977-f96805be872a.png)
- And that's it! You're completely uninfected
