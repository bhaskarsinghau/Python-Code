from pytube import YouTube
 
youtube_video_url = 'https://www.youtube.com/watch?v=CIx0a1vcYPc'
 
try:
    yt_obj = YouTube(youtube_video_url)
 
    filters = yt_obj.streams.filter(progressive=True, file_extension='mp4')
 
    # download the highest quality video
    filters.get_highest_resolution().download()
    print('Video Downloaded Successfully')
except Exception as e:
    print(e)

#There are few useful functions to get the highest and lowest resolution videos.

'''
filters = yt_obj.streams.filter(progressive=True, file_extension='mp4')
 
filters.get_highest_resolution()
filters.get_lowest_resolution()   

'''