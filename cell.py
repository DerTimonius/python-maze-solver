from graphics import Line, Point, Window

class Cell:
    def __init__(self, win = None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win
        self.visited = False

    def draw(self, x1: int, y1: int, x2: int, y2: int):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        line = Line(Point(x1, y1), Point(x1, y2))
        self._win.draw_line(line, "gray" if self.has_left_wall else "white")
        line = Line(Point(x1, y1), Point(x2, y1))
        self._win.draw_line(line, "gray" if self.has_top_wall else "white")
        line = Line(Point(x2, y1), Point(x2, y2))
        self._win.draw_line(line, "gray" if self.has_right_wall else "white")
        line = Line(Point(x1, y2), Point(x2, y2))
        self._win.draw_line(line, "gray" if self.has_bottom_wall else "white")

    def draw_move(self, to_cell, undo = False): 
        half_length = abs(self._x2 - self._x1) // 2
        x_center = half_length + self._x1
        y_center = half_length + self._y1

        half_length2 = abs(to_cell._x2 - to_cell._x1) // 2
        x_center2 = half_length2 + to_cell._x1
        y_center2 = half_length2 + to_cell._y1 
        curr_center = Point(x_center, y_center)
        to_center = Point(x_center2, y_center2)
        line_color = "gray" if undo else "red"
        line = Line(curr_center, to_center)
        self._win.draw_line(line, line_color)