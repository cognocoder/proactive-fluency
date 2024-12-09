
from PIL import Image, ImageTk

from window import ROOT

icon_size = ROOT["icon"]["size"]

ICONS = {
    "play": ImageTk.PhotoImage(Image.open("images/icons/player-play.png").resize((icon_size, icon_size))),
    "record": ImageTk.PhotoImage(Image.open("images/icons/player-record.png").resize((icon_size, icon_size))),
    "save": ImageTk.PhotoImage(Image.open("images/icons/device-floppy.png").resize((icon_size, icon_size))),
    "stop": ImageTk.PhotoImage(Image.open("images/icons/player-stop.png").resize((icon_size, icon_size))),
    "typography": ImageTk.PhotoImage(Image.open("images/icons/typography.png").resize((icon_size, icon_size))),
}
