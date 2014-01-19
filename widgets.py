import cec

class Widget:
    def __init__(self):
        # TODO Handle position and dimensions
        # self._parent = parent
        pass

    @property
    def parent(self):
        return self._parent

    def key_callback(self, key_code, duration):
        pass

    def activate(self):
        print("Activated %s" % self)

    def deactivate(self):
        print("Deactivated %s" % self)

    def render(self, at, dim):
        pass

    def min_size(self):
        return 0

class Split(Widget):
    def __init__(self, orientation="v", infinite=False, **kwargs):
        self._infinite = infinite
        self._children = []
        if orientation.startswith("h"):
            self._plus = cec.key_code.right
            self._minus = cec.key_code.left
        elif orientation.startswith("v"):
            self._plus = cec.key_code.down
            self._minus = cec.key_code.up
        else:
            raise RuntimeError("Invalid orientation: %s" % orientation)
        
        self.__current = 0

        super().__init__(**kwargs)

    def key_callback(self, key_code, duration):
        w = self._children[self.__current]
        if w.key_callback(key_code, duration):
            return True
        else:
            if key_code == self._plus:
                return self.advance(+1, infinite=self._infinite)
            elif key_code == self._minus:
                return self.advance(-1, infinite=self._infinite)
            return False

    def advance(self, direction, infinite=False):
        direction = direction // abs(direction)

        l = len(self._children)

        new = self.__current + direction

        while self.__current != new:
            if (0 <= new < l) or infinite:
                new = new % l
                if self._children[new].activate():
                    self._children[self.__current].deactivate()
                    self.__current = new
                    return True
                else:
                    new += direction
            else:
                break

    def activate(self):
        if self._children[self.__current].activate():
            return True
        else:
            return self.advance(+1, infinite=True)

    def deactivate(self):
        if len(self._children) > 0:
            self._children[self.__current].deactivate()

    def clear(self):
        self.__current = 0
        self._children.clear()

    def add_children(self, child):
        self._children.append(child)

    def render(self, visitor):
        visitor.render_list(self._children)

class Scrollable(Split):
    pass

class TextRect(Widget):
    def __init__(self, text, fg_color=(1,1,1,1), bg_color=(0,0,0,1),
                             font_size=16, font="DejaVuSans.ttf", **kwargs):
        super().__init__(**kwargs)
        self.__fg = fg_color
        self.__bg = bg_color

        self.__text = text

    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, val):
        self.__text = val

    def __repr__(self):
        return "<TextRect '%s'>" % self.__text

    def render(self):
        pass

