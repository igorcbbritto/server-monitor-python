import psutil
import time
import datetime

CPU_LIMIT = 80
RAM_LIMIT = 80
DISK_LIMIT = 80


def check_cpu():
    return psutil.cpu_percent(interval=1)


def check_ram():
    return psutil.virtual_memory().percent


def check_disk():
    return psutil.disk_usage('C:\\').percent


def log_message(message):
    with open("monitor.log", "a", encoding="utf-8") as log:
        log.write(f"{datetime.datetime.now()} - {message}\n")


def show_status():
    cpu = check_cpu()
    ram = check_ram()
    disk = check_disk()

    print("=== MONITORAMENTO DO SERVIDOR ===")
    print(f"CPU: {cpu}%")
    print(f"RAM: {ram}%")
    print(f"DISCO: {disk}%")
    print()

    log_message(f"CPU: {cpu}% RAM: {ram}% DISK: {disk}%")

    if cpu > CPU_LIMIT:
        print("ALERTA: uso de CPU acima do limite")

    if ram > RAM_LIMIT:
        print("ALERTA: uso de memória RAM acima do limite")

    if disk > DISK_LIMIT:
        print("ALERTA: uso de disco acima do limite")


if __name__ == "__main__":
    while True:
        show_status()
        time.sleep(10)
