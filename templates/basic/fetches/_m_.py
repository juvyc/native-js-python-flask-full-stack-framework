from conn import conn

def __init__(params, render=False):
    params['content'] = "This is a dynamic pages"

    #Close database connection
    conn.close()
    return params if render is False else render('/fetches/page.html', **params)