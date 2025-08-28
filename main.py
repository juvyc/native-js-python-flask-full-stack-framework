import sys, os
from conn import conn
from flask import Flask, render_template as render, request, redirect, make_response
import glob, hashlib, base64, datetime

#set templates directory
templates = "templates/"
#set useable teplate
use_template = 'basic'

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

#Load all templates parts files
template_parts_path = templates + use_template + '/parts/**'
list_template_parts = {}
for path in glob.glob(template_parts_path, recursive=True):
    if path.endswith(".html"):
        with open(path) as f: 
            #get file content
            fcontent = f.read()
            #remove relative path
            keyn = path.replace(templates + use_template + '/parts\\', '')
            keyn = keyn.replace('\\', '/')
            keyn = base64.b64encode(keyn.encode()).decode().replace('=', '')
            #pass to lists of template parts
            list_template_parts[keyn] = base64.b64encode(fcontent.encode()).decode()

#Load all templates controller files
template_controllers_path = templates + use_template + '/controllers/**'
list_template_controllers = {}
for path in glob.glob(template_controllers_path, recursive=True):
    if path.endswith(".js"):
        with open(path) as f: 
            #get file content
            fcontent = f.read()
            #remove relative path
            keyn = path.replace(templates + use_template + '/controllers\\', '')
            keyn = keyn.replace('\\', '/')
            #pass to lists of controllers
            list_template_controllers[keyn] = fcontent

params = {}

params['template_parts'] = list_template_parts
params['template_controllers'] = list_template_controllers

#Router controller
@app.route("/", methods=['GET', 'POST', 'PUT'])
@app.route("/<slug>", methods=['GET', 'POST', 'PUT'])
@app.route("/<slug>/<slug2>", methods=['GET', 'POST', 'PUT'])
@app.route("/<slug>/<slug2>/<slug3>", methods=['GET', 'POST', 'PUT'])
def route_engine(slug = False, slug2=False, slug3=False):

    params['method'] = request.method

    #Refresh security salt every touches on the server side
    params['security_salt'] = global_security_salt = generate_security_salt()

    #pass the current path to view
    params['current_path'] = request.path
    #Page title
    #params['page_title'] = "Welcome to Student Portal"

    #Require login authenticaiton when accessing login
    if slug == 'admin' and not auth():
        return redirect("/login", code=302)

    #Render dynamic template when request method is PUT
    if request.method == 'PUT' and request.args.get('ft'):
        #get target module name
        modname = request.args.get('ft').replace('/', '.')
        #print(modname)
        #target module
        tmod = __import__(modname, fromlist=['__init__'])
        #run init function of the target module
        tmod.__init__(params)

         #Close database connection
        conn.close()

        #Finally render dynamic templates
        return render('/fetches/' + request.args.get('ft') + '.html',  **params)

    #Close database connection
    conn.close()

    #Render the base view
    return render('/app.html',  **params)


'''
#Login security checker
Implement some codes inside the auth function that validate the user if authenticated or not
it must return True or False only
'''
def auth():
    return False

@app.route("/auth/check", methods=['POST'])
def checkAuth():
    return {
        'status' : auth()
    }


#Start the app
if __name__ == '__main__':
    app.run(debug=True, use_debugger=False, use_reloader=False)