from youtube_dl import YoutubeDL
from .omx_handler import OmxRequestHandler

_ytdl = YoutubeDL(dict(forceurl=True, skip_download=True, restrictfilenames=False))
_ytdl.add_default_info_extractors()

class YtDlHandler(OmxRequestHandler):
    def get_location(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        loc = self.get_argument("location")

        info = _ytdl.extract_info(loc, download=False)

        return info["url"]

