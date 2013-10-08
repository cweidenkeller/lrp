from flask import Flask, render_template, request
from gevent.wsgi import WSGIServer
app = Flask(__name__)

@app.route("/")
def home():
    if not request.args.get('l'): 
        return render_template('home.html')
    else:
        return render_template('es_home.html')
@app.route('/our_story')
def about_us():
    if not request.args.get('l'):
        return render_template('our_story.html')
    else:
        return render_template('es_our_story.html')
@app.route('/contact_us')
def contact_us():
    if not request.args.get('l'):
        return render_template('contact_us.html')
    else:
        return render_template('es_contact_us.html')
@app.route('/book/<name>')
def book(name):
    if not request.args.get('l'):
        return render_template('book.html')
    else:
        return render_template('es_book.html')

if __name__ == "__main__":
    #app.run(port=80, host='0.0.0.0', debug=True)
    ws = WSGIServer(('', 80), app)
    ws.serve_forever()
