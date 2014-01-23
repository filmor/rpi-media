from tornado.ioloop import IOLoop
from tornado.web import Application
from .ytdl_handler import YtDlHandler

if __name__ == '__main__':
    app = Application([
        ("/yt", YtDlHandler)
        ])

    app.listen(8081)
    IOLoop.instance().start()

