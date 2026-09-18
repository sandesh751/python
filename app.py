from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello DevOps Bhai! its Practice Time🧠 Level 2 is Live!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
