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
    apply_laplacian()

def apply_laplacian():
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    laplacian = cv2.Laplacian(img, cv2.CV_64F)
    
    laplacian = cv2.normalize(laplacian, None, 0, 255, cv2.NORM_MINMAX)
    
    laplacian_img = Image.fromarray(laplacian.astype('uint8'))
    laplacian_img.thumbnail((300, 300))
    laplacian_img = ImageTk.PhotoImage(laplacian_img)
    
    configure_label(lbl_transformed_image, laplacian_img)

def start():
    window = tk.Tk()
    window.title("Laplacian Filter")

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
