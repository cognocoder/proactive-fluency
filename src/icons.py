
from PIL import Image, ImageTk

from .config import CONFIG

icon_size = CONFIG.icon.size

ICONS = {
    "folder": ImageTk.PhotoImage(Image.open("img/icons/folder.png").resize((icon_size, icon_size))),
    "folder-disabled": ImageTk.PhotoImage(Image.open("img/icons/folder-disabled.png").resize((icon_size, icon_size))),
    
    "help-square-rounded": ImageTk.PhotoImage(Image.open("img/icons/help-square-rounded.png").resize((icon_size, icon_size))),

    "hourglass": ImageTk.PhotoImage(Image.open("img/icons/hourglass.png").resize((icon_size, icon_size))),
    "hourglass-busy": ImageTk.PhotoImage(Image.open("img/icons/hourglass-busy.png").resize((icon_size, icon_size))),

    "language": ImageTk.PhotoImage(Image.open("img/icons/language.png").resize((icon_size, icon_size))),
    
    "message-chatbot": ImageTk.PhotoImage(Image.open("img/icons/message-chatbot.png").resize((icon_size, icon_size))),
    "message-chatbot-disabled": ImageTk.PhotoImage(Image.open("img/icons/message-chatbot-disabled.png").resize((icon_size, icon_size))),
    
    "microphone": ImageTk.PhotoImage(Image.open("img/icons/microphone.png").resize((icon_size, icon_size))),
    "microphone-disabled": ImageTk.PhotoImage(Image.open("img/icons/microphone-disabled.png").resize((icon_size, icon_size))),

    "microphone-outline": ImageTk.PhotoImage(Image.open("img/icons/microphone-outline.png").resize((icon_size, icon_size))),
    "microphone-outline-disabled": ImageTk.PhotoImage(Image.open("img/icons/microphone-outline-disabled.png").resize((icon_size, icon_size))),
    
    "player-play": ImageTk.PhotoImage(Image.open("img/icons/player-play.png").resize((icon_size, icon_size))),
    "player-play-disabled": ImageTk.PhotoImage(Image.open("img/icons/player-play-disabled.png").resize((icon_size, icon_size))),

    "player-play-outline": ImageTk.PhotoImage(Image.open("img/icons/player-play-outline.png").resize((icon_size, icon_size))),
    "player-play-outline-disabled": ImageTk.PhotoImage(Image.open("img/icons/player-play-outline-disabled.png").resize((icon_size, icon_size))),
    
    "square-rounded-check": ImageTk.PhotoImage(Image.open("img/icons/square-rounded-check.png").resize((icon_size, icon_size))),
    "square-rounded-check-disabled": ImageTk.PhotoImage(Image.open("img/icons/square-rounded-check-disabled.png").resize((icon_size, icon_size))),

    "square-rounded-chevron-left": ImageTk.PhotoImage(Image.open("img/icons/square-rounded-chevron-left.png").resize((icon_size, icon_size))),
    "square-rounded-chevron-left-disabled": ImageTk.PhotoImage(Image.open("img/icons/square-rounded-chevron-left-disabled.png").resize((icon_size, icon_size))),

    "square-rounded-chevron-right": ImageTk.PhotoImage(Image.open("img/icons/square-rounded-chevron-right.png").resize((icon_size, icon_size))),
    "square-rounded-chevron-right-disabled": ImageTk.PhotoImage(Image.open("img/icons/square-rounded-chevron-right-disabled.png").resize((icon_size, icon_size))),

    "square-rounded-chevrons-left": ImageTk.PhotoImage(Image.open("img/icons/square-rounded-chevrons-left.png").resize((icon_size, icon_size))),
    "square-rounded-chevrons-left-disabled": ImageTk.PhotoImage(Image.open("img/icons/square-rounded-chevrons-left-disabled.png").resize((icon_size, icon_size))),

    "square-rounded-chevrons-right": ImageTk.PhotoImage(Image.open("img/icons/square-rounded-chevrons-right.png").resize((icon_size, icon_size))),
    "square-rounded-chevrons-right-disabled": ImageTk.PhotoImage(Image.open("img/icons/square-rounded-chevrons-right-disabled.png").resize((icon_size, icon_size))),

    "square-rounded-x": ImageTk.PhotoImage(Image.open("img/icons/square-rounded-x.png").resize((icon_size, icon_size))),
    "square-rounded-x-disabled": ImageTk.PhotoImage(Image.open("img/icons/square-rounded-x-disabled.png").resize((icon_size, icon_size))),

    "text-size": ImageTk.PhotoImage(Image.open("img/icons/text-size.png").resize((icon_size, icon_size))),
    
    "typography": ImageTk.PhotoImage(Image.open("img/icons/typography.png").resize((icon_size, icon_size))),
}
