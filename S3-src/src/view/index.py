from flask import Flask, render_template, request
import tkinter as tk
from tkinter import filedialog
import os

app = Flask(__name__)

app.config["UPLOADS"] = ""

@app.route('/')
def home():
    return render_template("./Menu-principal.html")

@app.route('/convertir', methods=['GET', 'POST'])
def convertir():
    if request.method=='POST':
        if request.files:
            file = request.files['pdf']

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

def pdf_to_word():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfile()
    
    
if __name__ == '__main__':
    app.run(debug=True)