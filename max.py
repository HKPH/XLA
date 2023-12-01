import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import cv2
import numpy as np

def configure_label(label, image):
    label.configure(image=image)
    label.image = image

def open_image():
    file_path = filedialog.askopenfilename()
    img = Image.open(file_path)
    img.thumbnail((300, 300))
    img = ImageTk.PhotoImage(img)
    configure_label(lbl_original_image, img)
    global image_path
    image_path = file_path
    apply_max_filter()

def apply_max_filter():
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    kernel = np.ones((3, 3), np.uint8)
    max_img = cv2.dilate(img, kernel, iterations=1)
    
    max_img = Image.fromarray(max_img)
    max_img.thumbnail((300, 300))
    max_img = ImageTk.PhotoImage(max_img)
    
    configure_label(lbl_transformed_image, max_img)

def start():
    window = tk.Tk()
    window.title("Max Filter")

    btn_open_image = tk.Button(window, text="Open Image", command=open_image)
    btn_open_image.pack()

    global lbl_original_image, lbl_transformed_image
    lbl_original_image = tk.Label(window)
    lbl_original_image.pack(side="left", padx=10)

    lbl_transformed_image = tk.Label(window)
    lbl_transformed_image.pack(side="right", padx=10)

    window.geometry("800x400+{}+{}".format(
        window.winfo_screenwidth() // 2 - 400,
        window.winfo_screenheight() // 2 - 200
    ))

    window.mainloop()

if __name__ == "__main__":
    start()
