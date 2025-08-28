from conn import conn

def __init__(params):
    params['home_content'] = "This is a home content"

    #Close database connection
    conn.close()