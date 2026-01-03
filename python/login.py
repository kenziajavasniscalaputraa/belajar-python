import tkinter as tk
from tkinter import messagebox
import time

MAX_ATTEMPTS = 3
COOLDOWN = 60

# --- UI ---
root = tk.Tk()
root.title("💫 Kenzia Javas Niscala Putra 💫")
root.geometry("534x767")
root.configure(bg="#1e1e2f")
root.attempts = 0
root.cooldown = False

def login():
    if root.cooldown:
        messagebox.showwarning("Cooldown", "Tunggu cooldown selesai!")
        return

    if user_entry.get() == "Kenzia Javas" and pw_entry.get() == "2521":
        messagebox.showinfo("Success", "Login Berhasil!")
        buka_menu()
        root.withdraw()
    else:
        root.attempts += 1
        messagebox.showerror("Error", f"Username/password salah woi! ({root.attempts}/3)")
        if root.attempts >= MAX_ATTEMPTS:
            messagebox.showwarning("Cooldown", f"Terlalu banyak percobaan! Tunggu {COOLDOWN}s.")
            mulai_cooldown()

def mulai_cooldown():
    root.cooldown = True
    login_button.config(state="disabled")
    for i in range(COOLDOWN, 0, -1):
        login_button.config(text=f"Tunggu {i}s")
        root.update()
        time.sleep(1)
    login_button.config(text="Login", state="normal")
    root.cooldown = False
    root.attempts = 0

def buka_menu():
    menu = tk.Toplevel()
    menu.title("Menu Utama")
    menu.geometry("534x767")
    menu.configure(bg="#1e1e2f")

    tk.Label(menu, text="💫 Aplikasi Kasir Sederhana 💫", fg="white", bg="#1e1e2f", font=("Segoe UI", 12, "bold")).pack(pady=5)

    labels = ["Nama Pembeli", "Nama Barang", "Jumlah Produk", "Harga Produk (Rp)", "Uang Pembeli (Rp)"]
    entries = []
    for text in labels:
        frame = tk.Frame(menu, bg="#1e1e2f")
        frame.pack(pady=5)
        tk.Label(frame, text=text, fg="white", bg="#1e1e2f").pack(side="left")
        entry = tk.Entry(frame)
        entry.pack(side="left")
        entries.append(entry)

    name_entry, barang_entry, jumlah_entry, harga_entry, uang_entry = entries

    def hitung_struk():
        try:
            jumlah = int(jumlah_entry.get())
            harga = int(harga_entry.get())
            uang = int(uang_entry.get())
            total = jumlah * harga
            kembalian = uang - total
        except:
            messagebox.showerror("Error", "Masukkan angka yang valid!")
            return
        if kembalian < 0:
            messagebox.showwarning("Kurang", "Uang tidak cukup!")
            return
        struk = (
            f"STRUK PEMBELIAN \n"
            f"Nama Pembeli : {name_entry.get()}\n"
            f"Barang       : {barang_entry.get()}\n"
            f"Jumlah       : {jumlah}\n"
            f"Harga Satuan : Rp {harga}\n"
            f"Total Harga  : Rp {total}\n"
            f"Uang Bayar   : Rp {uang}\n"
            f"Kembalian    : Rp {kembalian}\n"
        )
        messagebox.showinfo("Struk Kembalian", struk)

    tk.Button(menu, text="Total", command=hitung_struk, bg="#00adb5", fg="white", activebackground="#007b83").pack(pady=10)

frame = tk.Frame(root, bg="#1e1e2f")
frame.pack(pady=5)

tk.Label(frame, text="💫 Login 💫", font=("Segoe UI", 14), fg="white", bg="#1e1e2f").grid(row=0, column=0, columnspan=2)
tk.Label(frame, text="Username", fg="white", bg="#1e1e2f").grid(row=1, column=0)
user_entry = tk.Entry(frame)
user_entry.grid(row=1, column=1)
tk.Label(frame, text="Password", fg="white", bg="#1e1e2f").grid(row=2, column=0)
pw_entry = tk.Entry(frame, show="*")
pw_entry.grid(row=2, column=1)
login_button = tk.Button(frame, text="Login", bg="#00adb5", fg="white", activebackground="#007b83", command=login)
login_button.grid(row=3, column=1, pady=10)

root.mainloop() 