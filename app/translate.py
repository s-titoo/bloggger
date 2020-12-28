import json
import requests
from flask_babel import _
from app import app

def translate(text, source_language, dest_language):

    endpoint = 'https://api.cognitive.microsofttranslator.com'
    path = '/translate?api-version=3.0'
    params = '&from={}&to={}'.format(source_language, dest_language)
    url_to_pass = endpoint + path + params


    # add 'Ocp-Apim-Subscription-Region': 'westeurope'
    # if for your resource you chose region other than Global
    
    headers = {
    'Content-type': 'application/json',
    'Content-Length': '10000',
    # 'Ocp-Apim-Subscription-Region': 'westeurope'
    }

    body = [{
    'text' : text
    }]

    if 'MS_TRANSLATOR_KEY' not in app.config or \
    not app.config['MS_TRANSLATOR_KEY']:
        return _('Error: the translation service is not configured.')
    headers['Ocp-Apim-Subscription-Key'] = app.config['MS_TRANSLATOR_KEY']

    r = requests.post(url_to_pass, headers=headers, json=body)

    # return r.status_code, headers

    if r.status_code != 200:
        return _('Error: the translation service failed.')
    parsed_json = json.loads(r.content.decode('utf-8-sig'))
    translated_text = parsed_json[0]['translations'][0]['text']
    return translated_text

