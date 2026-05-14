import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class CatholicApp:
    def __init__(self, root):
        self.root = root
        self.root.title("The Catholic Test")
        self.root.geometry("900x550")
        self.root.resizable(False, False)
        

        self.white = "#FFFFFF"
        self.light_gray = "#F8F9FA"
        self.sidebar_gray = "#E9ECEF"
        self.text_main = "#212529"
        self.text_muted = "#6C757D"
        self.correct_green = "#28A745" 
        self.wrong_red = "#DC3545"    
        self.accent_blue = "#007BFF"

        self.container = tk.Frame(self.root, bg=self.white)
        self.container.pack(expand=True, fill="both")

        self.show_start_page()

    def clear_frame(self):
        for widget in self.container.winfo_children():
            widget.destroy()

    def show_start_page(self):
        self.clear_frame()
        self.container.configure(bg=self.white)
        

        title_frame = tk.Frame(self.container, bg=self.white)
        title_frame.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(title_frame, text="The Catholic Test", font=("Helvetica", 32, "bold"), 
                 fg=self.text_main, bg=self.white).pack()
        
        tk.Label(title_frame, text="12 Questions on Catholic Theology", font=("Helvetica", 14), 
                 fg=self.text_muted, bg=self.white).pack(pady=10)


        tk.Button(title_frame, text="START TEST", font=("Helvetica", 11, "bold"), 
                  bg=self.accent_blue, fg="white", relief="flat", 
                  padx=40, pady=12, cursor="hand2", command=self.show_test_page).pack(pady=20)

    def show_test_page(self):
        self.clear_frame()
        

        sidebar = tk.Frame(self.container, bg=self.sidebar_gray, width=400)
        sidebar.pack(side="left", fill="y")
        sidebar.pack_propagate(False)

        try:
            pil_img = Image.open("Aquinas1.png")
            pil_img.thumbnail((360, 360))
            self.img_tk = ImageTk.PhotoImage(pil_img)
            tk.Label(sidebar, image=self.img_tk, bg=self.sidebar_gray).pack(expand=True)
        except:
            tk.Label(sidebar, text="[St. Thomas Aquinas]", bg=self.sidebar_gray, fg=self.text_muted).pack(expand=True)


        content = tk.Frame(self.container, bg=self.white, padx=40)
        content.pack(side="right", expand=True, fill="both")

        tk.Label(content, text="QUESTION 1", font=("Helvetica", 10, "bold"), 
                 fg=self.accent_blue, bg=self.white).pack(anchor="w", pady=(50, 0))
        
        lbl_q = tk.Label(content, text="Do you think Jesus was just a really good teacher that God 'adopted' because He was so holy?", 
                         font=("Helvetica", 14), wraplength=420, justify="left", 
                         fg=self.text_main, bg=self.white)
        lbl_q.pack(anchor="w", pady=20)


        btn_frame = tk.Frame(content, bg=self.white)
        btn_frame.pack(anchor="w", pady=10)
        

        tk.Button(btn_frame, text="YES", font=("Helvetica", 10, "bold"), bg=self.wrong_red, 
                  fg="white", width=12, relief="flat", pady=8).pack(side="left", padx=5)

        tk.Button(btn_frame, text="NO", font=("Helvetica", 10, "bold"), bg=self.correct_green, 
                  fg="white", width=12, relief="flat", pady=8).pack(side="left", padx=5)


        hint_box = tk.Frame(content, bg=self.light_gray, padx=15, pady=15)
        hint_box.pack(fill="x", pady=30)

        tk.Label(hint_box, text="SCRIPTURAL FOUNDATION", font=("Helvetica", 8, "bold"), 
                 fg=self.text_muted, bg=self.light_gray).pack(anchor="w", pady=(0, 10))

        full_verses = [
            "John 1:1 — \"...the Word was God.\"",
            "John 8:58 — \"...before Abraham was, I am.\"",
            "Colossians 2:9 — \"...fullness of Deity in bodily form.\""
        ]

        for verse in full_verses:
            tk.Label(hint_box, text=verse, font=("Helvetica", 10), bg=self.light_gray, 
                     fg=self.text_main, justify="left", wraplength=380).pack(anchor="w", pady=2)


root = tk.Tk()
app = CatholicApp(root)
root.mainloop()