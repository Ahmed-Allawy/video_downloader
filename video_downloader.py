from pytube import Playlist
from pytube import YouTube
def on_progress(stream, chunk, bytes_remaining):
    """Callback function"""
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    pct_completed = bytes_downloaded / total_size * 100
    print(f"\b\b\b\b\b\b||{round(pct_completed, 2)}%",end='')
##################################################################################################
def Video_download(path,list):
    count = 1
    size = len(list)
    for video in list: 
        print(f'Downloading video number: {count} => remainning {size-count} videos')
        yt = YouTube(
        video,
            on_progress_callback=on_progress,
            #on_complete_callback=complete_func,
            #proxies=my_proxies,
            # use_oauth=False,
            # allow_oauth_cache=True,
            
        )
        yt.streams.filter(res="360p").first().download(output_path= path)
        count += 1
    print("\nDownload completed !")
###########################################################################################################
def playlist_download(path,list):
    number = 1
    for pl in list:
        new_path=str(path)+"\\playlist "+str(number)
        p = Playlist(pl)
        print(f'Downloading: {p.title}')
        Video_download(path=new_path, list=p.video_urls)
        #count = 1
        # for video in p.videos: 
        #     print(f'Downloading video number: {count} => remainning {p.length-count} videos')
        #     yt = YouTube(
        #     video.embed_url,
        #         on_progress_callback=on_progress,
        #         #on_complete_callback=complete_func,
        #         #proxies=my_proxies,
        #         use_oauth=False,
        #         allow_oauth_cache=True
        #     )
        #     yt.streams.filter(res="360p").first().download(output_path=str(path)+"\\playlist "+str(number))
        #     count += 1
        print("playlist " +str(number)+" completed !")
        number+=1
    print("\nDownload completed !")
###########################################################################################################

state = input("Select number => 1-video :: 2-playlist :")
path = input("Enter path of download :")
list = [item for item in input("Enter the URLs with space separated : ").split()]

if(state == '1'): 
   Video_download(path=path, list=list)

elif (state == '2'): 
    playlist_download(path=path, list=list)
else :
    print("Wong number :(")