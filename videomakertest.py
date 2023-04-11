import random
import sox
from moviepy.editor import *
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip
import moviepy.video.fx.all as fx
from moviepy.audio.fx.all import *



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
    aspect_ratio = 9 / 16
    new_height = int(vid.w * aspect_ratio)
    y_top = int((vid.h - new_height) / 2)
    y_bottom = y_top + new_height
    crop_rectangle = (0, y_top, vid.w, y_bottom)
    cropped_video = vid.crop(*crop_rectangle)
    title_scr = ImageClip(f"scr/{ID}.png").set_duration(audio_lengths[0])

    # comment1_scr = ImageClip(f"scr/comments/{ID}_{comment_ID}").set_duration(audio_lengths[1])
    # comment2_scr = ImageClip(f"scr/comments/{ID}_{comment_ID}").set_duration(audio_lengths[2])
    # comment3_scr = ImageClip(f"scr/comments/{ID}_{comment_ID}").set_duration(audio_lengths[3])
    aud = AudioFileClip(f"voice/merged_audios/{ID}.wav")
    audios = CompositeAudioClip([aud])
    video_comp = CompositeVideoClip([cropped_video.set_position("center"), title_scr.set_position("center").resize(0.6)]).set_fps(
        30)
    video_comp.audio = audios
    video_comp.write_videofile(f"videos/resize_videos/{ID}.mp4")

    music_file = AudioFileClip("bgm.mp3").subclip(0, total + 2).fx(afx.volumex, 0.07)
    vid = VideoFileClip(f"videos/resize_videos/{ID}.mp4").set_fps(30)
    music = CompositeAudioClip([music_file, vid.audio])
    video_res = CompositeVideoClip([vid.resize(width=720, height=1280)])
    video_res.audio = music
    video_res.write_videofile(f"videos/final_videos/{ID}_final.mp4")
