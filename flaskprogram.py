from flask import Flask

app = Flask(__name__)

@app.route('/')

def hello():
	return 'welcomme to jenkins 28_12 day!!!! bye Bhukh lagi heee?? i have only 8 minit'



if __name__ == '__main__':
	app.run(host="0.0.0.0",debug=True)
