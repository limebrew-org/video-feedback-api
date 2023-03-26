from moviepy.editor import *
from moviepy.video.VideoClip import *
from moviepy.video.compositing.CompositeVideoClip import *

QUESTION_BG_VIDEO_PATH = "./videos/question_bg_trim.mp4"
VIDEO_SOURCE_PATH = "./videos/feedback-google.mp4"
BACKGROUND_LOGO_SOURCE_PATH = "./media/limebrew.png"


# Load the Question BG video
question_bg_clip = VideoFileClip(QUESTION_BG_VIDEO_PATH)

# Set the question you want to ask
question_text = "What is it like to work at Google?"

# Create a TextClip with the question and set the font, color, and size
question_text_clip = TextClip(question_text, fontsize=50, color='white', font='Arial').set_position('center').set_duration(3)

#? Create the logo Clip
logo_clip = ImageClip(BACKGROUND_LOGO_SOURCE_PATH).resize(height=100)

#? Set logo Duration
logo_clip = logo_clip.set_duration(question_bg_clip.duration)

#? set logo position
logo_clip = logo_clip.set_position(("right", "top"))

# Combine the question clip and background clip
question_clip = CompositeVideoClip([question_bg_clip, question_text_clip, logo_clip])

# Load the video clip you want to add the question to
answer_clip = VideoFileClip(VIDEO_SOURCE_PATH)

# Concatenate the question clip and background clip with the video clip
final_clip = concatenate_videoclips([question_clip, answer_clip])

# # Write the final clip to a file
final_clip.write_videofile("output_video.mp4", fps=final_clip.fps)