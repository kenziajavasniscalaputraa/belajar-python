import tkinter as tk
from tkinter import messagebox
import math

def hitung_keliling():
    try:
        r = float(entry_jari.get())
        keliling = 2 * math.pi * r
        label_hasil.config(text=f"Keliling: {keliling:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Masukkan angka yang bener woi!")

# --- UI ---
root = tk.Tk()
root.title("Kalkulator Keliling Lingkaran")
root.geometry("350x200")
root.configure(bg="#1e1e2f")

label_judul = tk.Label(root, text="💫 Kalkulator Keliling Lingkaran 💫", 
                       font=("Segoe UI", 12, "bold"), fg="white", bg="#1e1e2f")
label_judul.pack(pady=10)

frame = tk.Frame(root, bg="#1e1e2f")
frame.pack(pady=5)

label_jari = tk.Label(frame, text="Jari-jari (r):", font=("Segoe UI", 10), fg="white", bg="#1e1e2f")
label_jari.grid(row=0, column=0, padx=5, pady=5)
entry_jari = tk.Entry(frame, font=("Segoe UI", 10))
entry_jari.grid(row=0, column=1, padx=5, pady=5)

btn_hitung = tk.Button(root, text="Hitung 🔥", font=("Segoe UI", 10, "bold"), 
                       bg="#00adb5", fg="white", activebackground="#007b83", 
                       relief="flat", command=hitung_keliling)
btn_hitung.pack(pady=10)

label_hasil = tk.Label(root, text="Keliling: -", font=("Segoe UI", 10, "bold"), 
                       fg="#00ffcc", bg="#1e1e2f") 
label_hasil.pack(pady=5)

root.mainloop()