
from PIL import Image, ImageTk

from window import ROOT

icon_size = ROOT["icon"]["size"]

ICONS = {
    "headphone": ImageTk.PhotoImage(Image.open("img/icons/headphones.png").resize((icon_size, icon_size))),
    "headphone-outline": ImageTk.PhotoImage(Image.open("img/icons/headphones-outline.png").resize((icon_size, icon_size))),
    "language": ImageTk.PhotoImage(Image.open("img/icons/language.png").resize((icon_size, icon_size))),
    "message-chatbot": ImageTk.PhotoImage(Image.open("img/icons/message-chatbot.png").resize((icon_size, icon_size))),
    "microphone": ImageTk.PhotoImage(Image.open("img/icons/microphone.png").resize((icon_size, icon_size))),
    "microphone-outline": ImageTk.PhotoImage(Image.open("img/icons/microphone-outline.png").resize((icon_size, icon_size))),
    "player-play": ImageTk.PhotoImage(Image.open("img/icons/player-play.png").resize((icon_size, icon_size))),
    "player-play-outline": ImageTk.PhotoImage(Image.open("img/icons/player-play-outline.png").resize((icon_size, icon_size))),
    "save": ImageTk.PhotoImage(Image.open("img/icons/square-rounded-plus.png").resize((icon_size, icon_size))),
    "stop": ImageTk.PhotoImage(Image.open("img/icons/player-stop.png").resize((icon_size, icon_size))),
    "text-size": ImageTk.PhotoImage(Image.open("img/icons/text-size.png").resize((icon_size, icon_size))),
    "typography": ImageTk.PhotoImage(Image.open("img/icons/typography.png").resize((icon_size, icon_size))),
}
