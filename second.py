import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class CatholicApp:
    def __init__(self, root):
        self.root = root
        self.root.title("The Catholic Test")
        # Larger window to fit theological text and side-by-side columns
        self.root.geometry("1200x650")
        self.root.resizable(False, False)
        
        # Color Palette
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

        sidebar = tk.Frame(self.container, bg=self.sidebar_gray, width=450)
        sidebar.pack(side="left", fill="y")
        sidebar.pack_propagate(False)

        try:
            pil_img = Image.open("Aquinas1.png")
            pil_img.thumbnail((400, 400))
            self.img_tk = ImageTk.PhotoImage(pil_img)
            tk.Label(sidebar, image=self.img_tk, bg=self.sidebar_gray).pack(expand=True)
        except:
            tk.Label(sidebar, text="[St. Thomas Aquinas]", bg=self.sidebar_gray, fg=self.text_muted).pack(expand=True)

        content = tk.Frame(self.container, bg=self.white, padx=50)
        content.pack(side="right", expand=True, fill="both")

        tk.Label(content, text="QUESTION 1", font=("Helvetica", 10, "bold"), 
                 fg=self.accent_blue, bg=self.white).pack(anchor="w", pady=(60, 0))
        
        lbl_q = tk.Label(content, text="Do you think Jesus was just a really good teacher that God 'adopted' because He was so holy?", 
                         font=("Helvetica", 16), wraplength=500, justify="left", 
                         fg=self.text_main, bg=self.white)
        lbl_q.pack(anchor="w", pady=30)

        btn_frame = tk.Frame(content, bg=self.white)
        btn_frame.pack(anchor="w", pady=10)

        # YES triggers the Adoptionism warning panel
        tk.Button(btn_frame, text="YES", font=("Helvetica", 10, "bold"), bg=self.wrong_red, 
                  fg="white", width=15, relief="flat", pady=10, command=self.show_wrong_panel).pack(side="left", padx=5)

        # NO is the correct theological answer
        tk.Button(btn_frame, text="NO", font=("Helvetica", 10, "bold"), bg=self.correct_green, 
                  fg="white", width=15, relief="flat", pady=10, command=self.show_start_page).pack(side="left", padx=5)

        hint_box = tk.Frame(content, bg=self.light_gray, padx=20, pady=20)
        hint_box.pack(fill="x", pady=40)

        tk.Label(hint_box, text="SCRIPTURAL FOUNDATION", font=("Helvetica", 8, "bold"), 
                 fg=self.text_muted, bg=self.light_gray).pack(anchor="w", pady=(0, 10))

        full_verses = [
            "John 1:1 — \"In the beginning was the Word, and the Word was with God, and the Word was God.\"",
            "John 8:58 — \"Truly, truly, I say to you, before Abraham was, I am.\"",
            "Colossians 2:9 — \"For in Him all the fullness of Deity dwells in bodily form.\""
        ]

        for verse in full_verses:
            tk.Label(hint_box, text=verse, font=("Helvetica", 11), bg=self.light_gray, 
                     fg=self.text_main, justify="left", wraplength=550).pack(anchor="w", pady=2)

    def show_wrong_panel(self):
        """This panel only appears if they choose YES"""
        self.clear_frame()
        
        sidebar = tk.Frame(self.container, bg=self.sidebar_gray, width=450)
        sidebar.pack(side="left", fill="y")
        sidebar.pack_propagate(False)

        try:
            tk.Label(sidebar, image=self.img_tk, bg=self.sidebar_gray).pack(expand=True)
        except:
            tk.Label(sidebar, text="[Image Placeholder]", bg=self.sidebar_gray, fg=self.text_muted).pack(expand=True)
        
        content = tk.Frame(self.container, bg=self.white, padx=30)
        content.pack(side="right", expand=True, fill="both")

        # Layout for scriptures (left) and Adoptionism text (right)
        text_container = tk.Frame(content, bg=self.white)
        text_container.pack(fill="both", expand=True, pady=40)

        # Left Column: Scriptural Evidence
        left_col = tk.Frame(text_container, bg=self.white)
        left_col.pack(side="left", fill="both", expand=True, padx=(0, 20))

        verses_data = [
            ("John 1:1", "In the beginning was the Word, and the Word was with God, and the Word was God.", 
             "If the Word was God from the very beginning, He cannot be a man who became God later through adoption. He is the Creator, not a creation."),
            ("John 8:58", "Jesus said to them, 'Truly, truly, I say to you, before Abraham was, I am.'", 
             "By using the name 'I AM' Jesus claims an eternal existence that predates His human birth."),
            ("Colossians 2:9", "For in Him all the fullness of Deity dwells in bodily form.", 
             "The fullness of God's nature is physically present in Him. You cannot adopt 'fullness'.")
        ]

        for ref, txt, exp in verses_data:
            tk.Label(left_col, text=f'"{txt}" {ref}', font=("Helvetica", 10, "bold"), 
                     bg=self.white, fg=self.text_main, justify="left", wraplength=340).pack(anchor="w", pady=(10, 0))
            tk.Label(left_col, text=exp, font=("Helvetica", 9), 
                     bg=self.white, fg=self.text_muted, justify="left", wraplength=340).pack(anchor="w", pady=(2, 5))

        # Right Column: The Error of Adoptionism explanation
        right_col = tk.Frame(text_container, bg=self.white)
        right_col.pack(side="left", fill="both", expand=True)

        explanation = (
            "Wait just a moment! If you say He was merely a man 'adopted' by God, "
            "you fall into the error of Adoptionism.\n\n"
            "The Son is not a promotion given to a human; He is the eternal 'Concept' "
            "of the Father. For the Son to save us, He must be of the same substance "
            "(Homoousios) as the Father.\n\n"
            "If He is not God, He cannot bridge the gap between the Creator and the creature. "
            "He didn't become God, He is God who became man."
        )

        tk.Label(right_col, text=explanation, font=("Helvetica", 11), 
                 bg=self.white, fg=self.text_main, justify="left", wraplength=340).pack(anchor="nw", pady=10)

        # Back button to retry the question
        tk.Button(content, text="TRY AGAIN", font=("Helvetica", 10, "bold"), 
                  bg=self.accent_blue, fg="white", relief="flat", padx=30, pady=12, 
                  command=self.show_test_page).pack(anchor="e", pady=20)


root = tk.Tk()
app = CatholicApp(root)
root.mainloop()