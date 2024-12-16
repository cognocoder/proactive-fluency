
from pathlib import Path
from src.file import delete_goprev, folder_change, save, delete, save_gonext
from src.audio import generate_audio, play_audio, record_audio
from src.binds import keybindsconfig
from src.busy import setbusy
from src.config import CONFIG
from src.font import fontconfig, font_rotatename, font_rotatesize
from src.grid import controlsframe_gridconfig, gridconfig, root_gridconfig
from src.lang import lang_rotate
from src.layout import layoutconfig
from src.state import State, readto_str, readto_textarea
from src.window import Window

state = State()
window = Window()

gridconfig(window)
layoutconfig(window)
keybindsconfig(window.root, text_area=window.textarea)
fontconfig(state.font, window.statuslabel, window.textarea)

from src.buttons import buttons_gridconfig

buttons_gridconfig(window, state)
lastdir = readto_str("lastdir", window.statuslabel)
folder_change(window, state, Path(lastdir) if lastdir else state.dir)

state.openlast(window)
state.setenabled_navbuttons(window.buttons)
readto_textarea(state.dir / f"{state.file.current}.txt", window.textarea, window.statuslabel)

window.buttons["user"]["microphone"].widget.config(
    command=lambda : record_audio(window, state, True))
window.buttons["user"]["microphone-outline"].widget.config(
    command=lambda : record_audio(window, state, False))
window.buttons["user"]["player-play-outline"].widget.config(
    command=lambda : play_audio(window, state, state.getname_byext("wav")))

window.buttons["bot"]["message-chatbot"].widget.config(
    command=lambda : generate_audio(window, state))
window.buttons["bot"]["player-play"].widget.config(
    command=lambda : play_audio(window, state, state.getname_byext("mp3")))

window.buttons["nav"]["first"].widget.config(
    command=lambda : state.gofirst(window))
window.buttons["nav"]["prev"].widget.config(
    command=lambda : state.goprev(window))
window.buttons["nav"]["next"].widget.config(
    command=lambda : state.gonext(window))
window.buttons["nav"]["last"].widget.config(
    command=lambda : state.golast(window))

window.buttons["session"]["save"].widget.config(
    command=lambda : save_gonext(state.dir / f"{state.file.current}.txt", "w+",
        window.textarea.get("1.0", "end-1c"), window.statuslabel, state, window))
window.buttons["session"]["delete"].widget.config(
    command=lambda : delete_goprev(state.dir / f"{state.file.current}.txt", window.statuslabel, state, window))

window.buttons["folder"]["folder"].widget.config(
    command=lambda : folder_change(window, state))

window.buttons["language"]["language"].widget.config(
    command=lambda : lang_rotate(state.lang, window.langstrvar, window.statuslabel))

window.buttons["text"]["text-size"].widget.config(
    command=lambda : font_rotatesize(state.font, window.statuslabel, window.textarea))
window.buttons["text"]["typography"].widget.config(
    command=lambda : font_rotatename(state.font, window.statuslabel, window.textarea))

window.root.mainloop()
