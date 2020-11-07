# rpyshort
Simple Python app to shorten url

## Installation

In order to make this app work, you will have to have a Redis Server installed, and I will recommend you to have an NGINX server as well for proxying the app.
After this you just have to run it, you could for example use supervisord.

Required libs : 

```
flask
redis
```

### Nginx Configuration Example

```
server {
  listen 80;
  server_name example.com;

  location / {
    proxy_pass http://127.0.0.1:5001;
  }
```

## Usage

For now in order to create a shorten URL you have to send a request with a JSON payload. 
It will return you the generated token, wich will be stored in Redis.

Example with curl : 

```
curl -d '{"url":"https://example.com"} -X POST http://[serverurl]/short'

f68f2184
```

Example for using given UUID : 

```
curl -LI http://[serverurl]/f68f2184

HTTP/1.0 302 FOUND
Content-Type: text/html; charset=utf-8
Content-Length: 247
Location: https://example.com/
Server: Werkzeug/1.0.1 Python/3.7.3
Date: Sat, 07 Nov 2020 21:50:28 GMT
```
