import globals

class Coordinate:
    def __init__(self, xy, total_size=None):
        x, y = xy
        if type(x) == type(y) == int:       # Given in pixels (absolute)
            W, H = total_size
            self._relative_x = x / W
            self._relative_y = y / H

        elif type(x) == type(y) == float:   # Given in proportions (relative)
            self._relative_x = x
            self._relative_y = y

        else: 
            raise Exception('Exception in Coordinate __init__ !!')

    def relative(self):
        return (self._relative_x, self._relative_y)
    
    def absolute(self, window_size):
        W, H = window_size
        return (int(self._relative_x * W), int(self._relative_y * H))
    
    @property
    def rel(self):
        return self.relative()

    @property
    def abs(self):
        return self.absolute(globals.window_size())
