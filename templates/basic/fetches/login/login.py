def __init__(params, render=False):
    params['content'] = "This is my login information"

    return params

    #Finally render dynamic templates
    #return render('/fetches/' + request.args.get('ft') + '.html',  **params)