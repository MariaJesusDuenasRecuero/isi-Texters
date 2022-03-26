from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("./Menu-principal.html")

@app.route('/convertir')
def convertir():
    return render_template("./Convertir.html")

@app.route('/escanear')
def escanear():
    return render_template("./Escanear.html")

@app.route('/resumir')
def resumir():
    return render_template("./Resumir.html")

@app.route('/unir')
def unir():
    return render_template("./Unir.html")

@app.route('/about')
def about():
    return render_template("./Sobre-nosotros.html")

@app.route('/signin')
def signin():
    return render_template("./Inicio-de-sesion.html")
    
    
if __name__ == '__main__':
    app.run(debug=True)