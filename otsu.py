import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import cv2
import numpy as np

def otsu_algorithm(img):
    hist, bins = np.histogram(img.flatten(), 256, [0, 256])

    total_pixels = img.size
    sum_total = 0

    for i in range(256):
        sum_total += i * hist[i]

    sum_background = 0
    weight_background = 0
    max_variance = 0
    threshold = 0

    for i in range(256):
        weight_background += hist[i]
        if weight_background == 0:
            continue

        weight_foreground = total_pixels - weight_background
        if weight_foreground == 0:
            break

        sum_background += i * hist[i]
        mean_background = sum_background / weight_background
        mean_foreground = (sum_total - sum_background) / weight_foreground

        variance_between = weight_background * weight_foreground * (mean_background - mean_foreground)**2

        if variance_between > max_variance:
            max_variance = variance_between
            threshold = i

    return threshold

def apply_otsu():
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    threshold = otsu_algorithm(img)

    thresholded_img = np.where(img > threshold, 255, 0).astype(np.uint8)
    thresholded_img = Image.fromarray(thresholded_img)
    thresholded_img.thumbnail((300, 300))
    thresholded_img = ImageTk.PhotoImage(thresholded_img)
    lbl_transformed_image.configure(image=thresholded_img)
    lbl_transformed_image.image = thresholded_img

def open_image():
    global image_path
    file_path = filedialog.askopenfilename()
    img = Image.open(file_path)
    img.thumbnail((300, 300))
    img = ImageTk.PhotoImage(img)
    lbl_original_image.configure(image=img)
    lbl_original_image.image = img
    image_path = file_path
    apply_otsu()

if __name__ == "__main__":
    window = tk.Tk()
    window.title("Otsu's Algorithm")

    btn_open_image = tk.Button(window, text="Open Image", command=open_image)
    btn_open_image.pack()

    lbl_original_image = tk.Label(window)
    lbl_original_image.pack(side="left", padx=10)

    lbl_transformed_image = tk.Label(window)
    lbl_transformed_image.pack(side="right", padx=10)

    window.geometry("600x400+{}+{}".format(
        window.winfo_screenwidth() // 2 - 300,
        window.winfo_screenheight() // 2 - 200
    ))

    window.mainloop()
