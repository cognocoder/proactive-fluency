
class DisplayFontConfig:
    mono = "Liberation Mono"
    sans = "Liberation Sans"
    serif = "Liberation Serif"
    size = 12

class TextFontConfig:
    names = ["HanyiSentyTang", "Hanyi Senty Lingfei Scroll", "KaiTi", "Noto Sans CJK SC"]
    sizes = [60, 72, 18, 24, 36, 48]

class IconConfig:
    size = 24

class LanguageConfig:
    supported = ["zh-cn", "ja-jp", "en-us", "pt-br"]

class ThemeConfig:
    bg = "#242424"
    bghover = "#424242"
    bgactive = "#606060"
    fg = "#F2F2F2"
    fghover = "#d0d0d0"

class WindowConfig:
    size = "1600x900"
    title = "Proactive Fluency"

    font = DisplayFontConfig()

class AppConfig:
    fonts = TextFontConfig()
    icon = IconConfig()
    language = LanguageConfig()
    theme = ThemeConfig()
    window = WindowConfig()

CONFIG = AppConfig()
