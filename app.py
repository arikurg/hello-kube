from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World from Kubernetes! 🚀\n'

if __name__ == '__main__':
    # Listen on all available network interfaces
    app.run(host='0.0.0.0', port=5000)