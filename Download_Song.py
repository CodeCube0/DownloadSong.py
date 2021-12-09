from pytube import YouTube
file = open('song.txt', 'r')
for line in file:
   url = line
   try:
       yt = YouTube(url)
       streams = yt.streams.filter(only_audio=True)
       stream = yt.streams.get_by_itag(140)
       stream.download()
   except:
       pass
file.close()