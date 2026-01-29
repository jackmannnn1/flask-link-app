from flask import Flask, render_template_string
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template_string("""
<!DOCTYPE html>
<html>
<head>
    <meta http-equiv="refresh" content="0.5">
    <style>
        body {
            background: black;
            color: red;
            font-size: 48px;
            text-align: center;
            margin-top: 20%;
            animation: blink 0.2s infinite;
            font-family: Arial, sans-serif;
        }

        @keyframes blink {
            0% { opacity: 1; }
            50% { opacity: 0; }
            100% { opacity: 1; }
        }
    </style>
</head>
<body>
    ⚠️ KRITIKUS HIBA TÖRTÉNT ⚠️
</body>
</html>
""")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
