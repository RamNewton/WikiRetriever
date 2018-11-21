from flask import Flask, render_template, request, redirect, url_for, session
import requests

app = Flask(__name__)
app.secret_key = 'abcd'


thisSess = requests.Session()

@app.route('/')
def home():
	print(request.method)
	return render_template('home.html')

@app.route('/processing', methods = ['GET', 'POST'])
def process():
	if(request.method == 'POST'):
		session['kw'] = request.form['kw']
		return redirect(url_for('links'))
	else:
		return "WTF"
@app.route('/links')
def links():
	KW = session['kw']
	URL = "https://en.wikipedia.org/w/api.php"
	PARAMS = {
		'action' : 'query',
		'list' : 'search',
		'srsearch' : KW,
		'format' : 'json',
		'srlimit' : 5
	}
	R = thisSess.get(url = URL, params = PARAMS)
	data = R.json()
	data = data['query']['search']
	url = "https://en.wikipedia.org/wiki/"
	return render_template('links.html', info = data, url = url)

if __name__ == "__main__":
	app.run(debug = True)
