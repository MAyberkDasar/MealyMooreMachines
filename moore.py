import tkinter as tk
from tkinter import simpledialog
import matplotlib.pyplot as plt

anaPencere = tk.Tk()
anaPencere.title("Moore Makinesi")
anaPencere.geometry("400x300")

durumlar = []
girdiAlfabesi = []
ciktiAlfabesi = []
gecisTablosu = {}
ciktiTablosu = {}

def durumlariAl():
    global durumlar
    durumSayisi = int(simpledialog.askstring("Durum Sayısı", "Durum sayısını giriniz: ", parent= anaPencere))
    durumlar = [simpledialog.askstring("Durum", f"{i+1}. durumu (q0, q1) giriniz: ", parent= anaPencere) for i in range(durumSayisi)]
    print(f"Durumlar: {durumlar}")

def alfabeleriAl():
    global girdiAlfabesi, ciktiAlfabesi
    girdiAlfabesi = simpledialog.askstring("Girdi Alfabesi", "Giriş alfabesini (a,b) giriniz: ", parent= anaPencere).split(",")
    ciktiAlfabesi = simpledialog.askstring("Çıktı Alfabesi", "Çıktı alfabesini (0,1) giriniz: ", parent= anaPencere).split(",")
    print(f"Giriş Alfabesi: {girdiAlfabesi}, Çıktı Alfabesi: {ciktiAlfabesi}")

def gecisTablosuOlustur():
    global gecisTablosu
    gecisTablosu = {}
    for durum in durumlar:
        gecisTablosu[durum] = {}
        for sembol in girdiAlfabesi:
            hedefDurum = simpledialog.askstring("Geçiş Tablosu", f"{durum} durumunda '{sembol}' için hedef durumu giriniz: ", parent= anaPencere)
            gecisTablosu[durum][sembol] = hedefDurum

    print(f"Durumlar ve geçişler: {gecisTablosu}")

def ciktiTablosuOlustur():
    global ciktiTablosu
    ciktiTablosu = {}
    for durum in durumlar:
        cikti = simpledialog.askstring("Çıktı Tablosu", f"{durum} durumunda üretilecek çıktıyı giriniz: ", parent= anaPencere)
        ciktiTablosu[durum] = cikti

    print(f"Durumlar ve çıktılar: {ciktiTablosu}")

def girdiAlVeIsle():
    girdi = simpledialog.askstring("Giriş", "Girişi giriniz: ", parent= anaPencere)
    durum = durumlar[0]
    durumGecisleri = [durum]
    cikti = [ciktiTablosu[durum]]

    print(f"Başlangıç: {durum}, Çıktı: {ciktiTablosu[durum]}")

    for sembol in girdi:
        oncekiDurum = durum
        durum = gecisTablosu[durum][sembol]
        durumGecisleri.append(durum)
        cikti.append(ciktiTablosu[durum])

        print(f"Girdi: {oncekiDurum} - '{sembol}' -> {durum}, Çıktı: {ciktiTablosu[durum]}")

    print(f"Durum Geçişleri: {durumGecisleri}")
    gorsellestir(durumGecisleri, cikti, girdi)

def gorsellestir(durumGecisleri, cikti, girdi):
    plt.figure(figsize=(10, 5))
    plt.plot(range(len(durumGecisleri)), durumGecisleri, linestyle='-', color='b')
    plt.scatter(range(len(durumGecisleri)), durumGecisleri, color='red', zorder=5)
    for i, txt in enumerate(cikti):
        plt.annotate(txt, (i, durumGecisleri[i]), textcoords="offset points", xytext=(0, 10), ha='center')
    plt.title("Moore Makinesi")
    plt.xlabel("Giriş")
    plt.ylabel("Durumlar")
    plt.xticks(range(len(durumGecisleri)), ['Başlangıç'] + list(girdi))
    plt.grid(True)
    plt.show()

tk.Button(anaPencere, text="Durumları Gir", command=durumlariAl).pack(pady=5)
tk.Button(anaPencere, text="Alfabeleri Gir", command=alfabeleriAl).pack(pady=5)
tk.Button(anaPencere, text="Geçiş Tablosu Gir", command=gecisTablosuOlustur).pack(pady=5)
tk.Button(anaPencere, text="Çıktı Tablosu Gir", command=ciktiTablosuOlustur).pack(pady=5)
tk.Button(anaPencere, text="Girdi Gir ve İşle", command=girdiAlVeIsle).pack(pady=5)

anaPencere.mainloop()
