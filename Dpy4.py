from pytube import YouTube
import pyautogui
try :
    nb = pyautogui.prompt(text='ENTER Youtube URL ', title='YT-downloader' , default='https://www.youtube.com/watch?v=YVFjv56wcYE')
    print('download:.')
    yt = YouTube(nb)
    print('download:.....')
    stream = yt.streams.get_by_itag(22)
    print("download:...........")
    stream.download()
    print('download:__successfully__')
except :
    print("Something went wrong try enter the url correctly")
