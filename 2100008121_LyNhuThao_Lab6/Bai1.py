
import tkinter as tk

class FrameRecorderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Frame Recorder")
        self.root.geometry("600x300")
        self.root.configure(bg="#D58BDC")

        self.title_label = tk.Label(root, text="Frame Recorder", font=("Helvetica", 24), bg="#D58BDC")
        self.title_label.pack(pady=20)

        self.fps_frame = tk.Frame(root, bg="#D58BDC")
        self.fps_frame.pack(pady=10)

        self.fps_label = tk.Label(self.fps_frame, text="create an", font=("Helvetica", 14), bg="#D58BDC")
        self.fps_label.pack(side=tk.LEFT)

        self.fps_entry = tk.Entry(self.fps_frame, font=("Helvetica", 14))
        self.fps_entry.pack(side=tk.LEFT, padx=5)
        self.fps_entry.insert(0, "100")

        self.fps_suffix_label = tk.Label(self.fps_frame, text="fps video", font=("Helvetica", 14), bg="#D58BDC")
        self.fps_suffix_label.pack(side=tk.LEFT)

        self.button_frame = tk.Frame(root, bg="#D58BDC")
        self.button_frame.pack(pady=20)

        self.pause_button = tk.Button(self.button_frame, text="Pause", font=("Helvetica", 14), command=self.pause_recording)
        self.pause_button.pack(side=tk.LEFT, padx=10)

        self.start_button = tk.Button(self.button_frame, text="Start", font=("Helvetica", 14), command=self.start_recording)
        self.start_button.pack(side=tk.LEFT, padx=10)

        self.end_button = tk.Button(self.button_frame, text="End", font=("Helvetica", 14), command=self.end_recording)
        self.end_button.pack(side=tk.LEFT, padx=10)

        self.status_label = tk.Label(root, text="Recording Paused", font=("Helvetica", 14), bg="#D58BDC")
        self.status_label.pack(pady=10)

    def pause_recording(self):
        self.status_label.config(text="Recording Paused")

    def start_recording(self):
        self.status_label.config(text="Recording Started")

    def end_recording(self):
        self.status_label.config(text="Recording Ended")

if __name__ == "__main__":
    root = tk.Tk()
    app = FrameRecorderApp(root)
    root.mainloop()