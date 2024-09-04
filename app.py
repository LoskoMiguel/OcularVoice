from flask import Flask, render_template, request
import pytesseract
from PIL import Image
import pyttsx3
from googletrans import Translator

app = Flask(__name__)

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract"
translator = Translator()

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/texto', methods=['GET', 'POST'])
def texto():
    if request.method == 'POST':
        acceder = request.files.get("entrada_text")

        imagen = Image.open(acceder)

        pasar_texto = pytesseract.image_to_string(imagen).replace("\n", " ")
        return render_template('texto.html', texto=pasar_texto)
    return render_template('texto.html', texto="")

@app.route('/voz', methods=['GET', 'POST'])
def voz():
    if request.method == 'POST':
        acceder = request.files.get("entrada_voz")

        imagen = Image.open(acceder)

        pasar_texto = pytesseract.image_to_string(imagen).replace("\n", " ")

        print(pasar_texto)

        engine = pyttsx3.init()
        engine.setProperty("rate", 130)
        engine.say(pasar_texto)
        engine.runAndWait()
    return render_template('voz.html')

@app.route('/texto_voz', methods=['GET', 'POST'])
def texto_voz():
    if request.method == 'POST':
        acceder = request.files.get("entrada_text_voz")

        imagen = Image.open(acceder)

        pasar_texto = pytesseract.image_to_string(imagen).replace("\n", " ")

        print(pasar_texto)

        engine = pyttsx3.init()
        engine.setProperty("rate", 130)
        engine.say(pasar_texto)
        engine.runAndWait()
        return render_template('texto_voz.html', texto=pasar_texto)
    return render_template('texto_voz.html', texto="")

@app.route('/traduccion', methods=['GET', 'POST'])
def traduccion():
    if request.method == 'POST':
        acceder = request.files.get("entrada_traduccion")
        imagen = Image.open(acceder)
        pasar_texto = pytesseract.image_to_string(imagen).replace("\n", " ")

        traducido = translator.translate(pasar_texto, src='en', dest='es').text

        return render_template('traduccion_ingles.html', original=pasar_texto, traducido=traducido)
    return render_template('traduccion_ingles.html', original="", traducido="")

if __name__ == "__main__":
    app.run(debug=False)
