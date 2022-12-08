# Project-Gideon

## Description
A personal virus I made in python as a little fun project, Have a pretty nice list of features:

`Downloader` Features:
- Updateable Payload
- Easily modifiable sleep time
- Silent and light
- No need for any paid services or complicated stuff

`Payload` Features:
- Steals Chrome History
- Steals some specific tabs you want with *cookies included*
- Steals Chrome Password
- Steals Files with certain `keywords`, `Date modified`, and `Extension`
- Send via email

It used to have a wifi stealer but they are often detected by antiviruses

## Flowchart
![Untitled Diagram drawio](https://user-images.githubusercontent.com/94969176/206345325-00603a96-ff7a-4c02-9fb3-18cb8979fcb6.png)

## Prerequisites [Probably should've made a dependency list]
- Python 3.9 or up
- Pyinstaller
- mimetypes
- smtplib
- email.message 
- win32crypt
- Crypto.Cipher 
- sqlite3
- urllib2
- browserhistory 
- urllib.request
- browser_cookie3
- base64


## How to use 
`Disclaimer: Educational Purposes only, I do not hold any responsibility on what others do using this program. This program is only meant to teach how viruses can be made with innocent pieces of codes. By using this as an inspiration or using the code itself, you are agreeing that I do not hold any responsibilities of what you do.`

### Setting up the Payload
To set up the payload, you will need 2 email addresses, one to send and one to receive. For the sender, you will need an `App password` of the sender email, You can simply get this by turning 2FA

#### Turning on 2FA
- Go to [Gmail](https://mail.google.com/)
- Click your profile picture at top right of the page
- Click `Manage Your Google Account`
- Go to `Security` Tab
- Scroll down to 2FA and follow the steps
- After you finished, Proceed with getting the app password

#### Getting the App Password
- Below 2FA, You'd find `App Password`, if not just go [here](https://myaccount.google.com/apppasswords)
- Just click `Select App` and choose `Other (Custom name)`, You are free to name it anything
![image](https://user-images.githubusercontent.com/94969176/206349063-86e9bed2-55b2-4310-bb16-c764b5896801.png)
- Copy the 16-digits code shown
![image](https://user-images.githubusercontent.com/94969176/206349272-a3c30194-d1e5-4c87-87fe-14d21cc65fbe.png)

#### Putting it up on the payload and setting up the rest
- Open the payload in an IDE or any code editor
- Fill these up with the necessary credentials
![image](https://user-images.githubusercontent.com/94969176/206349684-0abc6646-8dad-46bb-bdfe-eb3d8833a520.png)
- Scroll down to `clairvoyance_mod` function
- Modify `EXTENSION`, `DETECT_KEYWORD`, "Days" (As in how many days back since modified) as you liked, I limited scans on `C:\\` to `DETECT_TUPLE`, you can change this by just changing the contents of the tuple to `("C:\\",)` 
![image](https://user-images.githubusercontent.com/94969176/206349810-97dcd923-9386-4698-ae2f-72c0fe3612e9.png)
- You also can download different types of websites with cookies on it by changing the requirements on this piece of code
![image](https://user-images.githubusercontent.com/94969176/206350298-99828a85-63fb-4609-96bd-342cec42f06a.png)
- Once you are ready, save it

#### Packing it into an EXE
- Open `Command Prompt`
- Get the current directory (Folder) name and add `cd ` before it (If it's on another drive, just write the drive name, I.e. if the file is on D: drive, type `D:` and press enter)
![image](https://user-images.githubusercontent.com/94969176/206350644-a3fb6f0d-af6e-4854-97d0-894aed3deb3f.png)
- type `Pyinstaller -F -w payload.exe`, I usually use a powerpoint icon to make it seem more legit, if you are using that as well, I provided mine in the project files, You can write `Pyinstaller -F -w -i pptxico.ico payload.exe`


### Setting up the downloader
- Open the downloader in an IDE or any code editor (Even Notepad)
