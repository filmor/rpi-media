from tornado.web import RequestHandler
from pyomxplayer import OMXPlayer

_current_player = None

class OmxRequestHandler(RequestHandler):
    def get(self):
        global _current_player
        action = self.get_argument("action")
        print(action)

        if action == "play":
            print(self.get_location())
            if _current_player is not None:
                _current_player.stop()

            _current_player = OMXPlayer(self.get_location(), args="-p")
            _current_player.play()

        elif action == "pause":
            if _current_player is not None:
                _current_player.pause()
        elif action == "stop":
            if _current_player is not None:
                _current_player.stop()
        elif action == "download":
            print(self.get_location())
            self.redirect(self.get_location())

