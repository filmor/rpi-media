from .widgets import Scrollable, TextRect
from collections import Callable, Mapping
import cec

class MenuItem(TextRect):
    def __init__(self, text, on_select=lambda: False):
        self._active_text = (1, 1, 1, 1)
        self._inactive_text = (0.7, 0.7, 0.7, 1)
        self._bg = (0, 0, 1, 0.5)
        self._on_select = on_select

        super().__init__(bg_color=self._bg, fg_color=self._inactive_text,
                         text=text)

    def key_callback(self, key, duration):
        if key == cec.key_code.select:
            return self._on_select()

    def activate(self):
        super().activate()
        return True

    def __repr__(self):
        return "<MenuItem '%s'>" % self.text


class Menu(Scrollable):
    def __init__(self, definition, **kwargs):
        self._definition = definition
        self._current = definition
        self._path = []

        super().__init__(**kwargs)
        self._fill()

    def _change_path(self, name):
        if name == "..":
            if len(self._path) > 0:
                self._path.pop()
                self._current = self._definition
                for p in self._path:
                    self._current = self._current[p]
        else:
            self._current = self._current[name]
            self._path.append(name)

        self._fill()

    def key_callback(self, key, duration):
        if not super().key_callback(key, duration):
            if key == cec.key_code.exit and len(self._path) > 0:
                self._change_path("..")
                return True

    def _fill(self):
        super().deactivate()
        super().clear()

        for name, value in self._current.items():
            on_select = None

            if isinstance(value, Mapping):
                on_select = lambda: self._change_path(name)
            elif isinstance(value, Callable):
                on_select = lambda: value()
            elif value is None:
                on_select = lambda: None

            super().add_children(MenuItem(name, on_select))

        super().activate()

