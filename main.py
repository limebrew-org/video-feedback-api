from moviepy.editor import *
from moviepy.video.VideoClip import *
from moviepy.video.compositing.CompositeVideoClip import *

BG_VIDEO_PATH = "./videos/question_bg_trim.mp4"
LOGO_SOURCE_PATH = "./media/limebrew.png"

QUESTION_1 = "What is it like to work at Google?"
QUESTION_2 = "What are the benifits at Google?"

ANSWER_CLIP_1 = "./videos/life-at-google.mp4"
ANSWER_CLIP_2 = "./videos/benifits-at-google.mp4"

OUTPUT_VIDEO_PATH = "./output/result.mp4"

def loadVideoClip(filename):
    video_clip = VideoFileClip(filename)
    return video_clip

def loadQuestionClip(question):
    question_clip = TextClip(question, fontsize=50, color='white', font='Arial').set_position('center').set_duration(3)
    return question_clip

def loadLogoClip(filename,duration):
    logo_clip = ImageClip(filename).resize(height=100)
    logo_clip = logo_clip.set_duration(duration)
    logo_clip = logo_clip.set_position(("right", "top"))
    return logo_clip

def writeFile(clip,filename):
    clip.write_videofile(filename,fps=clip.fps)

def createCompositeVideoClip(clip_list):
    composite_clip = CompositeVideoClip(clip_list)
    return composite_clip

def concatenateVideoClips(clip_list):
    concat_clip = concatenate_videoclips(clip_list)
    return concat_clip


#TODO: #############   Question - 1   #############
#TODO: ############################################
#? Load Background clip
bg_clip_1 = loadVideoClip(BG_VIDEO_PATH)

#? Load Question Clip
question_clip_1 = loadQuestionClip(QUESTION_1)

#? Load Logo Clip
question_clip_logo_1 = loadLogoClip(filename=LOGO_SOURCE_PATH,duration=bg_clip_1.duration)


#? Create Composite Video Clip
composite_question_clip_1 = createCompositeVideoClip([bg_clip_1, question_clip_1, question_clip_logo_1])



#TODO: #############   Answer - 1   #############
#TODO: ##########################################
#? Load the Answer Clip
answer_clip_1 = loadVideoClip(ANSWER_CLIP_1)

#? Load Logo Clip
answer_clip_logo_1 = loadLogoClip(filename=LOGO_SOURCE_PATH,duration=answer_clip_1.duration)

#? Create Composite Video Clip
composite_answer_clip_1 = createCompositeVideoClip([answer_clip_1,answer_clip_logo_1])



#TODO: #############   Question - 2   #############
#TODO: ############################################
#? Load Background clip
bg_clip_2 = loadVideoClip(BG_VIDEO_PATH)

#? Load Question Clip
question_clip_2 = loadQuestionClip(QUESTION_2)

#? Load Logo Clip
question_clip_logo_2 = loadLogoClip(filename=LOGO_SOURCE_PATH,duration=bg_clip_2.duration)


#? Create Composite Video Clip
composite_question_clip_2 = createCompositeVideoClip([bg_clip_2, question_clip_2, question_clip_logo_2])


#TODO: #############   Answer - 2   #############
#TODO: ##########################################
#? Load the Answer Clip
answer_clip_2 = loadVideoClip(ANSWER_CLIP_2)

#? Load Logo Clip
answer_clip_logo_2 = loadLogoClip(filename=LOGO_SOURCE_PATH,duration=answer_clip_2.duration)

#? Create Composite Video Clip
composite_answer_clip_2 = createCompositeVideoClip([answer_clip_2,answer_clip_logo_2])



#TODO: #############   Final Clip   #############
#TODO: ##########################################

#? Concatenate the composite_question_clips and composite_answer_clips
final_clip = concatenateVideoClips([
    composite_question_clip_1, 
    composite_answer_clip_1,
    composite_question_clip_2,
    composite_answer_clip_2
    ])


#? Write the final clip to a file
writeFile(final_clip,OUTPUT_VIDEO_PATH)