from flask import Flask, render_template, request
from gevent.wsgi import WSGIServer
app = Flask(__name__)
CF_URL = 'http://bd1bd20de0e06484ccd2-a4b933abf0480693b1cbd92bb7f0259c' + \
         '.r92.cf1.rackcdn.com/'
BOOTSTRAP_THEME = 'bootstrap-theme.min.css'
BOOTSTRAP_CSS = 'bootstrap.min.css'
BOOTSTRAP = 'bootstrap.min.js'
CUSTOM_CSS = 'custom.css'
JQUERY = 'jquery.min.js'
def _render(template_name):
    return render_template(template_name,
                           cf_url=CF_URL,
                           bootstrap_theme=BOOTSTRAP_THEME,
                           bootstrap_css=BOOTSTRAP_CSS,
                           bootstrap=BOOTSTRAP,
                           custom_css=CUSTOM_CSS,
                           jquery=JQUERY)
                                          
@app.route("/")
def home():
    if not request.args.get('l'): 
        return _render('home.html')
    else:
        return _render('es_home.html')
@app.route('/our_story')
def about_us():
    if not request.args.get('l'):
        return _render('our_story.html')
    else:
        return _render('es_our_story.html')
@app.route('/contact_us')
def contact_us():
    if not request.args.get('l'):
        return _render('contact_us.html')
    else:
        return _render('es_contact_us.html')
@app.route('/book/<name>')
def book(name):
    if not request.args.get('l'):
        return _render('book.html')
    else:
        return _render('es_book.html')

if __name__ == "__main__":
    ws = WSGIServer(('', 80), app)
    ws.serve_forever()
