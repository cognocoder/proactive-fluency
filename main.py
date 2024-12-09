
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


# Create the Root Window
root = tk.Tk()
root.title(ROOT["title"])
root.geometry(ROOT["size"])

root.grid_rowconfigure(0, weight=0)
root.grid_rowconfigure(1, weight=0)
root.grid_rowconfigure(4, weight=1)
root.grid_rowconfigure(5, weight=0)

root.grid_columnconfigure(0, weight=0)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_columnconfigure(3, weight=0)


# Text Area
text_area = tk.Text(root, height=4)
text_area.insert("1.0", "我很好，你呢？")
text_area.grid(row=2, column=1, columnspan=2, padx=4, pady=4, sticky=tk.EW)
text_area.config(wrap="word", undo=True, autoseparators=True, maxundo=-1)


# Controls Frame
controls_frame = tk.Frame(root)
controls_frame.grid(row=1, column=1, columnspan=2, sticky=tk.EW)
# controls_frame.grid_columnconfigure(0, weight=0)
# controls_frame.grid_columnconfigure(1, weight=1)
# controls_frame.grid_columnconfigure(2, weight=1)
# controls_frame.grid_columnconfigure(3, weight=1)


# Record Buttons
record_label_frame = tk.LabelFrame(controls_frame, padx=4, pady=4, text="Record")
record_label_frame.grid(row=0, column=1, sticky=tk.EW, padx=4, pady=4)

record_buttons_frame = tk.Frame(record_label_frame)
record_buttons_frame.pack(fill="both", expand="yes")


# Listen Buttons
listen_label_frame = tk.LabelFrame(controls_frame, padx=4, pady=4, text="Generate")
listen_label_frame.grid(row=0, column=2, sticky=tk.EW, padx=4, pady=4)

listen_buttons_frame = tk.Frame(listen_label_frame)
listen_buttons_frame.pack(fill="both", expand="yes")


# Text Buttons
text_label_frame = tk.LabelFrame(controls_frame, padx=4, pady=4, text="Text")
text_label_frame.grid(row=0, column=3, sticky=tk.EW, padx=4, pady=4)

text_buttons_frame = tk.Frame(text_label_frame)
text_buttons_frame.grid(row=0, column=0, sticky=tk.EW)


#
from icons import ICONS

# Font Spinbox Selection
selected_font = tk.StringVar()

font_separator = ttk.Separator(text_label_frame, orient="vertical")
font_separator.grid(row=0, column=1, sticky=tk.NS, padx=4)

font_name_label = tk.Label(text_label_frame, image=ICONS["typography"])
font_name_label.grid(row=0, column=2, sticky=tk.EW)

font_names_list = ["HanyiSentyTang", "Hanyi Senty Lingfei Scroll", "KaiTi", "Noto Sans CJK SC"]
font_name_spinbox = tk.Spinbox(text_label_frame, textvariable=selected_font, values=font_names_list, command=lambda : change_font(font_name_spinbox.get()))
font_name_spinbox.config(cursor="hand2", width=20, state="readonly")
font_name_spinbox.grid(row=0, column=3, sticky=tk.EW, padx=4)

font_size_spinval = tk.StringVar()
font_size_spinval.set(48)
font_size_spinbox = ttk.Spinbox(text_label_frame, from_=8, to=72, textvariable=font_size_spinval, command=lambda : change_font(selected_font.get()), width=4)
font_size_spinbox.config(cursor="hand2")
font_size_spinbox.grid(row=0, column=4, sticky=tk.E)


# Status Bar
status_bar_spacer = tk.Label(root)
status_bar_spacer.grid(row=4, column=0, columnspan=3, sticky=tk.EW)

status_bar_label = tk.Label(root, text="Ready", justify="left", anchor="w", relief="sunken", padx=4, pady=2)
status_bar_label.grid(row=5, column=0, columnspan=3, sticky=tk.EW, padx=2, pady=2)


# Get Frame by Section
def get_frame_by_section(section):
    if section == "record":
        return record_buttons_frame
    elif section == "listen":
        return listen_buttons_frame
    elif section == "text":
        return text_buttons_frame
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
        button = button_cfg["widget"](frame)
        button.config(cursor="hand2")
        button.grid(row=button_cfg["grid"][0], column=button_cfg["grid"][1])
        buttons[section][label] = button


