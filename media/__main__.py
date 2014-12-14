from .app import Application
from .menu import Menu

test_menu = {
        "bla": {
            "blubb": lambda: print("blubb"),
            "brabbel": None
        },
        "bla2": {
            "blubb": None,
            "brabbel": lambda: print("brabbel")
        },
    }


app = Application(Menu(test_menu))
app.run()
