from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

# Serve static files (CSS, JS)
@app.route('/static/<path:filename>')
def send_static(filename):
    return send_from_directory('static', filename)

# Serve form.html as the main page
@app.route('/')
def index():
    return send_from_directory('.', 'form.html')

# Serve index.html
@app.route('/index.html')
def home():
    return send_from_directory('.', 'index.html')

# Serve any other HTML files
@app.route('/<path:filename>')
def serve_file(filename):
    if filename.endswith('.html') or filename.endswith('.css') or filename.endswith('.js'):
        return send_from_directory('.', filename)
    return send_from_directory('.', filename), 404

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
