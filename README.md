# Monitor de CPU em Tempo Real (Python)
Uma aplicação Desktop desenvolvida com CustomTkinter que monitora a saúde do computador via telemetria.

O que aprendi/apliquei:

Bibliotecas: Uso do psutil para leitura de sensores do sistema operacional e CustomTkinter para UI moderna.

Lógica de Refresh: Implementação de loops de atualização (callbacks) para monitoramento contínuo sem travar a interface.

Tratamento de Dados: Conversão de dados brutos do sistema em feedback visual (barra de progresso).

### 🚦 Lógica de Cores (HMI Alarm Colors)
Implementei um sistema de feedback visual inspirado em interfaces industriais (HMI), onde a cor da barra indica a gravidade da carga de trabalho instantaneamente, permitindo que o operador avalie a situação sem precisar ler os números exatos:

* **🟢 Verde (0% - 49%):** Operação Normal (Safe)
* **🟡 Amarelo (50% - 59%):** Atenção (Warning)
* **🟠 Laranja (60% - 69%):** Alerta Alto (High Alert)
* **🔴 Vermelho (70% - 100%):** Crítico (Critical)
