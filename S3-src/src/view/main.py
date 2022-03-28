from flask import Flask, render_template, request, redirect
import tkinter as tk
import os, sys
from werkzeug.utils import secure_filename

p = os.path.abspath('..')
print(p)
print(sys.path.append(p))

from controller.request import *


app = Flask(__name__)

app.config["UPLOADS"] = os.path.join(app.root_path, 'static/uploads')

def archivo_permitido(filename, isPDF=False):
    if not "." in filename:
        return False
    
    ext = filename.rsplit(".", 1)[1]
    
    if isPDF:
        extension_correcta = "pdf"
        if ext.lower() == extension_correcta:
            return True
    else:
        if ext.lower() in ["doc", "docx"]:
            return True
        else:
            return False

def crear_peticion(type, filename, convert_to=None):
    peticion = Request(type, filename, convert_to)
    peticion.realizar_peticion()
    pass

#TODO: controlar la respuesta de la peticion

@app.route('/')
def home():
    return render_template('./Menu-principal.html')

@app.route('/convertir')
def convertir():
    return render_template("./Convertir2.html")

@app.route('/convertir_a_word', methods=['POST'])
def convertir_a_word():
    if request.files:
        file = request.files['pdf']
        if not archivo_permitido(file.filename, isPDF=True):
            print("Este archivo no es un PDF")
            return redirect('/convertir')
            
        else:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config["UPLOADS"], filename))
            print("Archivo subido")
            
    crear_peticion(type=requests.CONVERTIR, filename=filename, convert_to="doc")
    return redirect('/convertir')
    

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