# Output Directory
output_dir = Path("./output")
output_dir.mkdir(exist_ok=True)


# Change Font
def change_font(name):
    status_bar_label.config(text=f"Font set to {name}")
    new_font = font.Font(family=name, size=font_size_spinval.get(), weight="normal")
    text_area.config(font=new_font)


# Enable Buttons
def set_all_buttons_enable(value):
    for section, section_buttons in buttons.items():
        for button in section_buttons.values():
            button.config(state=tk.DISABLED if not value else tk.NORMAL)

def set_button_enable(section, button, value):
    buttons[section][button].config(state=tk.DISABLED if not value else tk.NORMAL)


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
    playsound(str(filepath))
    set_all_buttons_enable(True)
    status_bar_label.config(text="Ready")

def play_audio(filepath):
    print(filepath)
    set_all_buttons_enable(False)
    status_bar_label.config(text="Playing audio...")
    play_audio_thread = threading.Thread(target=_play_audio, args=(filepath,))
    play_audio_thread.start()
    

# Recognize Speech
def _recognize_speech(audio, recognizer):
    try:
        text = recognizer.recognize_google(audio, language="zh-cn")
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
        # filename = output_dir / f"{timestamp}.wav"
        filepath = output_dir / f"recorded.wav"
        with open(filepath, "wb") as f:
            f.write(audio.get_wav_data())    
        status_bar_label.config(text=f"Audio saved to {filepath}")

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
    set_all_buttons_enable(False)

    listen_thread = threading.Thread(target=_listen_audio)
    listen_thread.start()


# Generate Speech
def _generate_speech():
    input_text = text_area.get("1.0", "end-1c") 
    
    if input_text.strip():
        status_bar_label.config(text="Generating speech...")  # Provide feedback during speaking
        
        # Generate speech from the entered text
        tts = gTTS(text=input_text, lang="zh-cn")
        tts.save(output_dir / "generated.mp3")

        status_bar_label.config(text="Generated Speech saved as output.mp3.")  # Provide feedback when audio is finished
        play_audio(output_dir / "generated.mp3")

    else:
        status_bar_label.config(text="Please enter some text to speak.")

def generate_audio():
    set_all_buttons_enable(False)

    generate_speech_thread = threading.Thread(target=_generate_speech)
    generate_speech_thread.start()

# Save Text
def save_text():
    set_all_buttons_enable(False)
    text = text_area.get("1.0", tk.END)
    file_path = output_dir / "text.txt"
    with open(file_path, "w") as file:
        file.write(text)
    status_bar_label.config(text=f"Text saved to {file_path}")
    set_all_buttons_enable(True)


# Save As
def save_as(source, extension, filetypes):
    timestamp = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    text = re.sub(r'[^\w\s]|[\n\r]', ' ', text_area.get("1.0", "end-1c")).strip() 
    default_filename = f"{timestamp} {text}{extension}"

    new_filename = filedialog.asksaveasfilename(defaultextension=extension, initialdir=output_dir, initialfile=default_filename, filetypes=filetypes)
    
    if new_filename:
        try:
            shutil.copy(source, new_filename)
            status_bar_label.config(text=f"File saved as {default_filename}.")
        except Exception as e:
            status_bar_label.config(text=f"Error while saving: {str(e)}")
    else:
        status_bar_label.config(text="Save operation canceled.")


# Connect Buttons
buttons["record"]["record"].config(command=lambda : record_audio())
buttons["record"]["play"].config(command=lambda : play_audio(output_dir / "recorded.wav"))
buttons["record"]["save"].config(command=lambda : save_as(output_dir / "recorded.wav", ".wav", [("Wave files", "*.wav")]))

buttons["listen"]["record"].config(command=lambda : generate_audio())
buttons["listen"]["play"].config(command=lambda : play_audio(output_dir / "generated.mp3"))
buttons["listen"]["save"].config(command=lambda : save_as(output_dir / "generated.mp3", ".mp3", [("MP3 files", "*.mp3")]))

buttons["text"]["save"].config(command=lambda : save_as(output_dir / "text.txt", ".txt", [("Text files", "*.txt")]))


# Initial Font
change_font(selected_font.get())


# Key Bindings
root.bind("<Control-a>", select_all)


# Execute the Application
root.mainloop()
