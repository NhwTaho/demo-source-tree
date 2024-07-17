import tkinter as tk

class AtarBalsAntivirusApp:
    def __init__(self, root):
        self.root = root
        self.root.title("AtarBals Modern Antivirus")
        self.root.geometry("800x500")
        self.root.configure(bg="white")

        # Sidebar
        self.sidebar_frame = tk.Frame(root, width=200, bg="#4862A3")
        self.sidebar_frame.pack(side=tk.LEFT, fill=tk.Y)

        self.sidebar_title = tk.Label(self.sidebar_frame, text="AtarBals AntiVirus", font=("Helvetica", 16), fg="white", bg="#4862A3")
        self.sidebar_title.pack(pady=20)

        self.sidebar_options = ["Status", "Updates", "Settings", "Share Feedback", "Buy Premium", "Help"]
        for option in self.sidebar_options:
            label = tk.Label(self.sidebar_frame, text=option, font=("Helvetica", 14), fg="white", bg="#4862A3", anchor="w")
            label.pack(fill=tk.X, padx=20, pady=5)

        self.scan_now_button = tk.Button(self.sidebar_frame, text="Scan Now", font=("Helvetica", 14), bg="green", fg="white", command=self.scan_now)
        self.scan_now_button.pack(pady=20, padx=20, fill=tk.X)

        # Main Content
        self.main_frame = tk.Frame(root, bg="white")
        self.main_frame.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)

        self.title_label = tk.Label(self.main_frame, text="Scan", font=("Helvetica", 24), bg="white")
        self.title_label.pack(pady=20)

        self.subtitle_label = tk.Label(self.main_frame, text="Premium will be free forever. You just need to click button.", font=("Helvetica", 14), bg="white")
        self.subtitle_label.pack(pady=10)

        self.buttons_frame = tk.Frame(self.main_frame, bg="white")
        self.buttons_frame.pack(pady=20)

        self.buttons = ["Quick Scan", "Web Protection", "Quarantine", "Full Scan", "Simple Update"]
        for i, button_text in enumerate(self.buttons):
            button = tk.Button(self.buttons_frame, text=button_text, font=("Helvetica", 14), bg="magenta", fg="black", command=lambda bt=button_text: self.perform_action(bt))
            button.grid(row=i//2, column=i%2, padx=20, pady=10, ipadx=10, ipady=5)

        self.status_label = tk.Label(self.main_frame, text="Get Premium to Enable: {Web Protection}, {Full Scan}, {Simple Update}", font=("Helvetica", 12), fg="magenta", bg="white")
        self.status_label.pack(pady=10)

    def scan_now(self):
        self.status_label.config(text="Scan Now button clicked!")

    def perform_action(self, action):
        self.status_label.config(text=f"{action} button clicked!")

if __name__ == "__main__":
    root = tk.Tk()
    app = AtarBalsAntivirusApp(root)
    root.mainloop()

