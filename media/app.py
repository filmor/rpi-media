import cec, time

class Application:
    def __init__(self, initial_widget):
        self._widget = initial_widget

        self._running = False

        self._adapter = cec.Adapter()
        # self._adapter.open()

        self._adapter.set_callback(cec.cb_type.key, self._key_callback)

    def _key_callback(self, key_code, duration):
        self._widget.key_callback(key_code, duration)
        if key_code == cec.key_code.select:
            pass
        elif key_code == cec.key_code.up:
            pass
        elif key_code == cec.key_code.down:
            pass
        elif key_code == cec.key_code.left:
            pass
        elif key_code == cec.key_code.right:
            pass
        elif key_code == cec.key_code.exit:
            pass

    def set_scene(self, scene):
        self._widget.deactivate()
        self._widget = scene
        self._widget.activate()

    def render(self):
        #bcm.host_init()
        self._adapter.open()
        #dim = bcm.graphics_get_display_size(0)

    def run(self):
        self.render()
        self._running = True
        while self._running:
            time.sleep(1)

