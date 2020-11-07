#!/usr/bin/python3

# rpyshort
# Simple python program to let you shorten any URL 

from flask import Flask, redirect, request
import redis, uuid

red = redis.Redis(host='localhost', port=6379, db=1, decode_responses=True)

app = Flask(__name__)

@app.route('/<url_id>', methods=['GET'])
def redirect_func(url_id):
  if red.exists(url_id):
    url = red.get(url_id)
    return(redirect(url, code=302))
  else:
    return(f'ID {url_id} wasn\'t found.')

@app.route('/short', methods=['POST'])
def shorten_url(url):
  url_data = request.get_json()
  url_uuid = uuid.uuid4().hex[:8]
  red.set(url_uuid, url_data['url'])
  print(url_uuid)
  return(url_uuid)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5001)

