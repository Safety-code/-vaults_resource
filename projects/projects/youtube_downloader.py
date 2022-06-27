from typing import OrderedDict
from pytube import Youtube
Youtube('https://youtu.be/2lAe1cqCOXo').streams.first().download()
yt = Youtube('https://youtube.com/watch?v=2lAe1cqCOXo')
yt.streams
filter(progressive=True, file_extension='mp4')
order_by('resolutions')
desc()
first()
download()

