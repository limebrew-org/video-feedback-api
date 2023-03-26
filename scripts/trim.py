from moviepy.editor import *
from moviepy.video.VideoClip import *
from moviepy.video.compositing.CompositeVideoClip import *

QUESTION_BG_VIDEO_PATH = "./videos/question_bg.mp4"
QUESTION_BG_VIDEO_OUTPUT_PATH = "./videos/question_bg_trim.mp4"
VIDEO_SOURCE_PATH = "./videos/feedback-google.mp4"
BACKGROUND_LOGO_SOURCE_PATH = "./media/limebrew.png"

# Load the Question BG video
question_bg_clip = VideoFileClip(QUESTION_BG_VIDEO_PATH)

# Trim the video to 5 secs
trimmed_clip = question_bg_clip.subclip(0, 5)

# Save the trimmed clip
trimmed_clip.write_videofile(QUESTION_BG_VIDEO_OUTPUT_PATH)