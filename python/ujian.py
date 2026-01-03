import tkinter as tk
from tkinter import messagebox

USERNAME_BENAR = "1"  
PASSWORD_BENAR = "123"    

def login():
    user = entry_username.get()
    pwd = entry_password.get()

    if user == USERNAME_BENAR and pwd == PASSWORD_BENAR:
        messagebox.showinfo("Sukses", "Login Berhasil!")
        root.withdraw() 
        buka_kasir()   
    else:
        messagebox.showerror("Gagal", "Username atau Password Salah!")

def buka_kasir():
    kasir_window = tk.Toplevel()
    kasir_window.title(" 💫 Kasir 💫") 
    kasir_window.geometry("300x500")
    
    tk.Label(kasir_window, text="Nama Pembeli").pack(pady=(10,0))
    entry_nama = tk.Entry(kasir_window)
    entry_nama.pack()

    tk.Label(kasir_window, text="Nama Barang:").pack(pady=(5,0))
    entry_barang = tk.Entry(kasir_window)
    entry_barang.pack()

    tk.Label(kasir_window, text="Jumlah Produk: (Angka)").pack(pady=(5,0))
    entry_jumlah = tk.Entry(kasir_window)
    entry_jumlah.pack()

    tk.Label(kasir_window, text="Harga Produk: (Angka)").pack(pady=(5,0))
    entry_harga = tk.Entry(kasir_window)
    entry_harga.pack()

    tk.Label(kasir_window, text="Uang Pembeli: (Angka)").pack(pady=(5,0))
    entry_bayar = tk.Entry(kasir_window)
    entry_bayar.pack()

    def cetak_invoice():
        try:
            if not entry_jumlah.get().isdigit() or not entry_harga.get().isdigit() or not entry_bayar.get().isdigit():
                messagebox.showerror("Error", "Jumlah, Harga, dan Uang harus berupa Angka!")
                return

            nama_pembeli = entry_nama.get()
            nama_barang = entry_barang.get()
            jumlah = int(entry_jumlah.get()) 
            harga = int(entry_harga.get())   
            bayar = int(entry_bayar.get())   
            
            total_belanja = jumlah * harga
            kembali = bayar - total_belanja
            
            if bayar < total_belanja:
                messagebox.showwarning("Warning", "Uang pembeli kurang!")
                return
            
            invoice_text = f"""
Nama Pembeli = {nama_pembeli}
Nama Barang = {nama_barang}
Jumlah Barang = {jumlah}
Harga Rp. {harga}

Total = Rp. {total_belanja}
Tunai = Rp. {bayar}

Kembali = Rp. {kembali}

Terima Kasih Telah Berbelanja!!
            """
            messagebox.showinfo("Struk", invoice_text)
            
        except Exception:
            messagebox.showerror("Error", "Terjadi kesalahan input data.")

    tk.Button(kasir_window, text="Total", command=cetak_invoice, width=10).pack(pady=20)

root = tk.Tk()
root.title(" 💫 Login 💫") 
root.geometry("300x250")

tk.Label(root, text="Username").pack(pady=(20,0))
entry_username = tk.Entry(root)
entry_username.pack()

tk.Label(root, text="Password").pack(pady=(10,0))
entry_password = tk.Entry(root, show="*") 
entry_password.pack()

tk.Button(root, text="Login", command=login, width=10).pack(pady=20)

root.mainloop()