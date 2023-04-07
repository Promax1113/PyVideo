from moviepy.editor import *
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip
import moviepy.video.fx.all as fx


def concatenate_audio_moviepy(audio_clip_paths, output_path):
    clips = [AudioFileClip(c) for c in audio_clip_paths]
    final_clip = concatenate_audioclips(clips)
    final_clip.write_audiofile(output_path + ".wav")


def make_movie(ID):
    audios = []
    path = "voice/comments/"

    title = f"voice/{ID}.wav"
    audios.append(title)
    for file in os.listdir(path):
        if file.startswith(f"{ID}"):
            audios.append(path + file)

    concatenate_audio_moviepy(audios, f"voice/merged_audios/{ID}")

    scr = ImageClip(f"scr/{ID}.png").set_duration(30)
    aud = AudioFileClip(f"voice/merged_audios/{ID}")
    audios = CompositeAudioClip([aud])
    video_comp = CompositeVideoClip([scr]).set_fps(30)
    video_comp.audio = audios
    video_comp.write_videofile(f"videos/resize_videos/{ID}.mp4")

    vid = VideoFileClip(f"videos/resize_videos/{ID}").set_fps(30)
    video_res = CompositeVideoClip([vid.resize(height=720).crop(x1=0, y1=0, x2=720, y2=1280)])
    video_res.write_videofile(f"videos/final_videos/{ID}_final.mp4")


