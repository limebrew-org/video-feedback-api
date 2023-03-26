from moviepy.editor import *

VIDEO_SOURCE_PATH = "./videos/feedback-google.mp4"
BACKGROUND_LOGO_SOURCE_PATH = "./media/limebrew.png"

# Load the video file
video = VideoFileClip(VIDEO_SOURCE_PATH)

# Load the logo image
logo = ImageClip(BACKGROUND_LOGO_SOURCE_PATH).resize(height=100) 

logo = logo.set_duration(video.duration)

# Set the position of the logo image to top right
logo = logo.set_position(("right", "top"))

# Overlay the background image onto the video
result = CompositeVideoClip([video, logo])

# Write the result to a new video file
result.write_videofile("output_video.mp4", fps=video.fps)