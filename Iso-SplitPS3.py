import os
import threading
import customtkinter as ctk
from tkinter import filedialog, messagebox

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

BTN_FONT = ("Segoe UI", 13, "bold")
MAIN_BTN_FONT = ("Segoe UI", 17, "bold")


class ISOSplitter(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("ISO Splitter PS3")
        self.geometry("780x570")
        self.resizable(False, False)
        self.configure(fg_color="#0b0b0b")

        header = ctk.CTkFrame(self, fg_color="transparent")
        header.pack(pady=10)

        ctk.CTkLabel(
            header,
            text="NEX SPLIT",
            font=("Segoe UI", 30, "bold"),
            text_color="#ff2b2b"
        ).pack()

        ctk.CTkLabel(
            header,
            text="PS3 ISO Split Tool Made By Nexxus",
            font=("Segoe UI", 12),
            text_color="#aaaaaa"
        ).pack()

        self.card = ctk.CTkFrame(
            self,
            fg_color="#151515",
            border_color="#ff0000",
            border_width=2,
            corner_radius=10,
        )
        self.card.pack(pady=8, padx=15, fill="both", expand=True)

        self.card.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(
            self.card,
            text="ISO File",
            font=("Segoe UI", 13, "bold"),
            text_color="white"
        ).grid(row=0, column=0, pady=(20, 5))

        self.iso_entry = ctk.CTkEntry(self.card, width=600, height=35)
        self.iso_entry.grid(row=1, column=0)

        ctk.CTkButton(
            self.card,
            text="📂 SELECT ISO",
            font=BTN_FONT,
            width=180,
            height=35,
            fg_color="#cc0000",
            hover_color="#990000",
            command=self.select_iso
        ).grid(row=2, column=0, pady=6)

        ctk.CTkLabel(
            self.card,
            text="Output Folder",
            font=("Segoe UI", 13, "bold"),
            text_color="white"
        ).grid(row=3, column=0, pady=(10, 5))

        self.out_entry = ctk.CTkEntry(self.card, width=600, height=35)
        self.out_entry.grid(row=4, column=0)

        ctk.CTkButton(
            self.card,
            text="📁 SELECT FOLDER",
            font=BTN_FONT,
            width=180,
            height=35,
            fg_color="#cc0000",
            hover_color="#990000",
            command=self.select_folder
        ).grid(row=5, column=0, pady=6)

        size_frame = ctk.CTkFrame(self.card, fg_color="transparent")
        size_frame.grid(row=6, column=0, pady=10)

        ctk.CTkLabel(
            size_frame,
            text="Size GB:",
            font=("Segoe UI", 13, "bold"),
            text_color="#ccc"
        ).pack(side="left", padx=5)

        self.size_entry = ctk.CTkEntry(size_frame, width=80, height=30)
        self.size_entry.pack(side="left")
        self.size_entry.insert(0, "4")

        self.progress = ctk.CTkProgressBar(
            self.card,
            width=600,
            progress_color="#ff0000"
        )
        self.progress.grid(row=7, column=0, pady=10)
        self.progress.set(0)

        self.status = ctk.CTkLabel(
            self.card,
            text="READY",
            font=("Segoe UI", 12, "bold"),
            text_color="#bbbbbb"
        )
        self.status.grid(row=8, column=0)

        self.start_btn = ctk.CTkButton(
            self.card,
            text="🚀 SPLIT ISO",
            font=MAIN_BTN_FONT,
            width=220,
            height=50,
            fg_color="#cc0000",
            hover_color="#990000",
            command=self.start_split
        )
        self.start_btn.grid(row=9, column=0, pady=20)

    def select_iso(self):
        file = filedialog.askopenfilename(filetypes=[("ISO Files", "*.iso")])
        if file:
            self.iso_entry.delete(0, "end")
            self.iso_entry.insert(0, file)
            self.out_entry.delete(0, "end")
            self.out_entry.insert(0, os.path.dirname(file))

    def select_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.out_entry.delete(0, "end")
            self.out_entry.insert(0, folder)

    def start_split(self):
        if not self.iso_entry.get() or not self.out_entry.get():
            messagebox.showerror("Error", "Selectează ISO și folder!")
            return

        self.start_btn.configure(state="disabled")
        threading.Thread(target=self.split_iso, daemon=True).start()

    def split_iso(self):
        try:
            iso = self.iso_entry.get()
            out = self.out_entry.get()

            size_gb = float(self.size_entry.get())
            chunk = int(size_gb * 1024 * 1024 * 1024)

            total_size = os.path.getsize(iso)
            total = (total_size + chunk - 1) // chunk

            base = os.path.splitext(os.path.basename(iso))[0].upper()

            with open(iso, "rb") as f:
                i = 0
                while True:
                    data = f.read(chunk)
                    if not data:
                        break

                    out_file = os.path.join(out, f"{base}.ISO.{i}")
                    with open(out_file, "wb") as w:
                        w.write(data)

                    self.progress.set((i + 1) / total)
                    self.status.configure(text=f"{i+1}/{total}")
                    self.update()

                    i += 1

            self.progress.set(1)
            self.status.configure(text="DONE")

        except Exception as e:
            messagebox.showerror("Error", str(e))

        finally:
            self.start_btn.configure(state="normal")


if __name__ == "__main__":
    app = ISOSplitter()
    app.mainloop()
