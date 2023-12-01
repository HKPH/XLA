import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import cv2
import numpy as np

def isodata_algorithm(img, initial_threshold=None, delta_threshold=1):
    if initial_threshold is None:
        initial_threshold = np.mean(img)

    threshold = initial_threshold

    while True:
        group1 = img[img <= threshold]
        group2 = img[img > threshold]

        mean1 = np.mean(group1)
        mean2 = np.mean(group2)

        new_threshold = (mean1 + mean2) / 2

        if abs(new_threshold - threshold) < delta_threshold:
            break

        threshold = new_threshold

    return threshold

def apply_isodata():
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    delta_threshold = get_delta_threshold()
    final_threshold = isodata_algorithm(img, None, delta_threshold)
    thresholded_img = np.where(img > final_threshold, 255, 0).astype(np.uint8)
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
    apply_isodata()

def get_delta_threshold():
    try:
        delta_threshold = float(entry_delta_threshold.get())
        return max(0, delta_threshold) 
    except ValueError:
        return 1 

def create_gui():
    window = tk.Tk()
    window.title("Isodata Algorithm")
    window.geometry("800x400+{}+{}".format(
        window.winfo_screenwidth() // 2 - 300,
        window.winfo_screenheight() // 2 - 200
    ))
    tk.Label(window, text="Delta Threshold:").pack()
    global entry_delta_threshold
    entry_delta_threshold = tk.Entry(window)
    entry_delta_threshold.pack()
    
    btn_open_image = tk.Button(window, text="Open Image", command=open_image)
    btn_open_image.pack()

    global lbl_original_image
    lbl_original_image = tk.Label(window)
    lbl_original_image.pack(side="left", padx=10)

    global lbl_transformed_image
    lbl_transformed_image = tk.Label(window)
    lbl_transformed_image.pack(side="right", padx=10)

    return window

if __name__ == "__main__":
    app_window = create_gui()
    app_window.mainloop()
