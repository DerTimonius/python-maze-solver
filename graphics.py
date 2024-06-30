from tkinter import Tk, BOTH, Canvas

class Point:
    def __init__(self, x = 0, y = 0) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"x: {self.x}, y: {self.y}"

class Line:
    def __init__(self, p1: Point, p2: Point) -> None:
        self.p1 = p1
        self.p2 = p2

    def draw_line(self, canvas: Canvas, fill_color):
        canvas.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2)

    def __repr__(self) -> str:
        return f"p1: {self.p1}, p2: {self.p2}"

class Window:
    def __init__(self, height, width) -> None:
        self.__root = Tk()
        self.__root.title("A fantastical maze solver")
        self.canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.canvas.pack()
        self.running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
    
    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()

    def close(self):
        self.running = False

    def draw_line(self, line: Line, fill_color = "black"):
        line.draw_line(self.canvas, fill_color)

