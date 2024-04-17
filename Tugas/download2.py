from pytube import Playlist
     
p = Playlist('https://www.youtube.com/playlist?list=PLZS-MHyEIRo59lUBwU-XHH7Ymmb04ffOY')

print(f'Downloading: {p.title}')

for video in p.videos:
     video.streams.first().download()