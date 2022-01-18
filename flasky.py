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
    


    @route('/')
    def index(self):

        print('test')
        return render_template('index.html')





Flasky.register(app,route_base = '/')
app.register_error_handler(404, page_not_found)
app.logger.removeHandler(default_handler)


if __name__ == "__main__":
  app.run(debug='True', host='0.0.0.0', port=5000)