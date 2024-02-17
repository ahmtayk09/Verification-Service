import tkinter as tk
import time
import servis
import random
from tkinter import messagebox
import os

config = open("config.txt" , "r+") # Kullanıcı Kendi Konumunu ayarlıya bilir.
line = config.readline().strip()
stablekod = line
kod = "4u37u412037819412 3n2cn19"
def kapat_buton_tiklandi():
    onay = messagebox.askokcancel("Kapatma Onayı", "Bilgisayarı kapatmak istediğinizden emin misiniz?")
    if onay:
        os.system("shutdown /s /t 1")  # Bilgisayarı kapat

def buton1_tiklandi():
    global kod , stablekod
    pin = giris_kutusu.get()
    if pin == kod:
        messagebox.showinfo("Uyarı", "Kod Doğrulandı 1 Saatiniz Başlamıştır")
        kod = stablekod
        win.withdraw()
        time.sleep(3600)
        win.deiconify()
        messagebox.showinfo("Uyarı", "Süre Bitti Kod İsteyiniz")
    elif pin == "Admin00":
        open_admin_window()
    elif pin == stablekod:
        messagebox.showinfo("Uyarı", "Süresiz Açıldı")
        win.withdraw()
    else:
        messagebox.showinfo("Uyarı", "Kod Yanlış Tekrar Deneyiniz")
def buton2_tiklandi():
        global kod
        kod = random.randint(100000,999999)
        kod = str(kod)
        servis.gönder(kod)
        messagebox.showinfo("Uyarı", "Kod Başarıyla Gönderildi")
        

def on_closing():
    messagebox.showinfo("Uyarı", "Pencere kapatılamaz!")
    pass

def open_admin_window():
    global win
    admin_win = tk.Toplevel(win)
    admin_win.title("Admin Window")
    win.attributes('-topmost', False)
    admin_win.attributes("-topmost" , True)
    def set_stable_code():
        global stablekod , kod , win
        
        new_stable_code = entry_admin.get()
        if new_stable_code:
            # Dosyanın içeriğini oku
            with open("config.txt", "r") as dosya:
                lines = dosya.readlines()

            # İlk satırı güncelle
            lines[0] = new_stable_code + "\n"

            # Dosyayı yeniden yaz
            with open("config.txt", "w") as dosya:
                dosya.writelines(lines)

            stablekod = new_stable_code
            kod = stablekod
            admin_win.destroy()
            win.attributes('-topmost', True)


    label_admin = tk.Label(admin_win, text="Yeni Kod Giriniz:")
    label_admin.pack(pady=10)

    entry_admin = tk.Entry(admin_win)
    entry_admin.pack(pady=10)

    button_admin = tk.Button(admin_win, text="Kaydet", command=set_stable_code)
    button_admin.pack(pady=10)

# Ana pencereyi oluştur
win = tk.Tk()
win.title("Pc Password")

win.protocol("WM_DELETE_WINDOW", on_closing)
win.attributes('-topmost', True)


win.attributes("-fullscreen",True)

# Ekranın ortasına yerleştirme
win.geometry("400x200")
win.eval('tk::PlaceWindow . center')

# Entry (giriş kutusu) oluştur
giris_kutusu = tk.Entry(win)
giris_kutusu.pack(pady=10)

# Buton 1 oluştur
buton1 = tk.Button(win, text="KOD GÖNDER", command=buton1_tiklandi)
buton1.pack(side=tk.TOP, pady=5)

# Buton 2 oluştur
buton2 = tk.Button(win, text="KOD AL", command=buton2_tiklandi)
buton2.pack(side=tk.TOP, pady=5)

kapat_buton = tk.Button(win, text="Bilgisayarı Kapat", command=kapat_buton_tiklandi)
kapat_buton.pack(side=tk.TOP, pady=5)

# Pencereyi çalıştır
win.mainloop()
