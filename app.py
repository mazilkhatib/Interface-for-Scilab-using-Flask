from flask import Flask, render_template, request, redirect, url_for
import scilab2py
import numpy as np
from scilab2py import Scilab2Py
import random
import string
import io
from contextlib import redirect_stdout

sci = Scilab2Py()

app = Flask(__name__)


def randomName(Length=8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(Length))


@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == "POST":
        # accessing Scilab Function
        exec((request.form['command']))
        filename = 'plot_{}.png'.format(randomName())
        y = 'static/Plot_Images/' + filename
        sci.xs2png(0, y)
        sci.close()
        plot_done = True
        return render_template("index.html", filename='Plot_Images/' + filename, dimension="[1, 2, 3], '-o'",
                               plot_done=plot_done)
    else:
        return render_template("index.html")


@app.route('/threed', methods=["GET", "POST"])
def threed():
    if request.method == "POST":
        # accessing Scilab Function
        exec(request.form['command'])
        filename = 'plot_{}.png'.format(randomName())
        y = 'static/Plot_Images/' + filename
        sci.xs2png(0, y)
        sci.close()
        plot_done = True
        return render_template("threed.html", filename='Plot_Images/' + filename,
                               dimension=request.form['command'],
                               plot_done=plot_done)
    else:
        return render_template("threed.html")


@app.route('/commands', methods=["GET", "POST"])
def commands():
    if request.method == "POST":
        x = request.form['command']
        func_str = x
        stdout = io.StringIO()

        with redirect_stdout(stdout):
            exec(func_str)

        out = stdout.getvalue()
        command_exe = True
        return render_template("commands.html",x=x, out=out, command_exe=command_exe)
    else:
        return render_template("commands.html")


if __name__ == '__main__':
    app.run(debug=True)
