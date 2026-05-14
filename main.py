import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

def run_app():
    root = tk.Tk()
    root.title("The Catholic Test")
    root.geometry("900x550")
    root.configure(bg="#f4f4f4")

    try:

        pil_img = Image.open("Aquinas1.png")
        pil_img.thumbnail((400, 400)) 
        img_tk = ImageTk.PhotoImage(pil_img)
    except Exception as e:
        print(f"Error loading image: {e}")
        img_tk = None


    img_label = tk.Label(root, image=img_tk, bg="#f4f4f4")
    img_label.image = img_tk  # Keep a reference!
    img_label.pack(side="left", padx=30, pady=20)

    right_frame = tk.Frame(root, bg="#f4f4f4")
    right_frame.pack(side="right", expand=True, fill="both", padx=20, pady=40)


    question = "Do you think Jesus was just a really good teacher that God 'adopted' because He was so holy?"
    lbl_q = tk.Label(right_frame, text=question, font=("Arial", 14, "bold"), 
                     wraplength=400, justify="left", bg="#f4f4f4")
    lbl_q.pack(anchor="w", pady=(0, 20))


    btn_frame = tk.Frame(right_frame, bg="#f4f4f4")
    btn_frame.pack(anchor="w", pady=(0, 30))
    
    ttk.Button(btn_frame, text="Yes").pack(side="left", padx=5)
    ttk.Button(btn_frame, text="No").pack(side="left", padx=5)


    hints = [
        "\"In the beginning was the Word, and the Word was with God, and the Word was God.\" — John 1:1",
        "\"Jesus said to them, 'Truly, truly, I say to you, before Abraham was, I am.'\" — John 8:58",
        "\"For in Him all the fullness of Deity dwells in bodily form.\" — Colossians 2:9"
    ]

    tk.Label(right_frame, text="Scriptural Hints:", font=("Arial", 10, "italic"), 
             fg="#555", bg="#f4f4f4").pack(anchor="w")

    for hint in hints:
        lbl_h = tk.Label(right_frame, text=hint, font=("Georgia", 11), 
                         wraplength=400, justify="left", bg="#f4f4f4", pady=10)
        lbl_h.pack(anchor="w")

    root.mainloop()

run_app()