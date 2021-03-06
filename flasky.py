from flask import Flask, render_template, Markup, request, url_for, redirect, render_template_string
import sys
from flask_classful import FlaskView, route
from flask.logging import default_handler
from flask_assets import Environment, Bundle
import os
import pretty_errors
from werkzeug.exceptions import HTTPException, NotFound



sys.path.append('/')

app = Flask(__name__, template_folder='templates', static_folder='static')
assets = Environment(app)
cssbundle = Bundle('styles/SCSS/styles.scss', filters='pyscss', output='styles/CSS/styles.css')
assets.register('scss_all', cssbundle)


def page_not_found(e):
    return render_template('404.html'), 404     # error handler




class Flasky(FlaskView):
    def __init__(self):
        self.version = 'v1.0.5'
        self.latest_update = '18/03/22'




    @route('/')
    def index(self):
        varaboutsite = f'Version {self.version} Latest Update {self.latest_update}'
        return render_template('index.html', aboutsite=varaboutsite)




    @route('/', methods=['POST'])
    def index_post(self):
        print('test')
        if request.method == 'POST':
            cmdinput1 = request.form['cmdinput']
            if cmdinput1 == '-help':
                print('Wow it really worked?')
            return render_template('upindex.html',)
        else:
            print("What did you expect?")
            return render_template('index.html',)

        return render_template('index.html',)


    @route('/business')
    def business_page(self):
        return render_template('business.html')

    @route('/pass')
    def prodbusiness(self):
        return render_template('pass.html')


Flasky.register(app,route_base = '/')
app.register_error_handler(404, page_not_found)
app.logger.removeHandler(default_handler)


if __name__ == "__main__":
  app.run(debug='True', host='0.0.0.0', port=5000)
