import importlib

def load_bot(bot_name):
    try:
        bot_module = importlib.import_module('bots.' + bot_name)
        bot_class = getattr(bot_module, bot_name)
        return(bot_class())
    except ImportError:
        print("No bot by name " + bot_name + " found!")
        exit(1)

class colors:
    BLACK   = "\033[0;30m"
    RED     = "\033[1;31m"
    GREEN   = "\033[0;32m"
    YELLOW  = "\033[0;33m"
    BLUE    = "\033[0;34m"
    MAGENTA = "\033[0;35m"
    CYAN    = "\033[0;36m"
    WHITE   = "\033[0;37m"
    ENDC    = "\033[0;0m"

class shapes:
    BAR_V = u"\u2551"
    BAR_H = u"\u2550"
    BAR_TOP_LEFT = u"\u2554"
    BAR_TOP_RIGHT = u"\u2557"
    BAR_BOTTOM_LEFT = u"\u255A"
    BAR_BOTTOM_RIGHT = u"\u255D"

    CIRCLE = u"\u2B24"
    HOLLOW_CIRCLE = u"\u25CB"
    LARGE_CIRCLE = u"\u25EF"
