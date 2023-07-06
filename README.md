# Youtube to mp3/mp4

Download ffmpeg from https://ffmpeg.org/download.html and place it in the folder with your code.


If you get an error like this "youtube_dl.utils.RegexNotFoundError: Unable to extract uploader id;", please update to the latest code from https://github.com/ytdl-org/youtube-dl or modify line 1793 of youtube_dl/extractor/youtube.py like below and run it.

```
'uploader_id': self._search_regex(r'/(?:channel|user)/([^/?&#]+)', owner_profile_url, name='uploader id', default='uploader id') if owner_profile_url else None,
```
