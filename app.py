from flask import Flask

app = Flask(__name__)

@app.route("/")
def run_program():
    print("A PROGRAM LEFUTOTT!")
    return "<h1>Szia! A program lefutott 🚀</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)