import psutil
import socket
import csv
import os
import json
from datetime import datetime
import logging


#Logging Setup
logging.basicConfig(
    filename="Logs/automation.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logging.info("Data tracking script started")




try:
    server_name = socket.gethostname()
    cpu_percent = psutil.cpu_percent(interval=1)

    # Memory Usage
    memory = psutil.virtual_memory()
    total_memory = (memory.total) / (1024**3)
    used_memory = memory.used / (1024**3)
    available_memory = memory.available / (1024**3)
    memory_percent = memory.percent

    #DISK
    disk_info = []

    partitions = psutil.disk_partitions(all=False)

    for partition in partitions:
        try:
            usage = psutil.disk_usage(partition.mountpoint)

            disk_info.append({
                "device": partition.device,
                "mountpoint": partition.mountpoint,
                "total_gb": round(usage.total / (1024**3), 2),
                "used_gb": round(usage.used / (1024**3), 2),
                "free_gb": round(usage.free / (1024**3), 2)
            })

        except PermissionError:
            # Skip drives that cannot be accessed
            continue








    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    row = [
        timestamp,
        server_name,
        cpu_percent,
        round(total_memory, 2),
        round(used_memory, 2),
        round(available_memory, 2),
        memory_percent,
        json.dumps(disk_info)   # Convert list to JSON string
    ]


    file_exists = os.path.isfile("metrics/server_metrics.csv")

    with open("metrics/server_metrics.csv", mode="a", newline="") as file:
        writer = csv.writer(file)

        # Write header only if file does not exist
        if not file_exists:
            writer.writerow([
                "timestamp",
                "server_name",
                "cpu_percent",
                "total_ram_gb",
                "used_ram_gb",
                "available_ram_gb",
                "ram_percent",
                "disk_info_json"
            ])

        writer.writerow(row)
    logging.info("Movement of data to CSV successful")

except Exception as e:
    logging.error(f"Movement of data to CSV failed: {e}")
    raise
