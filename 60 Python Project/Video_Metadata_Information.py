from pytube import YouTube
 
try:
    yt_obj = YouTube('https://www.youtube.com/watch?v=R7aCOI4DuA0')
 
    print(f'Video Title is {yt_obj.title}')
    print(f'Video Length is {yt_obj.length} seconds')
    print(f'Video Description is {yt_obj.description}')
    print(f'Video Rating is {yt_obj.rating}')
    print(f'Video Views Count is {yt_obj.views}')
    print(f'Video Author is {yt_obj.author}')
 
except Exception as e:
    print(e)