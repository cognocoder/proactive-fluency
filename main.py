
import tkinter as tk
from tkinter import ttk
from tkinter import font
from tkinter import filedialog

from datetime import datetime

from playsound import playsound

from gtts import gTTS
import speech_recognition as sr

import threading

import re
from pathlib import Path
import shutil

from window import ROOT

from font import change_font, rotate_font_name, rotate_font_size
from lang import rotate_language

# Create the Root Window
root = tk.Tk()
root.title(ROOT["title"])
root.geometry(ROOT["size"])

root.grid_rowconfigure(0, weight=0)
root.grid_rowconfigure(1, weight=0)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(4, weight=1)
root.grid_rowconfigure(5, weight=0)

root.grid_columnconfigure(0, weight=0)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_columnconfigure(3, weight=0)
root.grid_columnconfigure(4, weight=0)

root.config(padx=24, pady=4)
root.config(bg=ROOT["theme"]["bg"])


# Text Area
text_area = tk.Text(root)
text_area.config(wrap="word", undo=True, autoseparators=True, maxundo=-1)
text_area.config(bg=ROOT["theme"]["bg"], fg=ROOT["theme"]["fg"], foreground=ROOT["theme"]["fg"], insertbackground=ROOT["theme"]["fg"], border=0, insertborderwidth=0, highlightthickness=0)
text_area.insert("1.0", "")
text_area.grid(row=2, column=1, columnspan=2, pady=4, sticky=tk.NSEW)

scrollbar = tk.Scrollbar(root, command=text_area.yview)
text_area.config(yscrollcommand=scrollbar.set)
scrollbar.config(cursor="hand2")
scrollbar.config(bg=ROOT["theme"]["bg:hover"], activebackground=ROOT["theme"]["bg:active"], highlightbackground=ROOT["theme"]["bg:hover"], troughcolor=ROOT["theme"]["bg"])
scrollbar.config(border=0, highlightthickness=0, borderwidth=0, elementborderwidth=0)
scrollbar.grid(row=2, column=3, pady=4, sticky=tk.NS)


# Controls Frame
controls_frame = tk.Frame(root)
controls_frame.grid(row=1, column=1, columnspan=3, pady=24, sticky=tk.EW)
controls_frame.grid_columnconfigure(0, weight=1)
controls_frame.grid_columnconfigure(6, weight=1)
controls_frame.config(bg=ROOT["theme"]["bg"])


# Record Buttons
record_buttons_frame = tk.Frame(controls_frame)
record_buttons_frame.grid(row=0, column=1, sticky=tk.EW, padx=24)
record_buttons_frame.config(bg=ROOT["theme"]["bg"])


# Listen Buttons
listen_buttons_frame = tk.Frame(controls_frame)
listen_buttons_frame.grid(row=0, column=2, sticky=tk.EW, padx=24)
listen_buttons_frame.config(bg=ROOT["theme"]["bg"])


# Text Buttons
text_buttons_frame = tk.Frame(controls_frame)
text_buttons_frame.grid(row=0, column=3, sticky=tk.EW, padx=24)
text_buttons_frame.config(bg=ROOT["theme"]["bg"])


# Language Frame
language_frame = tk.Frame(controls_frame)
language_frame.grid(row=0, column=4, sticky=tk.EW, padx=24)
language_frame.config(bg=ROOT["theme"]["bg"])

language_string_var = tk.StringVar()
language_string_var.set(ROOT["language"]["supported"][0])
language_label = tk.Label(language_frame, textvariable=language_string_var, justify="left", anchor="w")
language_label.config(bg=ROOT["theme"]["bg"], fg=ROOT["theme"]["fg"])
language_label.grid(row=0, column=1, sticky=tk.W, padx=4, pady=2)
language_label.config(font=("Liberation Mono", 12))


AppState = {
    "selected": {
        "font": {
            "name": 0,
            "size": 0
        },
        "language": {
            "name": 0
        }
    }
}

# Status Bar
status_bar_label = tk.Label(root, text="Ready", justify="left", anchor="w", padx=4, pady=2)
status_bar_label.grid(row=5, column=0, columnspan=4, sticky=tk.EW, padx=2, pady=2)
status_bar_label.config(bg=ROOT["theme"]["bg"], fg=ROOT["theme"]["fg"])

# Busy Flag
global busy
busy = False


# Get Frame by Section
def get_frame_by_section(section):
    if section == "user":
        return record_buttons_frame
    elif section == "bot":
        return listen_buttons_frame
    elif section == "text":
        return text_buttons_frame
    elif section == "language":
        return language_frame
    else:
        return None


# Setup Buttons
from buttons import BUTTONS

buttons = {}

# Add Buttons to Frames
for section, section_cfg in BUTTONS.items():
    frame = get_frame_by_section(section)
    buttons[section] = {}
    for label, button_cfg in section_cfg.items():
        if "enabled" in button_cfg and not button_cfg["enabled"]:
            continue

        button = button_cfg["widget"](frame)
        button.config(cursor="hand2", border=0, highlightthickness=0)
        button.config(bg=ROOT["theme"]["bg"], activebackground=ROOT["theme"]["bg:hover"], highlightbackground=ROOT["theme"]["bg"])
        button.grid(row=button_cfg["grid"][0], column=button_cfg["grid"][1], padx=8)
        buttons[section][label] = button


# Output Directory
outdir = Path("./out")


# Enable Buttons
def set_all_buttons_enable(value):
    global busy
    busy = not value

