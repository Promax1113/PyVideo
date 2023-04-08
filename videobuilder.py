# !! This file is deprecated !!


# from moviepy.editor import *
# import moviepy.video.fx.all as fx
#
#
# def movie(img_loc, audio_loc, out_filename):
#     img = ImageClip(f"images/{img_loc}.png").set_duration(10)
#     aud = AudioFileClip(f"audio/{audio_loc}.wav")
#     audio_clip = CompositeAudioClip([aud])
#     video_comp = CompositeVideoClip([img]).set_fps(60)
#     video_comp.audio = audio_clip
#     video_comp.write_videofile(out_filename)
