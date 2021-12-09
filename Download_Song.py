from pytube import YouTube
yt = YouTube('https://www.youtube.com/embed/pcHUgBYA8jo')
streams = yt.streams.filter(only_audio=True)
streams
stream = yt.streams.get_by_itag(140)
stream.download()