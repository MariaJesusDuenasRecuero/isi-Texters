from flask import Flask, current_app, flash, render_template, request, redirect, send_from_directory, url_for
from flask import session
import os, sys
from werkzeug.utils import secure_filename
import hashlib
from dotenv import load_dotenv

p = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(p)

from controller.request import *
from controller.user import User

load_dotenv()
app = Flask(__name__)

app.secret_key = os.getenv("SECRET_FLASK_KEY")
app.config["UPLOADS"] = os.path.join(app.root_path, 'static/uploads')
app.config["DOWNLOADS"] = os.path.join(app.root_path, 'static/downloads')
    
    
def authorized_user(user):
    if user is None:
        return False
    else:
        if user["subscribed"].lower() == "true":
            return True
        else:
            return False

def get_session_user():
    if "user" in session:
        return session["user"]
    else:
        return None

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
    if peticion.request != requests.OCR:
        if peticion.request == requests.RESUMIR:
            summarized_text = respuesta["summary"]
            filename = os.path.basename(files) + "_resumido.txt"
            with open(os.path.join(app.config["DOWNLOADS"], filename), "w") as f:
                f.write(summarized_text)
        
        else:
            download_folder = app.config["DOWNLOADS"]
            respuesta.save_files(download_folder)
            print("Archivo guardado en la carpeta: " + download_folder)
            
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
    return render_template("./Convertir.html")

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
    if not authorized_user(get_session_user()):
        error_message = 'Esta funcionalidad es solo para usuarios suscritos'
        flash(error_message)
        return redirect('/')
    
    if request.method == 'POST':
        if request.files:
            file = request.files['file']
            if file.filename == '':
                print("El archivo no tiene nombre,")
                return redirect('/resumir')
            
            if not archivo_permitido(file.filename, isPDF=True):
                print("Este archivo no es un PDF")
                return redirect('/resumir')
            
            else:
                file_path = subir_archivo(file)
                hacer_peticion(type=requests.RESUMIR, files=file_path)
                return redirect('/resumir')
            
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


@app.route('/ocr', methods=['GET','POST'])
def ocr():
    if not authorized_user(get_session_user()):
        error_message = 'Esta funcionalidad es solo para usuarios suscritos'
        flash(error_message)
        return redirect('/')
    
    if request.method == 'POST':
        if request.files:
            file = request.files['file']
            if file.filename == '':
                print("El archivo no tiene nombre,")
                return redirect('/ocr')
            
            if not archivo_permitido(file.filename, isPDF=True):
                print("Este archivo no es un PDF")
                return redirect('/ocr')
            
            else:
                file_path = subir_archivo(file)
                hacer_peticion(type=requests.OCR, files=file_path)
                return redirect('/ocr')
    elif request.method == 'GET':
        return render_template("./Ocr.html")


@app.route('/about')
def about():
    return render_template("./Sobre-nosotros.html")


@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        password_hash = hashlib.sha256(password.encode()).hexdigest()

        user = User(email, password_hash)
        try:
            user.read_user()
            session['user'] = user.serialize()
            return redirect(url_for('home'))
        except Exception as e:
            error_message = e.__str__()
            flash(error_message)
            return render_template("./Inicio-de-sesion.html")
    elif request.method == 'GET':
        return render_template("./Inicio-de-sesion.html")  

#@app.route('/signup', methods=['GET', 'POST'])
#def signup():
#    if request.method == 'POST':
#        pass
#    elif request.method == 'GET':
#        pass
#        return render_template('./signup.html')
    
@app.route('/logout')
def logout():
    if 'user' in session:
        session.pop('user')
    return redirect('/')

    
@app.errorhandler(404)
def not_found(error):
    return "<h1>404</h1><p>Pagina no encontrada</p>", 404


if __name__ == '__main__':
    app.run(debug=True)
    