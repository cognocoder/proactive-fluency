
from PIL import Image, ImageTk

from window import ROOT

icon_size = ROOT["icon"]["size"]

ICONS = {
    "play": ImageTk.PhotoImage(Image.open("img/icons/player-play.png").resize((icon_size, icon_size))),
    "record": ImageTk.PhotoImage(Image.open("img/icons/microphone.png").resize((icon_size, icon_size))),
    "save": ImageTk.PhotoImage(Image.open("img/icons/device-floppy.png").resize((icon_size, icon_size))),
    "stop": ImageTk.PhotoImage(Image.open("img/icons/player-stop.png").resize((icon_size, icon_size))),
    "generate": ImageTk.PhotoImage(Image.open("img/icons/message-chatbot.png").resize((icon_size, icon_size))),
}
