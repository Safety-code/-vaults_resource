from pytube import Youtube
#Save the video in the cureent working directory
downl_loc= './'

#Ask the user for video url
video_url = input('')

#Create an instance of youtube video

video_instance = pytube.Youtube(video_url)

stream = video_instance.streams.get_highest_resolution()

#download video
stream.download(downl_loc)
