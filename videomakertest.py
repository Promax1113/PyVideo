from moviepy.editor import *
import moviepy.video.fx.all as fx

title = "voice/12acoep.wav"
comment1 = "voice/comments/12acoep_jervfgo.wav"
comment2 = "voice/comments/12acoep_jes1aog.wav"
comment3 = "voice/comments/12acoep_jes3px8.wav"

audios = [title, comment1, comment2, comment3]


def concatenate_audio_moviepy(audio_clip_paths, output_path):
    clips = [AudioFileClip(c) for c in audio_clip_paths]
    final_clip = concatenate_audioclips(clips)
    final_clip.write_audiofile(output_path + ".wav")


concatenate_audio_moviepy(audios, "voice/merged_audios/12acoep")

scr = ImageClip("scr/12acoep.png").set_duration(30)
aud = AudioFileClip("voice/merged_audios/12acoep.wav")
audios = CompositeAudioClip([aud])
video_comp = CompositeVideoClip([scr]).set_fps(60)
video_comp.audio = audios
video_comp.write_videofile("videos/resize_videos/12acoep.mp4")

vid = VideoFileClip("videos/resize_videos/12acoep.mp4")
final = vid.resize(width=360)
videoc = CompositeVideoClip([final])
videoc.write_videofile("videos/final_videos/12acoep_final.mp4")

