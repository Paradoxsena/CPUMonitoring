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
        
        #Sistema HMI Alarm Colors (Cores de Alarme na Interface Homem-Máquina).
        if uso_cpu < 50:
            nova_cor = "#2CC985" # Verde (Seguro)
        elif uso_cpu < 60:
            nova_cor = "#F1C40F" # Amarelo (Atenção)
        elif uso_cpu < 70:
            nova_cor = "#E67E22" # Laranja (Alerta)
        else:
            nova_cor = "#E74C3C" # Vermelho (Crítico)

        # Aplica a cor na barra
        self.barra_cpu.configure(progress_color=nova_cor)

        self.after(1000, self.atualizar_hardware)

if __name__ == "__main__":
    app = MonitorApp()
    app.mainloop()