import glob
from flask import render_template_string
from main import templates, use_template
import base64

#Initialize all preloaded template parts and controllers
def preLoadedControllerTemplates(params={}):
    #Pass preload to template engine
    other_params = {"preLoad": True}

    #Load all templates parts files
    template_parts_path = templates + use_template + '/parts/**'
    list_template_parts = {}
    for path in glob.glob(template_parts_path, recursive=True):
        if path.endswith(".html"):
            with open(path) as f:
                fcontent = f.read()
                keyn = path.replace(templates + use_template + '/parts\\', '')
                keyn = keyn.replace('\\', '/')
                #Get file content
                fcontent = render_template_string(fcontent, **params, **other_params)
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
    return {"list_template_parts" : list_template_parts, "list_template_controllers" : list_template_controllers}