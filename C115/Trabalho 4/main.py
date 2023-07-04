import paho.mqtt.client as mqtt
import tkinter as tk
from tkinter import ttk
import threading

def on_connect(client, userdata, flags, rc):
    print("Conectado ao broker MQTT")
    client.subscribe("garagem")
    client.subscribe("luzes")
    client.subscribe("arCondicionado")
    client.subscribe("jardim")
    client.subscribe("despertador")
    client.subscribe("alarme")

def on_message(client, userdata, msg):
    print(f"Mensagem recebida: {msg.topic} - {msg.payload.decode()}")

    if msg.topic == "garagem":
        if status_garagem.get() == "Portão fechado":
            status_garagem.set("Portão aberto")
        else:
            status_garagem.set("Portão fechado")

    elif msg.topic == "luzes":
        if msg.payload.decode() == "luzSala":
            if status_luz_sala.get() == "Luz apagada":
                status_luz_sala.set("Luz acesa")
            else:
                status_luz_sala.set("Luz apagada")
        elif msg.payload.decode() == "luzCozinha":
            if status_luz_cozinha.get() == "Luz apagada":
                status_luz_cozinha.set("Luz acesa")
            else:
                status_luz_cozinha.set("Luz apagada")
        elif msg.payload.decode() == "luzQuarto":
            if status_luz_quarto.get() == "Luz apagada":
                status_luz_quarto.set("Luz acesa")
            else:
                status_luz_quarto.set("Luz apagada")
        elif msg.payload.decode() == "luzBanheiro":
            if status_luz_banheiro.get() == "Luz apagada":
                status_luz_banheiro.set("Luz acesa")
            else:
                status_luz_banheiro.set("Luz apagada")

    elif msg.topic == "arCondicionado":
        status_ar_condicionado.set(msg.payload.decode()+"°C")

    elif msg.topic == "jardim":
        if status_jardim.get() == "Regando jardim":
            status_jardim.set("Irrigação desligada")
        else:
            status_jardim.set("Regando jardim")

    elif msg.topic == "despertador":
        status_despertador.set(msg.payload.decode()+"H")

    elif msg.topic == "alarme":
        if status_alarme.get() == "Desligado":
            status_alarme.set("Ligado")
        else:
            status_alarme.set("Desligado")



client = mqtt.Client(client_id="INATEL/C115/SMR")
client.connect("test.mosquitto.org", 1883, 60)
client.on_connect = on_connect
client.on_message = on_message

thread1 = threading.Thread(target=client.loop_forever)
thread1.start()



#Interface
root = tk.Tk()
root.title("Sistema de Monitoramento Residencial")
root.geometry("750x300")
root.configure(background="white")

# Definindo estilos
style = ttk.Style()
style.configure("CustomFrame.TFrame", background="white")

# Status da Luz da Sala
status_luz_sala = tk.StringVar()
luz_sala_frame = ttk.Frame(root, style="CustomFrame.TFrame")
luz_sala_frame.grid(row=0, column=0, padx=20, pady=20)
luz_sala_label = tk.Label(luz_sala_frame, text="Luz da Sala:", font=("Arial", 12, "bold"), bg="white")
luz_sala_status = tk.Label(luz_sala_frame, textvariable=status_luz_sala, font=("Arial", 12), bg="white")
luz_sala_label.pack()
luz_sala_status.pack()

# Status da Luz da Cozinha
status_luz_cozinha = tk.StringVar()
luz_cozinha_frame = ttk.Frame(root, style="CustomFrame.TFrame")
luz_cozinha_frame.grid(row=0, column=1, padx=20, pady=20)
luz_cozinha_label = tk.Label(luz_cozinha_frame, text="Luz da Cozinha:", font=("Arial", 12, "bold"), bg="white")
luz_cozinha_status = tk.Label(luz_cozinha_frame, textvariable=status_luz_cozinha, font=("Arial", 12), bg="white")
luz_cozinha_label.pack()
luz_cozinha_status.pack()

