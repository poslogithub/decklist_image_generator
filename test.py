import tkinter
from PIL import Image, ImageTk

def get_concat_h_cut(im1, im2):
    dst = Image.new('RGBA', (im1.width + im2.width + 26, min(im1.height, im2.height)), None)
    dst.alpha_composite(im1, (0, 0))
    dst.alpha_composite(im2, (im1.width + 26, 0))
    return dst

def get_concat_v_cut(im1, im2):
    dst = Image.new('RGBA', (min(im1.width, im2.width), im1.height + im2.height), None)
    dst.alpha_composite(im1, (0, 0))
    dst.alpha_composite(im2, (0, 74))
    return dst

im1 = Image.open("森.png")
im2 = Image.open("山.png")


get_concat_h_cut(im1, im2).save('pillow_concat_h_cut.png')
get_concat_v_cut(im1, im2).save('pillow_concat_v_cut.png')
