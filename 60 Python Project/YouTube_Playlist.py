from pytube import Playlist
 
try:
    playlist = Playlist('https://www.youtube.com/watch?v=-hteQKIv-KM&list=PLKKfKV1b9e8rv3AYP31Ha5XoZvS4JEq9c')
 
    playlist.download_all(download_path='')
 
except Exception as e:
    print(e)