from flask import Flask, render_template as render, request
import glob

#set useable teplate
use_template = 'basic'

#Initialize the app using flask framework
app = Flask(__name__, 
    template_folder="templates/" + use_template, #keep the folder secret
    static_folder='templates/' + use_template + '/assets' #keep the assets secret
)

#Load all templates parts files
template_parts_path = 'templates/' + use_template + '/parts/**'
list_template_parts = {}
for path in glob.glob(template_parts_path, recursive=True):
    if path.endswith(".html"):
        with open(path) as f: 
            #get file content
            fcontent = f.read()
            #remove relative path
            keyn = path.replace('templates/' + use_template + '/parts\\', '')
            keyn = keyn.replace('\\', '/')
            #pass to lists of template parts
            list_template_parts[keyn] = fcontent

#Load all templates controller files
template_controllers_path = 'templates/' + use_template + '/controllers/**'
list_template_controllers = {}
for path in glob.glob(template_controllers_path, recursive=True):
    if path.endswith(".js"):
        with open(path) as f: 
            #get file content
            fcontent = f.read()
            #remove relative path
            keyn = path.replace('templates/' + use_template + '/controllers\\', '')
            keyn = keyn.replace('\\', '/')
            #pass to lists of controllers
            list_template_controllers[keyn] = fcontent

params = {}

params['template_parts'] = list_template_parts
params['template_controllers'] = list_template_controllers

#FrontEnd controller
@app.route("/")
@app.route("/<slug>")
@app.route("/<slug>/<slug2>")
@app.route("/<slug>/<slug2>/<slug3>")
def route_engine(slug = False, slug2=False, slug3=False):
    #pass the current path to view
    params['current_path'] = request.path
    #Page title
    params['page_title'] = "Student Portal"
    #Render the base view
    return render('/app.html',  **params)

#Start the app
if __name__ == '__main__':
    app.run(debug=True, use_debugger=False, use_reloader=False)