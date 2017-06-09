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

@app.route('/')
def home():
    return render_template('index.html')

@atexit.register
def shutdown():
    pass
    # if client:
    #     client.disconnect()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT, debug=True)

# httpd = Server(("", PORT), Handler)
# try:
#   print("Start serving at port %i" % PORT)
#   httpd.serve_forever()
# except KeyboardInterrupt:
#   pass
# httpd.server_close()

