from conn import conn

def __init__(params, render=False):
    params['home_content'] = "This is a home content"

    return params if render is False else render('/fetches/home.html', **params)