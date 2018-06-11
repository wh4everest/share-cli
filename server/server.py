import os
import string
import random

from flask import Flask, request, send_from_directory
from werkzeug.utils import secure_filename

app = Flask(__name__)

URL = os.environ['SHARE_CLI_URL']
app.config['UPLOAD_FOLDER'] = '/tmp/share-cli-uploads'

def gen_safe_filename(filename):
    chars = string.ascii_lowercase + string.ascii_uppercase + string.digits
    prefix = ''.join(random.SystemRandom().choice(chars) for _ in xrange(10))
    filename = secure_filename(filename)
    return prefix + '-' + filename

@app.route("/", methods=['POST'])
def upload():
    file = request.files['file']
    filename = gen_safe_filename(file.filename)
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return URL + filename + '\n'

@app.route("/<filename>")
def download(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)