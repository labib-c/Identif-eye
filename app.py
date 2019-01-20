import os

from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# UPLOAD_FOLDER = os.path.basename('uploads')
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")
def hello_world():
	return render_template("index.html")


@app.route("/uploads", methods=["POST"])
def upload_image():
	
	imagefile = request.files.get('imagefile', '')

	print(imagefile)
	f = os.path.join(os.getcwd(), imagefile.filename)

	return redirect("/", code=302)


# @app.route('/upload', methods=['POST'])
# def upload_image(req, res):
# 	print("hit")
	# file = req.files['image']
	# f = os.path.join(os.getcwd(), file.filename)
	# file.save(f)
	# return redirect("/", code=302)