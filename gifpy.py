import importlib.util
import subprocess
import os

try:
    from moviepy.editor import VideoFileClip
except ModuleNotFoundError:
    print("moviepy is not installed. Installing...")
    subprocess.check_call(["pip", "install", "moviepy"])
    from moviepy.editor import VideoFileClip

try:
    import tkinter as tk
    from tkinter import filedialog
except ModuleNotFoundError:
    print("tkinter is not installed. Installing...")
    subprocess.check_call(["pip", "install", "tkinter"])
    import tkinter as tk
    from tkinter import filedialog

root = tk.Tk()
root.withdraw()  # Hide the root window

file_path = filedialog.askopenfilename(title="Select .mkv file",
                                       filetypes=(("MKV files", "*.mkv"), ("All files", "*.*")))
if file_path:
    # User selected a file
    print("Selected file:", file_path)
    # Now you can call your conversion function with file_path
else:
    # User cancelled the selection
    print("No file selected.")

def convert_mkv_to_gif(input_path, output_path=None):
    def get_available_filename(output_path):
        filename, extension = os.path.splitext(output_path)
        if not os.path.exists(output_path):
            return output_path
        index = 1
        while True:
            new_output_path = f"{filename}_{index}{extension}"
            if not os.path.exists(new_output_path):
                return new_output_path
            index += 1

    if output_path is None:
        output_filename = os.path.basename(input_path).split('.')[0]
        output_path = get_available_filename(f"{output_filename}.gif")
    else:
        output_path = get_available_filename(output_path)
    clip = VideoFileClip(input_path)
    clip.write_gif(output_path)
    return output_path

if __name__ == "__main__":
    mkv_file_path = file_path  # Use the file selected through tkinter
    gif_output_path = None  # Use default output filename based on input filename
    gif_output_path = convert_mkv_to_gif(mkv_file_path, gif_output_path)
    if os.path.exists(gif_output_path):
        print("GIF file was successfully created:", gif_output_path)
    else:
        print("Failed to create GIF file.")