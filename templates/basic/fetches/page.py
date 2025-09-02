def __init__(params, render=False):
    params['content'] = "My page dynamic content"
    
    return params if render is False else render('/fetches/page.html', **params)