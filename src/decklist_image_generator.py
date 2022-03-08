from tkinter import filedialog
from mtgsdk import Card
import urllib

name = '森'
language = 'Japanese'
set = 'NEO'

# TODO: GUI化、nameではなくsnumberで判断（あるなら）
cards = Card.where(language=language).where(set=set).where(name=name).all()
img = None
for card in cards:
    flag = False
    for foreign_name in card.foreign_names:
        if foreign_name.get('name') == name and foreign_name.get('language') == language:
            image_url = foreign_name.get('imageUrl')
            if image_url:
                try:
                    with urllib.request.urlopen(url=image_url) as res:
                        img = res.read()
                    flag = True
                except:
                    pass
            break
        if flag:
            break
    if flag:
        break

if img:
    path = filedialog.asksaveasfilename(filetype=[("テキストファイル","*.txt")], initialdir=os.getcwd(), initialfile=filename)
