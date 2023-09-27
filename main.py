import os
import ffmpeg
# import youtube_dl
from yt_dlp import YoutubeDL

DOWNLOAD_PATH = os.getcwd()

def download_and_convert(url, type, start_time='', end_time=''):
    if type == "mp3":
        # mp3 다운로드 설정
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': '%(id)s.%(ext)s',
        }
    else:
        # mp4 영상 다운로드 설정
        ydl_opts = {
            'format': 'best',
            'postprocessors': [{
                'key': 'FFmpegVideoConvertor',
                'preferedformat': 'mp4',
            }]
        }

    # YouTube 영상 잘라서 다운로드, 음성도 가능
    with YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=False)
        video_url = info_dict.get('url', None)
        title = info_dict.get('title', None)
        title = title.replace("/", "")

    # 시작 및 끝 시간 설정
    if start_time == '':
        end = ffmpeg.input(video_url)
    else:
        start = ffmpeg.input(video_url,ss=start_time)
        end = start.trim(end=end_time)

    # MP3 파일로 변환
    output_file = f"{DOWNLOAD_PATH}\\{title}.{type}"
    end.output(output_file).run()

    print(f'Successfully downloaded and converted to MP3: {output_file}')    

url = 'https://www.youtube.com/watch?v=EIz09kLzN9k'
start_time = '00:00:00'
end_time = '00:02:27'

# mp3 음악 다운로드 시 
download_and_convert(url, "mp3") # type = mp3, mp4

# mp4 영상 다운로드 시
# download_and_convert(url, "mp4", start_time, end_time)
