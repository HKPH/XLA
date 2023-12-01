import tkinter as tk
from tkinter import ttk
import os

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")

def launch_algorithm_app(selected_algorithm):
    os.system(f'python {selected_algorithm}.py')

def main_menu():
    window = tk.Tk()
    window.title("Algorithm Selection Menu")
    algorithms = ["canny", "isodata", "k_nearest", "laplacian","max","median","min","negative_transform","otsu","power","prewitt",
                  "robert","simple_average","sobel","thresholding","triangle_thresholding","weighted_average"]

    selected_algorithm_var = tk.StringVar(window)
    selected_algorithm_var.set(algorithms[0]) 

    algorithm_menu = ttk.Combobox(window, textvariable=selected_algorithm_var, values=algorithms)
    algorithm_menu.pack(pady=10)

    btn_launch_algorithm = tk.Button(window, text="Chạy Thuật Toán", command=lambda: launch_algorithm_app(selected_algorithm_var.get()))
    btn_launch_algorithm.pack(pady=10)
    window.update_idletasks()
    center_window(window, window.winfo_width(), window.winfo_height())
    window.mainloop()

if __name__ == "__main__":
    main_menu()
