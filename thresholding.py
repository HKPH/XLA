import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import cv2
import numpy as np

def thresholding(image_path, threshold):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    thresholded_img = np.where(img > threshold, 1.0, 0.0)
    return thresholded_img

def configure_label(label, image):
    label.configure(image=image)
    label.image = image

def open_image():
    # Mở ảnh và hiển thị
    file_path = filedialog.askopenfilename()
    img = Image.open(file_path)
    img.thumbnail((300, 300))
    img = ImageTk.PhotoImage(img)
    configure_label(lbl_original_image, img)
    global image_path
    image_path = file_path
    apply_thresholding()

def apply_thresholding():
    threshold = int(entry_threshold.get())
    thresholded_img = thresholding(image_path, threshold)
    thresholded_img = np.uint8(thresholded_img * 255)
    thresholded_img = cv2.cvtColor(thresholded_img, cv2.COLOR_GRAY2BGR)
    thresholded_img = Image.fromarray(thresholded_img)
    thresholded_img.thumbnail((300, 300))
    thresholded_img = ImageTk.PhotoImage(thresholded_img)
    configure_label(lbl_transformed_image, thresholded_img)

def start():
    window = tk.Tk()
    window.title("Thresholding Transformation")

    global entry_threshold
    tk.Label(window, text="Threshold Value:").pack()
    entry_threshold = tk.Entry(window)
    entry_threshold.pack()

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
