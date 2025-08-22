from flask import Flask, request, jsonify

app = Flask(__name__)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/add")
def add():
    a = int(request.args.get("a", "0"))
    b = int(request.args.get("b", "0"))
    return {"sum": a + b}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
