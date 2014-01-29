from tornado.web import RequestHandler
from pyomxplayer import OMXPlayer

from os.path import join

_current_player = None

class OmxRequestHandler(RequestHandler):
    def get_location(self):
        return join("/media/video", self.get_argument("location"))

    def get(self):
        global _current_player
        action = self.get_argument("action")
        print(action, _current_player)

        if action == "play":
            location = self.get_location()
            if _current_player is not None:
                _current_player.stop()

            _current_player = OMXPlayer(location, args="-p")
            _current_player.play()

        elif action == "download":
            if location.startswith("http"):
                self.redirect(self.get_location())
        else:
            if _current_player is not None:
                getattr(_current_player, action)()

