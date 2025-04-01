from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    # Environment-Label aus Umgebungsvariablen abrufen
    environment_label = os.getenv("ENV_LABEL", "Default Environment")
    return f"<h1>Welcome to {environment_label}!</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
