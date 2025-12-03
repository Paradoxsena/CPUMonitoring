import customtkinter as ctk
import psutil

class MonitorApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Monitoramento da CPU")
        self.geometry("400x300")

        self.label_titulo = ctk.CTkLabel(self, text="Uso da CPU (Processador)", font=("Arial", 20))
        self.label_titulo.pack(pady=20)

        self.label_porcentagem = ctk.CTkLabel(self, text="0%", font=("Arial", 40, "bold"))
        self.label_porcentagem.pack(pady=10)

        self.barra_cpu = ctk.CTkProgressBar(self, width=300, height=20)
        self.barra_cpu.pack(pady=10)
        self.barra_cpu.set(0)

        self.atualizar_hardware()

    def atualizar_hardware(self):
        uso_cpu = psutil.cpu_percent(interval=0) 
        
        self.label_porcentagem.configure(text=f"{uso_cpu}%")
        
        self.barra_cpu.set(uso_cpu / 100)
        
        if uso_cpu > 80:
            self.label_porcentagem.configure(text_color="red")
        else:
            self.label_porcentagem.configure(text_color="white")

        self.after(1000, self.atualizar_hardware)

if __name__ == "__main__":
    app = MonitorApp()
    app.mainloop()