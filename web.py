import os
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash


app = Flask(__name__)
 

@app.route('/')
def index():
    return render_template('index.html')


  
@app.route('/result', methods=['POST'])
def show():
	urlLists=request.form['url'].splitlines()

	return render_template('show.html',urlLists=urlLists)

if __name__ == "__main__":
    app.run()