import os
import uuid
from flask import request
from .constants import UPLOAD_FOLDER_PATH

ALLOWED_EXTENSIONS = ['png', 'jpg', 'jpeg', 'gif', 'pdf', 'docx']

def is_allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def upload_file_local():
    file = request.files.get('file')

    if file is None: raise Exception('no file part')
    if file.filename == '': raise Exception('no selected file')

    if is_allowed_file(file.filename) is False:
        raise Exception("file extension must be between ({})"
        .format(", ".join(ALLOWED_EXTENSIONS)))

    fileext = file.filename.rsplit('.', 1)[1].lower()
    new_filename = str(uuid.uuid4()).replace("-","") + f'.{fileext}'
    file_url = '{}/static/uploads/{}'.format(
        os.environ.get("APP_URL"), new_filename)

    file.save(os.path.join(UPLOAD_FOLDER_PATH, new_filename))

    return file_url