from importlib.resources import open_binary
from tkinter import Frame
from mtgsdk import Card
from os.path import exists
import urllib
from tkinter import Canvas, Tk
from PIL import ImageTk, Image

class GeneratorApp(Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.name = '森'
        self.language = 'Japanese'
        self.set = 'NEO'
        self.ext = 'png'
        self.filename = self.name+"."+self.ext

        # 変数
        if not exists(self.filename):
            image_url = self.get_image_url(self.name, self.set)
            if image_url:
                try:
                    with urllib.request.urlopen(url=image_url) as res:
                        img = res.read()
                except:
                    print("except @ urlopen")
                try:
                    with open(self.filename, mode='wb') as f:
                        f.write(img)
                except:
                    print("except @ write")

        # GUI
        self.master.title(u"TkinterのCanvasを使ってみる")
        self.master.geometry("800x450")   #ウインドウサイズ（「幅x高さ」で指定）
        self.master_frame = Frame(self.master)
        self.master_frame.pack()

        self.canvas = Canvas(self.master_frame, width = 800, height = 450)
        self.canvas.pack()

        # キャンバスのサイズを取得
        self.master_frame.update() # Canvasのサイズを取得するため更新しておく
        self.canvas_width = self.canvas.winfo_width()
        self.canvas_height = self.canvas.winfo_height()

        # 画像の描画
        self.tk_img = ImageTk.PhotoImage(Image.open(self.filename))
        self.canvas.create_image(
            self.canvas_width / 2,       # 画像表示位置(Canvasの中心)
            self.canvas_height / 2,                   
            image=self.tk_img  # 表示画像データ
        )

    def run(self):
        self.master.mainloop()

    @classmethod
    def get_image_url(self, name, set, number=None, language='Japanese'):
        if number:
            cards = Card.where(language=language).where(set=set).where(name=name).where(number=number).all()
        else:
            cards = Card.where(language=language).where(set=set).where(name=name).all()
        
        for card in cards:
            for foreign_name in card.foreign_names:
                if foreign_name.get('name') == name and foreign_name.get('language') == language:
                    image_url = foreign_name.get('imageUrl')
                    if image_url:
                        return image_url
        return None


if __name__ == "__main__":
    #param = sys.argv
    root = Tk()
    app = GeneratorApp(master=root)
    app.run()
