from TTS.api import TTS
import shutil
import pathlib

# Imagine here we pass an ID from the other file.

ID = 1223124242

model_name = "tts_models/en/ek1/tacotron2"

filename = "Voiceovers/" + str(ID) + ".wav"

tts = TTS(model_name, progress_bar=True)
tts.tts_with_vc_to_file(text="What movie traumatized you as a kid?", file_path="output.wav")
