from flask import Flask, request
import os
from datetime import datetime

# Create Flask app
app = Flask(__name__)

# Folder to save uploaded files
UPLOAD_DIR = "received_metrics"

# Ensure folder exists
os.makedirs(UPLOAD_DIR, exist_ok=True)

# API endpoint to receive files
@app.route("/upload_metrics", methods=["POST"])
def upload_metrics():
    try:
        # Get server name from form data
        server_name = request.form.get('server_name')
        if not server_name:
            return "Server name missing", 400

        # Get uploaded file
        if 'file' not in request.files:
            return "No file part", 400

        file = request.files['file']
        if file.filename == "":
            return "No selected file", 400

        # Save file with server name and timestamp
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"{server_name}_{timestamp}_{file.filename}"
        save_path = os.path.join(UPLOAD_DIR, filename)
        file.save(save_path)

        return f"File received and saved as {filename}", 200

    except Exception as e:
        return f"Error: {str(e)}", 500

# Run the server continuously
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
