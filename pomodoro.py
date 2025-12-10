
import tkinter as tk
import time
import threading
import winsound  # Sadece Windows için

class PomodoroApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pomodoro Zamanlayıcı")
        self.root.geometry("300x200")
        self.root.resizable(False, False)

        self.dakika = 25
        self.saniye = 0
        self.pomodoro_sayisi = 0
        self.calisma_modu = True
        self.sayac_aktif = False

        self.label = tk.Label(root, text="25:00", font=("Helvetica", 32))
        self.label.pack(pady=20)

        self.status = tk.Label(root, text="Hazır", font=("Helvetica", 12))
        self.status.pack()

        self.start_button = tk.Button(root, text="Başlat", command=self.baslat)
        self.start_button.pack(side="left", padx=20)

        self.stop_button = tk.Button(root, text="Durdur", command=self.durdur)
        self.stop_button.pack(side="left")

        self.reset_button = tk.Button(root, text="Sıfırla", command=self.sifirla)
        self.reset_button.pack(side="left", padx=20)

        self.pomodoro_label = tk.Label(root, text="Tamamlanan: 0", font=("Helvetica", 10))
        self.pomodoro_label.pack(pady=10)

    def geri_sayim(self):
        while self.sayac_aktif and (self.dakika > 0 or self.saniye > 0):
            time.sleep(1)
            if self.saniye == 0:
                if self.dakika > 0:
                    self.dakika -= 1
                    self.saniye = 59
            else:
                self.saniye -= 1

            self.label.config(text=f"{self.dakika:02d}:{self.saniye:02d}")

        if self.sayac_aktif:
            self.zaman_bitti()

    def zaman_bitti(self):
        winsound.Beep(1000, 500)
        if self.calisma_modu:
            self.pomodoro_sayisi += 1
            self.pomodoro_label.config(text=f"Tamamlanan: {self.pomodoro_sayisi}")
            self.status.config(text="Mola Zamanı!")
            self.dakika = 5
            self.saniye = 0
            self.calisma_modu = False
        else:
            self.status.config(text="Yeni Pomodoro")
            self.dakika = 25
            self.saniye = 0
            self.calisma_modu = True

        self.label.config(text=f"{self.dakika:02d}:{self.saniye:02d}")
        self.sayac_aktif = False

    def baslat(self):
        if not self.sayac_aktif:
            self.sayac_aktif = True
            self.status.config(text="Çalışıyor..." if self.calisma_modu else "Mola...")
            threading.Thread(target=self.geri_sayim).start()

    def durdur(self):
        self.sayac_aktif = False
        self.status.config(text="Durdu")

    def sifirla(self):
        self.sayac_aktif = False
        self.calisma_modu = True
        self.dakika = 25
        self.saniye = 0
        self.label.config(text="25:00")
        self.status.config(text="Hazır")

if __name__ == "__main__":
    root = tk.Tk()
    app = PomodoroApp(root)
    root.mainloop()
