
import tkinter as tk

from pathlib import Path
import threading

from playsound import playsound

import speech_recognition as sr
from gtts import gTTS

from .busy import setbusy
from .state import State, readto_str
from .window import Window

def _play_audio(window: Window, state: State, path: Path):
    try:
        playsound(str(path))
        window.statuslabel.config(text="Ready")
    except Exception as e:
        window.statuslabel.config(text="Error while playing the audio.")
    finally:
        setbusy(state, False, window.buttons, window.statuslabel)
    

def play_audio(window: Window, state: State, path: Path):
    if state.busy:
        return
    
    setbusy(state, True, window.buttons, window.statuslabel)
    window.statuslabel.config(text="Playing audio...")
    play_audio_thread = threading.Thread(target=_play_audio, args=(window, state, path))
    play_audio_thread.start()


def _recognize_speech(window: Window, state: State, audio, recognizer):
    try:
        text = recognizer.recognize_google(audio, language=window.langstrvar.get())
        window.textarea.insert(tk.END, text)
        
        window.statuslabel.config(text="Speech recognized successfully.")
        setbusy(state, False, window.buttons, window.statuslabel)

    except sr.UnknownValueError:
        window.statuslabel.config(text="Speech recognition failed.")
    except sr.RequestError:
        window.statuslabel.config(text="Could not request the Speech Recognition service.")
    except Exception as e:
        window.statuslabel.config(text=f"Error: {str(e)}")

    finally:
        setbusy(state, False, window.buttons, window.statuslabel)

def _write_audio(window: Window, state: State, recognize: bool, audio, recognizer):
    try:
        state.dir.mkdir(exist_ok=True, parents=True)
        filepath = state.dir / f"{state.file.current}.wav"

        with open(filepath, "wb") as f:
            f.write(audio.get_wav_data())    

        window.statuslabel.config(text=f"Audio saved to '{str(filepath)}'.")

        if recognize:
            recognize_audio_thread = threading.Thread(target=_recognize_speech, args=(window, state, audio, recognizer))
            recognize_audio_thread.start()

    except Exception as e:
        window.statuslabel.config(text=f"Error: {str(e)}")

    finally:
        setbusy(state, False, window.buttons, window.statuslabel)

def _listen_audio(window: Window, state: State, recognize: bool):
    recognizer = sr.Recognizer()
    recognizer.pause_threshold = 1
    recognizer.dynamic_energy_threshold = False
    
    with sr.Microphone() as source:
        window.statuslabel.config(text="Recording...")
        audio = recognizer.listen(source, phrase_time_limit=None)
    
    write_audio_thread = threading.Thread(target=_write_audio, args=(window, state, recognize, audio, recognizer))
    write_audio_thread.start()

def record_audio(window: Window, state: State, recognize: bool):
    if state.busy:
        return
    
    setbusy(state, True, window.buttons, window.statuslabel)

    listen_thread = threading.Thread(target=_listen_audio, args=(window, state, recognize))
    listen_thread.start()


def _generate_speech(window: Window, state: State):
    input_text = window.textarea.get("1.0", "end-1c")

    if state.file.current > 0:
        previous_text = readto_str(state.dir / f"{state.file.current - 1}.txt", window.statuslabel)
        input_text = input_text[len(previous_text):]
    
    if input_text.strip():
        state.dir.mkdir(exist_ok=True, parents=True)

        language = window.langstrvar.get()[:2]
        lang = language if language != "zh" else window.langstrvar.get()

        tts = gTTS(text=input_text, lang=lang)
        window.statuslabel.config(text=f"Generating speech...")

        filepath = state.dir / f"{state.file.current}.mp3"
        tts.save(filepath)

        window.statuslabel.config(text="Speech saved to file.")
        
        setbusy(state, False, window.buttons, window.statuslabel)
        play_audio(window, state, filepath)

    else:
        window.statuslabel.config(text="Please enter some text to speak.")

def generate_audio(window: Window, state: State):
    if state.busy:
        return
    
    setbusy(state, True, window.buttons, window.statuslabel)

    generate_speech_thread = threading.Thread(target=_generate_speech, args=(window, state))
    generate_speech_thread.start()