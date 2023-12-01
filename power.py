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
    apply_power_law_transformation()

def apply_power_law_transformation():
    try:
        gamma = float(entry_gamma.get())
    except ValueError:
        tk.messagebox.showerror("Error", "Invalid input. Please enter a valid float.")
        return

    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    power_law_img = np.power(img / 255.0, gamma) * 255.0
    power_law_img = power_law_img.astype(np.uint8)

    power_law_img = Image.fromarray(power_law_img)
    power_law_img.thumbnail((300, 300))
    power_law_img = ImageTk.PhotoImage(power_law_img)

    configure_label(lbl_transformed_image, power_law_img)

def start():
    window = tk.Tk()
    window.title("Power Law Transformation")

    tk.Label(window, text="Gamma:").pack()
    global entry_gamma
    entry_gamma = tk.Entry(window)
    entry_gamma.pack()

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
