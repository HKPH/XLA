import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import cv2
import numpy as np

def open_image():
    file_path = filedialog.askopenfilename()
    img = Image.open(file_path)
    img.thumbnail((300, 300))
    img = ImageTk.PhotoImage(img)
    lbl_original_image.configure(image=img)
    lbl_original_image.image = img
    global image_path
    image_path = file_path
    apply_weighted_average_filter()

def apply_weighted_average_filter():
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    kernel = np.array([[1, 2, 1], [2, 4, 2], [1, 2, 1]], dtype=np.float32) / 16
    weighted_avg_filtered = cv2.filter2D(img, -1, kernel)
    weighted_avg_filtered = Image.fromarray(weighted_avg_filtered)
    weighted_avg_filtered.thumbnail((300, 300))
    weighted_avg_filtered = ImageTk.PhotoImage(weighted_avg_filtered)
    lbl_transformed_image.configure(image=weighted_avg_filtered)
    lbl_transformed_image.image = weighted_avg_filtered

def start():
    window = tk.Tk()
    window.title("Weighted Average Filter")

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
