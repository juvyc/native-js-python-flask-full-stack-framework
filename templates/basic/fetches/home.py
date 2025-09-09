from conn import conn
import utils
from flask import request

def __init__(params, render=False):
    params['home_content'] = "My Home Page"


    if(render is False):
        return params
    else:
        #BELOW CODES IS ONLY FOR RELOADABLE PAGES
        if request.method != 'PUT':
            #Integrate the pre loaded templates to params
            preLoadTmplts = utils.preLoadedControllerTemplates(params)
            params['template_parts'] = preLoadTmplts['list_template_parts']
            params['template_controllers'] = preLoadTmplts['list_template_controllers']

        #Finally render the full template
        return render('/parts/home.html', **params)