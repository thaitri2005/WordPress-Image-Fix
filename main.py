import os
from tkinter import Tk, Button, Label, filedialog
from PIL import Image
import tkinter.messagebox as messagebox

# Function to resize the image
def resize_image(input_path, output_path, max_size_mb=4.9):
    try:
        # Open an image file
        with Image.open(input_path) as img:
            # Save the original format
            original_format = img.format

            # Calculate the image file size
            img_size = os.path.getsize(input_path) / (1024 * 1024)  # Convert bytes to MB
            quality = 95  # Start with high quality

            while img_size > max_size_mb and quality > 10:
                # Resize the image by reducing the quality
                img.save(output_path, format=original_format, quality=quality)
                img_size = os.path.getsize(output_path) / (1024 * 1024)  # Check new size
                quality -= 5  # Reduce quality

            # Notify the user if the resize was successful
            if img_size <= max_size_mb:
                messagebox.showinfo("Success", f"Image resized successfully to {round(img_size, 2)} MB.")
            else:
                messagebox.showerror("Error", "Could not reduce the image size to 4.9 MB or less.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Function to select the image and call resize
def select_image():
    # Open a file dialog to select the image
    input_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.jpeg;*.png;*.gif")])
    
    if input_path:
        output_path = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG Image", "*.jpg")])
        if output_path:
            resize_image(input_path, output_path)

# Main GUI setup
def create_gui():
    # Create the main window
    root = Tk()
    root.title("Image Resizer Tool")
    root.geometry("300x150")

    # Add a label
    label = Label(root, text="Resize Image to 4.9 MB or Less", font=("Helvetica", 14))
    label.pack(pady=10)

    # Add a button to select the image
    button = Button(root, text="Select Image", command=select_image, font=("Helvetica", 12))
    button.pack(pady=20)

    # Start the GUI event loop
    root.mainloop()

if __name__ == "__main__":
    create_gui()
