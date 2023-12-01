import cv2
import numpy as np
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import tkinter as tk

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
    apply_k_median_filter()

def apply_k_median_filter():
    try:
        k = int(entry_k.get())
        threshold = int(entry_threshold.get())
        window_size = int(entry_window_size.get())
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter valid integers.")
        return

    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    rows, cols = img.shape

    filtered_img = np.zeros_like(img)

    for i in range(rows):
        for j in range(cols):
            start_row = max(0, i - window_size // 2)
            end_row = min(rows, i + window_size // 2 + 1)
            start_col = max(0, j - window_size // 2)
            end_col = min(cols, j + window_size // 2 + 1)

            window_values = img[start_row:end_row, start_col:end_col].flatten()
            nearest_values = sorted(window_values, key=lambda x: abs(np.subtract(x, img[i, j])))[:k]

            mean_value = np.mean(nearest_values)

            if abs(img[i, j] - mean_value) <= threshold:
                filtered_img[i, j] = img[i, j]
            else:
                filtered_img[i, j] = mean_value

    filtered_img = Image.fromarray(filtered_img)
    filtered_img.thumbnail((300, 300))
    filtered_img = ImageTk.PhotoImage(filtered_img)
    configure_label(lbl_transformed_image, filtered_img)

def start():
    window = tk.Tk()
    window.title("K Median Filter Application")

    tk.Label(window, text="K Value:").pack()
    global entry_k, entry_threshold, entry_window_size
    entry_k = tk.Entry(window)
    entry_k.pack()

    tk.Label(window, text="Threshold Value:").pack()
    entry_threshold = tk.Entry(window)
    entry_threshold.pack()

    tk.Label(window, text="Window Size:").pack()
    entry_window_size = tk.Entry(window)
    entry_window_size.pack()

    btn_open_image = tk.Button(window, text="Open Image", command=open_image)
    btn_open_image.pack()

    global lbl_original_image, lbl_transformed_image
    lbl_original_image = tk.Label(window)
    lbl_original_image.pack(side="left", padx=10)

    lbl_transformed_image = tk.Label(window)
    lbl_transformed_image.pack(side="right", padx=10)

    window.geometry("800x400+{}+{}".format(
        window.winfo_screenwidth() // 2 - 400,
        window.winfo_screenheight() // 2 - 300
    ))

    window.mainloop()

if __name__ == "__main__":
    start()
