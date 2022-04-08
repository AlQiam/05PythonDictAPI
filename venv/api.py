import justpy as jp
from definition import Definition
import json


class Api:
    """Handles requests at /api?w=word"""
    @classmethod
    def serve(cls, req):
        wp = jp.WebPage()
        word = req.query_params.get('w')
        jp.Div(a=wp, text=word.title())

        defined = Definition(word).get()
        response = {
            'word': word,
            'definition': defined

        }
        wp.html = json.dumps(response)

        return wp
