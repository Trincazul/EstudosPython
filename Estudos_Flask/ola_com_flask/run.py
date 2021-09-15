from flask import Flask

app = Flask(__name__)

@app.route('/<numero>', methods=['GET', 'POST']) 

def ola(numero):
    return 'ola mundo, você selecionou o numero {}'.format(numero)

if __name__ == "__main__":
    app.run(debug=True)

