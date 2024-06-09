from flask import Flask

app = Flask(__name__)

@app.route('/')

def hoome():
    return '<h1>Python Server on Docker Environment</h1>'

if __name__ == '__main__':
    app.run(debug = True,port=8081)
    