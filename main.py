from flask import Flask, render_template, request
import google.generativeai as genai
import os
import PyPDF2



app = Flask(__name__)

#routes
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/scam/", methods=['GET','POST'])
def detect_scam():
    if "file" not in request.files:
        return render_template("index.html", message="No file uploaded")
    file = request.files['file']
    
    
    extracted_text = ""
    
    
    
    if file.filename.endswith(".pdf"):



if __name__ == "__main__":
    app.run(debug=True)