import tkinter
from PIL import Image, ImageTk

class Application(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title('tkinter canvas trial')
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        global im

        # 画像読み込み
        read_image = Image.open('test_figure.png')

        # canvas作成
        self.test_canvas = tkinter.Canvas(self, width=read_image.width, height=read_image.height)
        self.test_canvas.grid(row=0, column=0)

        # canvasに画像を表示
        im = ImageTk.PhotoImage(image=read_image)
        self.test_canvas.create_image(0, 0, anchor='nw', image=im)
    
    def run(self):
        self.master.mainloop()

global im

if __name__ == "__main__":
    #param = sys.argv
    root = tkinter.Tk()
    app = Application(master=root)
    app.run()
