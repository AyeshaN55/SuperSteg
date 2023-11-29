
import tkinter as tk
from tkinter import filedialog, messagebox
from app_utils.Carrier import Carrier
from app_utils.BitMsg import BitMsg
from modules.inject import inject
from modules.extract import extract_msg

def create_gui_app():
    # Main window
    window = tk.Tk()
    window.title("SuperSteg")

    # Function to handle file selection
    def select_file():
        file_path = filedialog.askopenfilename(filetypes=[("PNG files", "*.png")])
        if file_path:
            file_entry.delete(0, tk.END)
            file_entry.insert(0, file_path)

    # Function to inject a message
    def inject_message():
        file_path = file_entry.get()
        message = message_entry.get()
        if file_path and message:
            carrier = Carrier(file_path)
            msg = BitMsg(message + 'ÿ')
            inject(carrier, msg)
            carrier.create_image()  # Assuming this saves the modified image
            messagebox.showinfo("Success", "Message injected successfully.")
        else:
            messagebox.showwarning("Warning", "Please select an image and enter a message.")

    # Function to extract a message
    def extract_message():
        file_path = file_entry.get()
        if file_path:
            carrier = Carrier(file_path)
            msg = extract_msg(carrier)
            messagebox.showinfo("Extracted Message", f"Message: {msg}")
        else:
            messagebox.showwarning("Warning", "Please select an image.")

    # UI elements
    file_label = tk.Label(window, text="Select an image:")
    file_label.pack()

    file_entry = tk.Entry(window, width=50)
    file_entry.pack()

    browse_button = tk.Button(window, text="Browse", command=select_file)
    browse_button.pack()

    message_label = tk.Label(window, text="Enter a message:")
    message_label.pack()

    message_entry = tk.Entry(window, width=50)
    message_entry.pack()

    inject_button = tk.Button(window, text="Inject Message", command=inject_message)
    inject_button.pack()

    extract_button = tk.Button(window, text="Extract Message", command=extract_message)
    extract_button.pack()

    # Start the GUI event loop
    window.mainloop()

if __name__ == "__main__":
    create_gui_app()
