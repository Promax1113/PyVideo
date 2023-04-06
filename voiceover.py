import pyttsx3
import shutil
import pathlib

# Imagine here we pass an ID from the other file.

ID = 1223124242

filename = str(ID) + ".mp3"
engine = pyttsx3.init()

def change_voice(engine, language, gender='VoiceGenderFemale'):
    for voice in engine.getProperty('voices'):
        if language in voice.languages and gender == voice.gender:
            engine.setProperty('voice', voice.id)
            return True

    raise RuntimeError("Language '{}' for gender '{}' not found".format(language, gender))


def generate_voiceover(textt, save_loc):

    engine.say(textt)
    engine.save_to_file(save_loc, filename)
    engine.runAndWait()


change_voice(engine, "en_US", "VoiceGenderFemale")

generate_voiceover("Which comedy movie has the greatest laughs-per-second ratio ever?", "voiceovers")
