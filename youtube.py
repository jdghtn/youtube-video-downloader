from pytube import YouTube
import tkinter as tk
from tkinter import filedialog

def download_video(url, file_path):
  try:
    yt = YouTube(url)
    streams = yt.streams.filter(progressive=True, file_extension='mp4')
    highest_res = streams.get_highest_resolution()
    highest_res.download(output_path=file_path)
    print('Video downloaded successfully!')
  except Exception as e:
    print('Video downloaded failed!')
    print(e)

def open_file_explorer():
  folder = filedialog.askdirectory()

  if folder:
    print(f'Selected folder: {folder}')

  return folder

if __name__ == '__main__':
  root = tk.Tk()
  root.withdraw()

  video_url = input('Enter the YouTube url: ')
  download_path = open_file_explorer()

  if download_path:
    print('Starting download...')
    download_video(video_url, download_path)
  else:
    print('Invalid location')