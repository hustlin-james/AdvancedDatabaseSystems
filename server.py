import os
import atexit

from flask import Flask, render_template, request, jsonify
try:
  from SimpleHTTPServer import SimpleHTTPRequestHandler as Handler
  from SocketServer import TCPServer as Server
except ImportError:
  from http.server import SimpleHTTPRequestHandler as Handler
  from http.server import HTTPServer as Server

# Read port selected by the cloud for our application
PORT = int(os.getenv('PORT', 8000))
# Change current directory to avoid exposure of control files
# os.chdir('static')
app = Flask(__name__)

@app.route('/cloud_storage')
def cloud_storage():
    return render_template('cloud_storage.html')

@app.route('/')
def home():
    return render_template('index.html')

@atexit.register
def shutdown():
    pass
    # if client:
    #     client.disconnect()

if __name__ == '__main__':
    res = os.path.isfile('vcap-local.json')

    if res:
        with open('vcap-local.json') as f:
            objectstorage_creds = json.load(f)
            auth_url = objectstorage_creds['auth_url'] + '/v3'  #authorization URL
            password = objectstorage_creds['password'] #password
            project_id = objectstorage_creds['projectId'] #project id
            user_id = objectstorage_creds['userId'] #user id 
            region_name = objectstorage_creds['region'] #region name 
    else:
        print("no credential files")
    app.run(host='0.0.0.0', port=PORT, debug=True)

# httpd = Server(("", PORT), Handler)
# try:
#   print("Start serving at port %i" % PORT)
#   httpd.serve_forever()
# except KeyboardInterrupt:
#   pass
# httpd.server_close()

