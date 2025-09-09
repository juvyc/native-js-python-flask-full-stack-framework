import sys, os
from conn import conn
from flask import Flask, render_template as render, request, redirect
import hashlib, base64, datetime

#set templates directory
templates = "templates/"
#set useable teplate
use_template = 'awonsa'

#Integrating fetches modules
sys.path.append(os.path.join(os.path.dirname(__file__), templates + use_template + '/fetches/'))

#from login.login import __init__
#print(__init__({}))
#print('Test')

#mn = 'login.login';
#tmod = __import__(mn, fromlist=['__init__'])
#print(tmod.__init__({}))

#global variable
global_security_salt = False

#security salt generator
def generate_security_salt():
    dt = str(datetime.datetime.now())
    security_salt = hashlib.shake_256(dt.encode())
    security_salt = security_salt.hexdigest(40).encode()
    return base64.b64encode(security_salt).decode().replace('=', '')

#Initialize the app using flask framework
app = Flask(__name__,
    template_folder=templates + use_template, #keep the folder secret
    static_folder=templates + use_template + '/assets' #keep the assets secret
)

params = {}

#params['template_parts'] = list_template_parts
#params['template_controllers'] = list_template_controllers

#Router controller
@app.route("/", methods=['GET', 'POST', 'PUT', 'PATCH'])
@app.route("/<slug>", methods=['GET', 'POST', 'PUT', 'PATCH'])
@app.route("/<slug>/<slug2>", methods=['GET', 'POST', 'PUT', 'PATCH'])
@app.route("/<slug>/<slug2>/<slug3>", methods=['GET', 'POST', 'PUT', 'PATCH'])
@app.route("/<slug>/<slug2>/<slug3>/<slug4>", methods=['GET', 'POST', 'PUT', 'PATCH'])
def route_engine(**kwargs):
    args = {**locals()}
    params['args'] = args

    slugs = []
    if len(args['kwargs'].keys()) > 0:
        slugs = list(args['kwargs'].values())
    else:
        slugs.append('home')


    params['method'] = request.method

    #Refresh security salt every touches on the server side
    params['security_salt'] = global_security_salt = generate_security_salt()

    #pass the current path to view
    params['current_path'] = request.path
    #Page title
    #params['page_title'] = "Welcome to Student Portal"

    #Render dynamic template when request method is PUT
    if len(slugs) > 0:
        #print('.'.join(slugs))
        modname = '.'.join(slugs)

        #print(modname);
        try:
            #Pass exeception as the test is a built in module of the python
            if modname.lower() == 'test':
                raise Exception("Python reserve term!")

            tmod = __import__(modname, fromlist=['__init__'])
            return tmod.__init__(params, render)
        except ModuleNotFoundError:
            try:
                tmod = __import__("_m_", fromlist=['__init__'])
                fret = tmod.__init__(params, render)

                if fret is not None:
                    return fret
                else:
                    raise Exception("Not found")
            except:
                return render('/404.html'), 404
        except:
            return render('/404.html'), 404

#Start the app
if __name__ == '__main__':
    app.run(debug=True)