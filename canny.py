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
    apply_canny()

def apply_canny():
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    edges = cv2.Canny(img, 100, 200)
    edges_img = Image.fromarray(edges)
    edges_img.thumbnail((300, 300))
    edges_img = ImageTk.PhotoImage(edges_img)
    configure_label(lbl_transformed_image, edges_img)

def start_application():
    window = tk.Tk()
    window.title("Canny Edge Detection")

    btn_open_image = tk.Button(window, text="Open Image", command=open_image)
    btn_open_image.pack()

    global lbl_original_image
    lbl_original_image = tk.Label(window)
    lbl_original_image.pack(side="left", padx=10)

    global lbl_transformed_image
    lbl_transformed_image = tk.Label(window)
    lbl_transformed_image.pack(side="right", padx=10)

    window.geometry("800x400+{}+{}".format(
        window.winfo_screenwidth() // 2 - 300,
        window.winfo_screenheight() // 2 - 200
    ))

    window.mainloop()

if __name__ == "__main__":
    start_application()
