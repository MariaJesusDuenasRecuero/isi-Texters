from crypt import methods
from importlib.metadata import files
from flask import Flask, render_template, request, redirect, send_from_directory
import os, sys
from werkzeug.utils import secure_filename

p = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
print(p)
print(sys.path.append(p))

from controller.request import *


app = Flask(__name__)

app.config["UPLOADS"] = os.path.join(app.root_path, 'static/uploads')
app.config["DOWNLOADS"] = os.path.join(app.root_path, 'static/downloads')

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

def hacer_peticion(type, files, convert_to=None):
    peticion = Request(type, files, convert_to)
    respuesta = peticion.realizar_peticion()
    
    if  type!= requests.RESUMIR:
        download_folder = app.config["DOWNLOADS"]
        respuesta.save_files(download_folder)
        print("Archivo guardado en la carpeta: " + download_folder)

   


# def get_file(filename):
#     return send_from_directory(app.config["DOWNLOADS"], filename)

#

def subir_archivo(file):
    filename = secure_filename(file.filename)
    file_path = os.path.join(app.config["UPLOADS"], filename) 
    file.save(file_path)
    print("Archivo subido")
    
    return file_path


@app.route('/')
def home():
    return render_template('./Menu-principal.html')

@app.route('/convertir')
def convertir():
    return render_template("./Convertir2.html")

@app.route('/convertir_a_word', methods=['POST'])
def convertir_a_word():
    if request.files:
        file = request.files['file']
        if not archivo_permitido(file.filename, isPDF=True):
            print("Este archivo no es un PDF")
            return redirect('/convertir')
            
        else:
            file_path = subir_archivo(file)
            
    hacer_peticion(type=requests.CONVERTIR, files=file_path, convert_to="doc")
    # get_file(filename)
    return redirect('/convertir')

@app.route('/convertir_a_pdf', methods=['POST'])
def convertir_a_pdf():
    if request.files:
        file = request.files['file']
        if file.filename == "":
            print("El archivo no tiene nombre")
            return redirect('/convertir')
        if not archivo_permitido(file.filename):
            print("Este archivo no es un documento WORD")
            return redirect('/convertir')
            
        else:
            file_path = subir_archivo(file)
            
    hacer_peticion(type=requests.CONVERTIR, files=file_path, convert_to="pdf")
    render_template("./loader.html")
    return redirect('/convertir')
    

@app.route('/escanear', methods=['GET','POST'])
def escanear():
    if request.method == 'POST':
        if request.files:
            file = request.files['file']
            if file.filename == '':
                print("El archivo no tiene nombre,")
                return redirect('/escanear')
            
            if not archivo_permitido(file.filename, isPDF=True):
                print("Este archivo no es un PDF")
                return redirect('/escanear')
            
            else:
                file_path = subir_archivo(file)
                hacer_peticion(type=requests.ESCANEAR, files=file_path)
                return redirect('/escanear')
    elif request.method == 'GET':
        return render_template("./Escanear.html")

@app.route('/resumir', methods=['GET', 'POST'])
def resumir():
    if request.method == 'POST':
        file = request.files['file']
        file_path = subir_archivo(file)
        hacer_peticion(type=requests.RESUMIR, files=file_path)
        return redirect("/resumir")
    elif request.method == 'GET':
        return render_template("./Resumir.html")


@app.route('/unir', methods=['GET','POST'])
def unir():
    if request.method == 'POST':
        if request.files:
            files = request.files.getlist('file')
            file_paths = []
            for file in files:
                if file.filename == '':
                    print("El archivo no tiene nombre")
                    return redirect('/unir')
                
                if not archivo_permitido(file.filename, isPDF=True):
                    print(f"{file.filename} no es un archivo PDF")
                    return redirect('/unir')
                
                else:
                    file_path = subir_archivo(file)
                    file_paths.append(file_path)
            
            hacer_peticion(type=requests.UNIR, files=file_paths)
            
            return redirect('/unir')
    
    elif request.method == 'GET':
        return render_template("./Unir.html")

@app.route('/ocr')
def ocr():
    return render_template("./Escanear.html")

@app.route('/about')
def about():
    return render_template("./Sobre-nosotros.html")

@app.route('/signin')
def signin():
    return render_template("./Inicio-de-sesion.html")  
    
if __name__ == '__main__':
    app.run(debug=True)