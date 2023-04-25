
""" import sys
sys.path.append('/home/project/xzceb-flask_eng_fr/final_project/machinetranslation/') """
""" from machinetranslation.translator import englishToFrench, frenchToEnglish """
print("1234")
from machinetranslation import translator
print("1234")
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def translateToFrench():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    translatedText = translator.englishToFrench(textToTranslate)
    return translatedText

@app.route("/frenchToEnglish")
def translateToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    translatedText = translator.frenchToEnglish(textToTranslate)
    return translatedText

@app.route("/")
def renderIndexPage():
    # Write the code to render template
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
    print('The app is running smoothly')
