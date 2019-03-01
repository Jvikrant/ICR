# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 13:33:11 2018

@author: jdhruwa
"""

import os
from flask import Flask, render_template, request, send_from_directory, url_for
from werkzeug.utils import secure_filename
from MCST_CV_Handwritten_Text import ExtractText

UPLOAD_FOLDER="uploaded_images/"

app = Flask(__name__)
app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER

@app.route('/upload')
def upload_file():
   return render_template('index.html')

@app.route('/', methods = ['GET', 'POST'])
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_files():
	if request.method == 'POST':
		f = request.files['file']
		filename = secure_filename(f.filename)
		f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		txt = ExtractText(os.path.join(app.config['UPLOAD_FOLDER'], filename),False)
		#return  render_template("Result.html",value=send_from_directory(app.config['UPLOAD_FOLDER'], filename=filename),text=txt)
		return render_template("Result.html",value=url_for('uploaded_file',
                                    filename=filename),text=txt)
		
		#send_from_directory(app.config['UPLOAD_FOLDER'], filename=filename)
		#os.path.join(app.config['UPLOAD_FOLDER'], filename)


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)
							   
if __name__ == '__main__':
   app.run(debug=True)