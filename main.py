from tkinter import Tk, BOTH, Canvas

'''
    The constructor should take a width and height. This will be the size of the new window we create in pixels.
    It should create a new root widget using Tk() and save it as a data member
    Set the title property of the root widget
    Create a Canvas widget and save it as a data member.
    Pack the canvas widget so that it's ready to be drawn
    Create a data member to represent that the window is "running", and set it to False
'''
class Window:
    def __init__(self, width, height):
        self.root = Tk()
        self.root.title("Maze Solver")
        self.canvas = Canvas(self.root, width=width, height=height)
        self.canvas.pack()
        self.running = False

    # The redraw() method on the window class should simply call the root widget's update_idletasks() and update() methods. Each time this is called, the window will redraw itself.
    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    '''wait_for_close() method

This method should set the data member we created to track the "running" state of the window to True. Next, it should call self.redraw() over and over as long as the running state remains True.
'''
    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()

    '''The close() method

Lastly, the close() method should simply set the running state to False. You'll also need to add another line to the constructor to call the protocol method on the root widget, to connect your close method to the "delete window" action. This will stop your program from running when you close the graphical window.'''
    def close(self):
        self.running = False
        self.root.protocol("WM_DELETE_WINDOW", self.close)
        self.root.mainloop()

def main():
    window = Window(800, 600)
    window.wait_for_close()
    window.close()

if __name__ == "__main__":
    main()