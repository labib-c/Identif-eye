import os

from flask import Flask, abort, request, render_template
from flask_cors import CORS


URL_PREFIX = "/api/v1.0"
UPLOAD_FOLDER = os.path.basename('uploads')

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def home():
    abort(403)

@app.route('/upload', methods=['POST'])
def upload_image():
    file = request.files['image']
    f = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(f)
    return render_template('/view/index.html')


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8000))
    app.run(host='0.0.0.0', port=port)
    # app.run(debug=True)