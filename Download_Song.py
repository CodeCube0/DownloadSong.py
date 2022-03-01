from pytube import YouTube
import os

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

print('Download in Corso......')
for line in file:
    url = line
    try:
        yt = YouTube(url)
        streams = yt.streams.filter(only_audio=True)
        stream = yt.streams.get_by_itag(140)
        stream.download()
    except:
        pass

print('Download Terminato con Successo!')
file.close()

folderFile = os.listdir()

x = 'mp4'

for elemento in folderFile:
    if x in elemento:
        new = elemento.replace(x, "mp3")

        os.rename(elemento, new)
