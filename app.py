from flask import Flask, render_template, request, redirect, url_for, send_from_directory, flash
from werkzeug.utils import secure_filename
import os
from PIL import Image
from stegano import lsb

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encode', methods=['GET', 'POST'])
def encode():
    if request.method == 'POST':
        image = request.files['image']
        message = request.form['message']
        password = request.form['password']

        if image and message and password:
            filename = secure_filename(image.filename)
            input_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            image.save(input_path)

            secret_message = f"{password}::{message}"
            encoded_image = lsb.hide(input_path, secret_message)
            output_path = os.path.join(app.config['UPLOAD_FOLDER'], 'encoded_' + filename)
            encoded_image.save(output_path)

            flash('Message successfully encoded into image!', 'success')
            return render_template('result.html', filename='encoded_' + filename)
        else:
            flash('Missing image, message, or password!', 'danger')
            return redirect(url_for('encode'))
    return render_template('encode.html')

@app.route('/decode', methods=['GET', 'POST'])
def decode():
    if request.method == 'POST':
        image = request.files['image']
        password = request.form['password']

        if image and password:
            filename = secure_filename(image.filename)
            input_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            image.save(input_path)

            try:
                hidden_message = lsb.reveal(input_path)
                if hidden_message:
                    stored_password, message = hidden_message.split('::', 1)
                    if password == stored_password:
                        flash('Message successfully decoded!', 'success')
                        return render_template('decode.html', decoded_message=message)
                    else:
                        flash('Incorrect password!', 'danger')
                else:
                    flash('No hidden message found!', 'warning')
            except Exception as e:
                flash('Error decoding image!', 'danger')

        else:
            flash('Image and password required!', 'danger')
        return redirect(url_for('decode'))
    return render_template('decode.html')

@app.route('/download/<filename>')
def download(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)
