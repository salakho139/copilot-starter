from flask import Flask
import time

app = Flask(__name__)

def seconds_since_epoch():
    epoch = time.time()
    return int(epoch)

@app.route("/")
def seconds():
    return str(seconds_since_epoch())

if __name__ == "__main__":
    app.run(debug=True)

