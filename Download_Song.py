from pytube import YouTube

file = open('song.txt', 'w')
stop = 'si'
link = []

print('Ti verrà chiesto quando se hai finito basta inserire: NO/no/n')

while stop != 'no' and stop != 'n':

    link.append(input('Inserisci i link che vuoi scaricare: '))
    stop = input('Continuare: ')
    stop = stop.lower()

for element in link:
    file.write('\n' + element)

file.close()

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
