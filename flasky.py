from flask import Flask, render_template, Markup, request, url_for, redirect
import sys
from flask_classful import FlaskView, route
from flask.logging import default_handler
import os


sys.path.append('/')

app = Flask(__name__, template_folder='templates', static_folder='static')

def page_not_found(e):
  return render_template('404.html'), 404     # error handler


class Flasky(FlaskView):
    def __init__(self):
        self.version = 'v1.0.0'
        self.latest_update = '18/01/22'

    
    @route('/')
    def index(self):

        print('test')
        return render_template('index.html')




    @route('/', methods=['GET', 'POST'])
    def index_post(self):
        print('test')
        cmdinput1 = request.form.get['cmdinput']
        process_cmdinput = cmdinput1.upper()
        print(process_cmdinput)
        if process_cmdinput == '-help':
            print('Wow it really worked?')
        else:
            print("What did you expect?")

        return render_template('index.html')



Flasky.register(app,route_base = '/')
app.register_error_handler(404, page_not_found)
app.logger.removeHandler(default_handler)


if __name__ == "__main__":
  app.run(debug='True', host='0.0.0.0', port=5000)