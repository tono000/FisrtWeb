from flask import current_app

def add_to_index(index, model):
    if not current_app.elasticsearch:
        return
    payload = {}