# Status do Quarto
status_luz_quarto = tk.StringVar()
luz_quarto_frame = ttk.Frame(root, style="CustomFrame.TFrame")
luz_quarto_frame.grid(row=0, column=2, padx=20, pady=20)
luz_quarto_label = tk.Label(luz_quarto_frame, text="Luz do Quarto:", font=("Arial", 12, "bold"), bg="white")
luz_quarto_status = tk.Label(luz_quarto_frame, textvariable=status_luz_quarto, font=("Arial", 12), bg="white")
luz_quarto_label.pack()
luz_quarto_status.pack()

# Status do Banheiro
status_luz_banheiro = tk.StringVar()
luz_banheiro_frame = ttk.Frame(root, style="CustomFrame.TFrame")
luz_banheiro_frame.grid(row=1, column=0, padx=20, pady=20)
luz_banheiro_label = tk.Label(luz_banheiro_frame, text="Luz do Banheiro:", font=("Arial", 12, "bold"), bg="white")
luz_banheiro_status = tk.Label(luz_banheiro_frame, textvariable=status_luz_banheiro, font=("Arial", 12), bg="white")
luz_banheiro_label.pack()
luz_banheiro_status.pack()

# Status do Garagem
status_garagem = tk.StringVar()
garagem_frame = ttk.Frame(root, style="CustomFrame.TFrame")
garagem_frame.grid(row=1, column=1, padx=20, pady=20)
garagem_label = tk.Label(garagem_frame, text="Portão da Garagem:", font=("Arial", 12, "bold"), bg="white")
garagem_status = tk.Label(garagem_frame, textvariable=status_garagem, font=("Arial", 12), bg="white")
garagem_label.pack()
garagem_status.pack()

# Status do Jardim
status_jardim = tk.StringVar()
jardim_frame = ttk.Frame(root, style="CustomFrame.TFrame")
jardim_frame.grid(row=1, column=2, padx=20, pady=20)
jardim_label = tk.Label(jardim_frame, text="Jardim:", font=("Arial", 12, "bold"), bg="white")
jardim_status = tk.Label(jardim_frame, textvariable=status_jardim, font=("Arial", 12), bg="white")
jardim_label.pack()
jardim_status.pack()

# Status do Ar Condicionado
status_ar_condicionado = tk.StringVar()
ar_condicionado_frame = ttk.Frame(root, style="CustomFrame.TFrame")
ar_condicionado_frame.grid(row=2, column=0, padx=20, pady=20)
ar_condicionado_label = tk.Label(ar_condicionado_frame, text="Temperatura do Ar Condicionado:", font=("Arial", 12, "bold"), bg="white")
ar_condicionado_status = tk.Label(ar_condicionado_frame, textvariable=status_ar_condicionado, font=("Arial", 12), bg="white")
ar_condicionado_label.pack()
ar_condicionado_status.pack()

# Status do Despertador
status_despertador = tk.StringVar()
despertador_frame = ttk.Frame(root, style="CustomFrame.TFrame")
despertador_frame.grid(row=2, column=1, padx=20, pady=20)
despertador_label = tk.Label(despertador_frame, text="Despertador:", font=("Arial", 12, "bold"), bg="white")
despertador_status = tk.Label(despertador_frame, textvariable=status_despertador, font=("Arial", 12), bg="white")
despertador_label.pack()
despertador_status.pack()

# Status do Alarme
status_alarme = tk.StringVar()
alarme_frame = ttk.Frame(root, style="CustomFrame.TFrame")
alarme_frame.grid(row=2, column=2, padx=20, pady=20)
alarme_label = tk.Label(alarme_frame, text="Status do Alarme:", font=("Arial", 12, "bold"), bg="white")
alarme_status = tk.Label(alarme_frame, textvariable=status_alarme, font=("Arial", 12), bg="white")
alarme_label.pack()
alarme_status.pack()

status_luz_sala.set("Luz apagada")
status_luz_banheiro.set("Luz apagada")
status_luz_cozinha.set("Luz apagada")
status_luz_quarto.set("Luz apagada")
status_ar_condicionado.set("20°C")
status_despertador.set("8:00H")
status_alarme.set("Desligado")
status_jardim.set("Irrigação desligada")
status_garagem.set("Portão fechado")

root.mainloop()