# Select All
def select_all(event=None):
    input = root.focus_get()
    if not isinstance(input, (tk.Text)):
        text_area.focus_set()
        input = text_area

    if isinstance(input, tk.Text):
        input.tag_add("sel", "1.0", "end")
        input.mark_set("insert", "end")
        input.see("insert")
    
    return "break"  # Prevent default handling


# Play Audio
def _play_audio(filepath):
    try:
        playsound(str(filepath))
        status_bar_label.config(text="Ready")
    except Exception as e:
        status_bar_label.config(text="Error while playing the audio.")
    finally:
        set_all_buttons_enable(True)
    

def play_audio(filepath):
    if busy:
        return
    
    set_all_buttons_enable(False)
    status_bar_label.config(text="Playing audio...")
    play_audio_thread = threading.Thread(target=_play_audio, args=(filepath,))
    play_audio_thread.start()
    

# Recognize Speech
def _recognize_speech(audio, recognizer):
    try:
        text = recognizer.recognize_google(audio, language=language_string_var.get())
        text_area.insert(tk.END, text)
        status_bar_label.config(text="Speech recognized successfully.")
        set_all_buttons_enable(True)
    except sr.UnknownValueError:
        status_bar_label.config(text="Speech recognition failed.")
    except sr.RequestError:
        status_bar_label.config(text="Could not request the Speech Recognition service.")
    except Exception as e:
        status_bar_label.config(text=f"Error: {str(e)}")
    finally:
        set_all_buttons_enable(True)

def _write_audio(audio, recognizer):
    try:
        # timestamp = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
        # filename = outdir / f"{timestamp}.wav"
        outdir.mkdir(exist_ok=True)
        filepath = outdir / f"rec.wav"
        with open(filepath, "wb") as f:
            f.write(audio.get_wav_data())    
        status_bar_label.config(text=f"Audio saved to file.")

        recognize_audio_thread = threading.Thread(target=_recognize_speech, args=(audio, recognizer))
        recognize_audio_thread.start()
    except Exception as e:
        status_bar_label.config(text=f"Error: {str(e)}")
    finally:
        set_all_buttons_enable(True)

def _listen_audio():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        status_bar_label.config(text="Recording...")
        audio = recognizer.listen(source, phrase_time_limit=None)
    
    write_audio_thread = threading.Thread(target=_write_audio, args=(audio, recognizer))
    write_audio_thread.start()

# Record Audio
def record_audio():
    if busy:
        return
    
    set_all_buttons_enable(False)

    listen_thread = threading.Thread(target=_listen_audio)
    listen_thread.start()


# Generate Speech
def _generate_speech():
    input_text = text_area.get("1.0", "end-1c") 
    
    if input_text.strip():
        outdir.mkdir(exist_ok=True)

        language = language_string_var.get()[:2]
        lang = language if language != "zh" else language_string_var.get()

        tts = gTTS(text=input_text, lang=lang)
        status_bar_label.config(text=f"Generating speech [{lang}]...")
        tts.save(outdir / "gen.mp3")

        status_bar_label.config(text="Speech saved to file.")
        
        set_all_buttons_enable(True)
        play_audio(outdir / "gen.mp3")

    else:
        status_bar_label.config(text="Please enter some text to speak.")

def generate_audio():
    if busy:
        return
    
    set_all_buttons_enable(False)

    generate_speech_thread = threading.Thread(target=_generate_speech)
    generate_speech_thread.start()


# Save As
def save(source, extension, filetypes):
    outdir.mkdir(exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    default_filename = f"{timestamp}{extension}"
    filename = filedialog.asksaveasfilename(defaultextension=extension, initialdir=outdir, initialfile=default_filename, filetypes=filetypes)

    if filename:
        if extension == ".txt":
            text = text_area.get("1.0", tk.END)
            try:
                with open(filename, "w+") as file:
                    file.write(text)
                status_bar_label.config(text=f"Text saved to file.")
            except Exception as e:
                status_bar_label.config(text=f"Error while saving text: {str(e)}")
        else:    
            try:
                shutil.copy(source, filename)
                status_bar_label.config(text=f"File saved to file.")
            except Exception as e:
                status_bar_label.config(text=f"Error while saving: {str(e)}")
    else:
        status_bar_label.config(text="Save operation canceled.")

# Connect Buttons
# buttons["record"]["record"].config(command=lambda : record_audio())
# buttons["record"]["play"].config(command=lambda : play_audio(outdir / "rec.wav"))

# buttons["listen"]["record"].config(command=lambda : generate_audio())
# buttons["listen"]["play"].config(command=lambda : play_audio(outdir / "gen.mp3"))

# buttons["text"]["save"].config(command=lambda : save(outdir / "txt.txt", ".txt", [("Text files", "*.txt")]))

# buttons["user"]["microphone-outline"].config(command=lambda : record_audio())
buttons["user"]["microphone"].config(command=lambda : record_audio())
buttons["user"]["player-play-outline"].config(command=lambda : play_audio(outdir / "rec.wav"))

buttons["bot"]["message-chatbot"].config(command=lambda : generate_audio())
buttons["bot"]["player-play"].config(command=lambda : play_audio(outdir / "gen.mp3"))

buttons["text"]["text-size"].config(command=lambda : rotate_font_size(AppState["selected"]["font"], status_bar_label, text_area))
buttons["text"]["typography"].config(command=lambda : rotate_font_name(AppState["selected"]["font"], status_bar_label, text_area))

buttons["language"]["language"].config(command=lambda : rotate_language(AppState["selected"]["language"], language_string_var, status_bar_label))

# Initial Font
change_font(AppState["selected"]["font"], status_bar_label, text_area)


# Key Bindings
root.bind("<Control-a>", select_all)


# Execute the Application
root.mainloop()
