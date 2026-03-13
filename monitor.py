import psutil

CPU_LIMIT = 80
RAM_LIMIT = 80
DISK_LIMIT = 80

def check_cpu():
    return psutil.cpu_percent(interval=1)

def check_ram():
    return psutil.virtual_memory().percent

def check_disk():
    return psutil.disk_usage('/').percent

def show_status():
    cpu = check_cpu()
    ram = check_ram()
    disk = check_disk()

    print("=== MONITORAMENTO DO SERVIDOR ===")
    print(f"CPU: {cpu}%")
    print(f"RAM: {ram}%")
    print(f"DISCO: {disk}%")
    print()

    if cpu > CPU_LIMIT:
        print("ALERTA: uso de CPU acima do limite")

    if ram > RAM_LIMIT:
        print("ALERTA: uso de memória RAM acima do limite")

    if disk > DISK_LIMIT:
        print("ALERTA: uso de disco acima do limite")

if __name__ == "__main__":
    show_status()
