from flask import Flask

application = Flask(__name__)

application.secret_key = "Utn34dfRgfdi23"
application.config['SESSION_COOKIE_NAME'] = 'User Cookie'


@application.route('/')
def index():
	return "Hello Kevin, Vinayak, Guo, and Jack! This is additional message0"


if __name__ == '__main__':
	application.run(port=5000, debug=True)