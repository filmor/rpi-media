from app import Application
from menu import Menu

test_menu = {
        "bla": {
            "blubb": None,
            "brabbel": None
        },
        "bla2": {
            "blubb": None,
            "brabbel": None
        },
    }


app = Application(Menu(test_menu))
# app.run()
