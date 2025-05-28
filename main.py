from flask import Flask
app = Flask(__name__)

@app.route('/delta')
def hello_name():
  print('hello')
  return 'Hello'

if __name__ == '__main__':
  app.run(host="0.0.0.0", debug=True)
