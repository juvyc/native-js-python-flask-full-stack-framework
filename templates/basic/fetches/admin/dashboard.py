from flask import request
import auth

def __init__(params, render=False):
    #JS Checker method if current user is logged-in
    if request.method == 'PATCH':
        return auth.exec()
    #Finally render the complete output
    return "Testing"