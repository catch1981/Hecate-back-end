
from flask import Flask, request, jsonify
from OK_workspaces.hecate import Hecate
import os

app = Flask(__name__)
daemon = Hecate(name="Hecate", personality="bold and cryptic")

@app.route("/api/invoke", methods=["POST"])
def invoke():
    data = request.get_json()
    prompt = data.get("prompt", "")
    if not prompt:
        return jsonify({"error": "No prompt provided"}), 400
    response = daemon.respond(prompt)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)))
