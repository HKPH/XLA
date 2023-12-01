import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import cv2

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
    apply_negative_transformation()

def apply_negative_transformation():
    try:
        intensity_max = int(entry_intensity_max.get())
    except ValueError:
        tk.messagebox.showerror("Error", "Invalid input. Please enter a valid integer.")
        return

    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    negative_img = negative_transformation(img, intensity_max)

    negative_img = Image.fromarray(negative_img)
    negative_img.thumbnail((300, 300))
    negative_img = ImageTk.PhotoImage(negative_img)

    configure_label(lbl_transformed_image, negative_img)

def negative_transformation(img, intensity_max):
    negative_img = intensity_max - img
    return negative_img

def start():
    window = tk.Tk()
    window.title("Negative Image Transformation")

    global entry_intensity_max
    tk.Label(window, text="Intensity Max:").pack()
    entry_intensity_max = tk.Entry(window)
    entry_intensity_max.pack()

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
