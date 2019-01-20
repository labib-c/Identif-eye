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
	print(request.content)
	return redirect("/", code=302)


	# file = request.files['file']
	# filename = secure_filename(file.filename)
	# file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
	# return redirect(url_for('uploaded_file', filename=filename))


# @app.route('/upload', methods=['POST'])
# def upload_image(req, res):
# 	print("hit")
	# file = req.files['image']
	# f = os.path.join(os.getcwd(), file.filename)
	# file.save(f)
	# return redirect("/", code=302)