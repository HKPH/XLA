import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import cv2

def open_image():
    file_path = filedialog.askopenfilename()
    img = Image.open(file_path)
    img.thumbnail((300, 300))
    img = ImageTk.PhotoImage(img)
    lbl_original_image.configure(image=img)
    lbl_original_image.image = img
    global image_path
    image_path = file_path
    apply_triangle_thresholding()

def apply_triangle_thresholding():
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    _, thresh_img = cv2.threshold(img, 0, 255, cv2.THRESH_TRIANGLE)
    thresh_img = Image.fromarray(thresh_img)
    thresh_img.thumbnail((300, 300))
    thresh_img = ImageTk.PhotoImage(thresh_img)
    lbl_transformed_image.configure(image=thresh_img)
    lbl_transformed_image.image = thresh_img

def start():
    window = tk.Tk()
    window.title("Triangle Thresholding")

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
