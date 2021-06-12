from pytube import YouTube

def download_video(url):
  my_video = Youtube(url)
  my_video = my_video.streams.get_highest_resolution()
  my_video.download()
