from flask import Flask, json, jsonify, request, redirect
import string
from datetime import datetime
from random import choices

app = Flask(__name__)

dict = {}

# generate a short url hash
def generate_short_link():
    characters = string.digits + string.ascii_letters
    short_url_hash = ''.join(choices(characters, k=7))

    if short_url_hash in dict:
        return generate_short_link()
    else:
        return short_url_hash

# Shorten a Link
@app.route('/v4/shorten', methods=['POST'])
def shorten_url():
    content = request.json
    original_url = content['long_url']
    domain = content['domain']

    short_url_hash = generate_short_link()

    dict[short_url_hash] = {}
    dict[short_url_hash]['original_url'] = original_url
    dict[short_url_hash]['domain'] = domain
    dict[short_url_hash]['short_url'] = domain + "/" + short_url_hash
    dict[short_url_hash]['visits'] = 0
    dict[short_url_hash]['date_created'] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    dict[short_url_hash]['title'] = ''

    bitlink = dict.get(short_url_hash, {}).get('short_url')
    created_at = dict.get(short_url_hash, {}).get('date_created')

    return jsonify({"link": bitlink, 
                    "long_url": original_url, 
                    "created_at": created_at
                    })

# Create a Bitlink
@app.route('/v4/bitlinks', methods=['POST'])
def create_bitlink():
    content = request.json
    original_url = content['long_url']
    domain = content['domain']
    title = content['title']

    short_url_hash = generate_short_link()

    dict[short_url_hash] = {}
    dict[short_url_hash]['original_url'] = original_url
    dict[short_url_hash]['domain'] = domain
    dict[short_url_hash]['short_url'] = domain + "/" + short_url_hash
    dict[short_url_hash]['visits'] = 0
    dict[short_url_hash]['date_created'] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    dict[short_url_hash]['title'] = title

    bitlink = dict.get(short_url_hash, {}).get('short_url')
    created_at = dict.get(short_url_hash, {}).get('date_created')

    return jsonify({"link": bitlink,
                    "long_url": original_url, 
                    "title": title, 
                    "created_at": created_at
                    })

# Update a Bitlink
@app.route('/v4/bitlinks/<domain>/<code>', methods=['PATCH'])
def update_bitlink(domain, code):
    content = request.json
    long_url = content['long_url']
    title = content['title']

    dict[code]['title'] = title
    dict[code]['original_url'] = long_url

    bitlink = dict.get(code, {}).get('short_url')
    created_at = dict.get(code, {}).get('date_created')
    original_url = dict.get(code, {}).get('original_url')
    title = dict.get(code, {}).get('title')
    return jsonify({"link": bitlink,
                    "long_url": original_url, 
                    "title": title, 
                    "created_at": created_at
                    })

# Retrieve a Bitlink
@app.route('/v4/bitlinks/<domain>/<code>')
def get_bitlink(domain, code):
    bitlink = dict.get(code, {}).get('short_url')
    created_at = dict.get(code, {}).get('date_created')
    original_url = dict.get(code, {}).get('original_url')
    title = dict.get(code, {}).get('title')
    return jsonify({"link": bitlink,
                    "long_url": original_url, 
                    "title": title, 
                    "created_at": created_at
                    })

# Get Clicks for a Bitlink
@app.route('/v4/bitlinks/<domain>/<code>/clicks')
def getClicks(domain, code):
    visits = dict.get(code, {}).get('visits')
    created_at = dict.get(code, {}).get('date_created')
    return jsonify({"clicks": visits, 
                    "created_at": created_at
                    })

# Redirect to Original Link
@app.route('/<domain>/<code>')
def redirect_to_url(domain, code):
    original_url = dict.get(code, {}).get('original_url')
    dict[code]['visits'] = dict.get(code, {}).get('visits') + 1
    return redirect(original_url) 

if __name__ == '__main__':
    app.run()