from flask import Flask, request, redirect
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <form method="POST">
            <label for="rot">Rotate by:</label>
            <input type="text" name="rot" value="0"><br>
            <textarea name="text">{0}</textarea>
            <input type="submit" value="Submit Query">
        </form>
    </body>
</html>
"""
def verify_int_rot(rot):
    try:
        int(rot)
        return True
    except ValueError:
        return False

@app.route("/", methods=['POST'])
def encrypt():

    rot_by = int(request.form['rot'])
    message = str(request.form['text'])

    encrypted_message = rotate_string(message, rot_by)

    return form.format(encrypted_message)


@app.route("/")
def index():
    return form.format()

app.run()