from io import BytesIO
from importlib.resources import open_binary
from tkinter import Frame
from mtgsdk import Card
from os.path import exists
import urllib
from tkinter import Button, Canvas, Tk, E, W
from PIL import ImageTk, Image

class GeneratorApp(Frame):
    def __init__(self, master=None):
        super().__init__(master)

        # 定数
        self.APP_NAME = "Decklist Image Generator"
        self.GEOMETRY = "1280x720"
        self.CONFIG_PATH = "config\\config.json"
        self.TMP_POSTSCRIPT_PATH = "tmp.ps"

        self.name = '山'
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
        self.master.title(self.APP_NAME)
        self.master.geometry(self.GEOMETRY)
        self.master_frame = Frame(self.master)
        self.master_frame.pack()

        self.canvas = Canvas(self.master_frame)
        self.canvas.pack()

        # 画像の描画
        self.tk_img = ImageTk.PhotoImage(Image.open(self.filename))
        self.canvas.create_image(0, 0, image=self.tk_img)

        self.export_button = Button(self.master_frame, text="エクスポート", command=self.export)
        self.export_button.pack()

    def export(self):
        ps = self.canvas.postscript()
        Image.open(BytesIO(ps.encode('utf-8'))).save("2017_07.png")

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
