import requests
import socket
import os
import logging



#Logging Setup
logging.basicConfig(
    filename="Logs/automation.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logging.info("API script started")



try:
    server_name = socket.gethostname()
    file_path = "metrics/server_metrics.csv"

    url = "http://192.168.178.59:5000/upload_metrics"

    with open(file_path, 'rb') as f:
        files = {'file': (os.path.basename(file_path), f)}
        data = {'server_name': server_name}
        response = requests.post(url, files=files, data=data)

    os.remove(file_path)
    logging.info("API request successfull\n")

except Exception as e:
    logging.error(f"API request failed: {e}\n")
    raise