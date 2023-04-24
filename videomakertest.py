import random
from moviepy.video.fx.all import crop
import moviepy.video.fx.resize
import sox
from moviepy.editor import *
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip
import moviepy.video.fx.all as fx
from moviepy.audio.fx.all import *
from moviepy.audio.fx.volumex import volumex



def concatenate_audio_moviepy(audio_clip_paths, output_path):
    clips = [AudioFileClip(c) for c in audio_clip_paths]
    final_clip = concatenate_audioclips(clips)
    final_clip.write_audiofile(output_path + ".wav")


def make_movie(ID, comment_ID):
    total = 0
    audios = []
    audio_lengths = []
    scrs = []
    path = "voice/comments/"
    c_path = "scr/comments"

    title = f"voice/{ID}.wav"
    audio_lengths.append(sox.file_info.duration(title))
    audios.append(title)
    for file in os.listdir(path):
        if file.startswith(f"{ID}"):
            audio_lengths.append(sox.file_info.duration(path + file))
            audios.append(path + file)
    for file1 in os.listdir(path):
        if file1.startswith(f"{ID}_"):
            scrs.append(path + file1)
    for dur in audio_lengths:
        total += int(dur)
    # print(audio_lengths + "      " + total)
    vid_part = random.randint(11, 540)
    concatenate_audio_moviepy(audios, f"voice/merged_audios/{ID}")
    vid = VideoFileClip("bg.mp4").subclip(vid_part, vid_part + total + 2)
    title_scr = ImageClip(f"scr/{ID}.png").set_duration(audio_lengths[0])

    # comment1_scr = ImageClip(f"scr/comments/{ID}_{comment_ID}").set_duration(audio_lengths[1])
    # comment2_scr = ImageClip(f"scr/comments/{ID}_{comment_ID}").set_duration(audio_lengths[2])
    # comment3_scr = ImageClip(f"scr/comments/{ID}_{comment_ID}").set_duration(audio_lengths[3])
    aud = AudioFileClip(f"voice/merged_audios/{ID}.wav")
    audios = CompositeAudioClip([aud])
    video_comp = CompositeVideoClip([vid.set_position("center"), title_scr.set_position("center").resize(0.8)]).set_fps(
        30)
    video_comp.audio = audios
    video_comp.write_videofile(f"videos/resize_videos/{ID}.mp4")

    music_file = AudioFileClip("bgm.mp3").subclip(0, total + 2).fx(volumex, 0.07)
    vid = VideoFileClip(f"videos/resize_videos/{ID}.mp4").set_fps(30)
    music = CompositeAudioClip([music_file, vid.audio])
    video_res = moviepy.video.fx.resize.resize(vid, height=720, width=405)
    video_res.audio = music
    video_res.write_videofile(f"videos/final_videos/{ID}.mp4")

    clip = VideoFileClip(f"videos/final_videos/{ID}.mp4")
    (w, h) = clip.size

    crop_width = h * 9 / 16
    # x1,y1 is the top left corner, and x2, y2 is the lower right corner of the cropped area.

    x1, x2 = (w - crop_width) // 2, (w + crop_width) // 2
    y1, y2 = 0, h
    cropped_clip = crop(clip, x1=x1, y1=y1, x2=x2, y2=y2)
    cropped_clip.write_videofile(f"videos/{ID}.mp4")
