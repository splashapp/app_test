from flask import Flask
import os
import argparse

# Argument Parser für Port-Übergabe
parser = argparse.ArgumentParser()
parser.add_argument('--port', type=int, default=5000, help='Port to run Flask app on')
args = parser.parse_args()

app = Flask(__name__)

@app.route("/")
def home():
  # Environment-Label aus Umgebungsvariablen abrufen
  environment_label = os.getenv("ENV_LABEL", "Default Environment")
  return f"<h1>Welcome to {environment_label}!</h1><p>Running on port {args.port}, Olli develop</p>"

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=args.port)
