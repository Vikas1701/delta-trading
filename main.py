from flask import Flask
app = Flask(__name__)

@app.route('/delta', methods=['POST'])
def hello_name(name):
  print('hello')
  return 'Hello'

if __name__ == '__main__':
  app.run()
