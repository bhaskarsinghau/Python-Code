from pytube import YouTube
 
list_urls = ['https://www.youtube.com/watch?v=DkU9WFj8sYo',
             'https://www.youtube.com/watch?v=D5NK5qMM14g']
 
for url in list_urls:
 
    try:
        yt_obj = YouTube(url)
 
        yt_obj.streams.get_highest_resolution().download()
    except Exception as e:
        print(e)
        raise Exception('Some exception occurred.')
    print('All YouTube videos downloaded successfully.')